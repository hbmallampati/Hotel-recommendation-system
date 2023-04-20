from pyspark.sql import SparkSession
from pyspark import SparkContext
import argparse
from pyspark.ml.recommendation import ALS
from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.sql.types import *
from pyspark.sql.functions import lit


def trainTestSplit(data):
    return  data.randomSplit([0.8,0.1,0.1])

def buildALSModel(data):
    als =  ALS(maxIter=10,rank=10,regParam=0.2,nonnegative=True, userCol="reviewer_id", itemCol="listing_id",ratingCol="Rating",coldStartStrategy="drop")
    model = als.fit(data)
    return model

def predictRatings(model, data):
    predictions = model.transform(data)
    predictions.show()


def evaluateModel(predictions):
    evaluator = RegressionEvaluator(metricName="rmse", labelCol="Rating",predictionCol="prediction")
    rmse = evaluator.evaluate(predictions)
    print ('RMSE is %s' % rmse)


def kfoldALS(data, k=3, userCol="reviewer_id", itemCol="listing_id", ratingCol="Rating", metricName="rmse"):
        evaluations = []
        weights = [1.0] * k
        splits = data.randomSplit(weights)
        for i in range(0, k):  
            testingSet = splits[i]
            trainingSet = spark.createDataFrame(sc.emptyRDD(), data.schema)
            for j in range(0, k):
                if i == j:
                    continue
                else:
                    trainingSet = trainingSet.union(splits[j])
            als = ALS(maxIter=10,rank=10,regParam=0.2,nonnegative=True, userCol=userCol, itemCol=itemCol, ratingCol=ratingCol,coldStartStrategy="drop")
            model = als.fit(trainingSet)
            predictions = model.transform(testingSet)
            evaluator = RegressionEvaluator(metricName=metricName, labelCol="Rating", predictionCol="prediction")
            evaluation = evaluator.evaluate(predictions.na.drop())
            print ("Loop " + str(i+1) + ": " + metricName + " = " + str(evaluation))
            evaluations.append(evaluation)
        return sum(evaluations)/float(len(evaluations))

def recommendListings(model, user, n):
        dataSet = data.select("listing_id").distinct().withColumn("reviewer_id", lit(user))
        AlreadyRated = data.filter(data.reviewer_id == user).select("listing_id", "reviewer_id")
        predictions = model.transform(dataSet.subtract(AlreadyRated)).dropna().orderBy("prediction", ascending=False).limit(n).select("listing_id", "prediction")
        predictions.show(truncate=False)
        print ("Top 3 listings recommended for:%d" % user)

    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = 'Hotel Recommendation System', formatter_class=argparse.ArgumentDefaultsHelpFormatter)    
    parser.add_argument('-i', '--input', help='Input file of listing ratings.')
    parser.add_argument('-o', '--output', help='Input file of listing ratings.')
    parser.add_argument('--master', default="local[8]", help="Specify the deploy mode")
    args = parser.parse_args()
  
    sc = SparkContext(args.master, 'HotelReco')

    # Spark session
    spark = SparkSession \
    .builder \
    .appName("HotelReco") \
    .config("spark.hotelreco.proj", "1") \
    .getOrCreate()

   
    # Loading and Parsing Dataset
    ratings = spark.read \
    .format("csv") \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .load(args.input)

    print("Ratings : ,", ratings)

    data = ratings.select('reviewer_id','listing_id','Rating')

    # Splitting data into train, val and test
    (trainingData, validationData, testData) = trainTestSplit(data)

    #Build ALS model
    als = ALS(maxIter=10,rank=10,regParam=0.2,nonnegative=True, userCol="reviewer_id", itemCol="listing_id",ratingCol="Rating",coldStartStrategy="drop")
    # Train ALS model with training data
    cvModel = als.fit(trainingData)
    # Predict ratings from built ALS model
    pred = cvModel.transform(validationData)
        
    # Evaluate the model by computing RMSE
    evaluator = RegressionEvaluator(metricName="rmse", labelCol="Rating",predictionCol="prediction")
    rmse = evaluator.evaluate(pred)
    print ('Total RMSE is %s' % rmse)

    sc = spark.sparkContext
    print ("RMSE = " + str(kfoldALS(validationData, k=4)))

    userRecs = cvModel.recommendForAllUsers(3)
    #userRecs.where(userRecs.reviewer_id == 53).select("recommendations.listing_id", "recommendations.Rating").collect()

    user = 12814
    rec = recommendListings(cvModel,int(args.output),3)


    



    
