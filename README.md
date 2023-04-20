# Hotel-recommendation-system
The vast amount of information on the internet has made online hotel searching a daunting task. As a result, recommendation systems have become valuable tools that allow individuals to receive personalized content based on their opinions. Traveler reviews have become a popular source of information for hotel suggestions. This project aims to predict hotel ratings based on reviewer comments and create a recommendation system that suggests the top 'n' hotels in the area based on the user's preferences.

### Steps
1. Predict ratings: Predicting ratings for hotels based on reviewer comments by using K-means clustering algorithm. The reviews will be subjected to sentiment analysis, and machine learning algorithms will be applied to anticipate the rating of the comments and classify them into various rating groups.
2. Spark recommendation model: Building an Apache Spark model to generate recommendations for hotels using Alternating Least Squares algorithm. The use of collaborative filtering will enable the suggestion of the listing to the user by generating a feature matrix based on the user reviews ratings, which are calculated through sentiment analysis to anticipate properties that are suitable for the user.

### System 
#### 1. Data pre-processing: 
Collecting the data on the hotels and users which is - review comments given by user and rating received by hotels. For each hotel listing, created a feature vector representing its attributes - listing_id,Hotel_name,reviewer_id,reviewer_name,rating,comments etc. For each user, created a vector representing their preferences, based on their past behavior, ratings, and interactions.
</br>
#### 2. TF-IDF vectorization: 
Term Frequency - Inverse Document Frequency is a method to transform text or documents into a vector form which can be used for analysis. 
Term Frequency(TF) - which is the number of times a specific word or text appears in the document. 
Inverse document frequency(IDF) - Weight of the word or term which is given by (IDF), it gives the rarer term a higher weight and lower weight for a common term.
<p align="center"> <img width="586" alt="Screenshot 2023-04-20 at 1 13 08 PM" src="https://user-images.githubusercontent.com/98439391/233477639-693584cc-d2ff-43d2-a726-c4a573da89e7.png">
</p>
</br>

#### 3. K-means clustering: 
Used k-means clustering to group similar listings together based on their feature vectors. Each listing will belong to one and only  one cluster. The number of clusters will depend on the size of the dataset and the desired level of granularity.
Generated clusters look like this - 
<p align="center"> <img width="568" alt="Screenshot 2023-04-20 at 1 25 05 PM" src="https://user-images.githubusercontent.com/98439391/233479998-2efec6e9-4304-4f46-bace-0ff455558fa6.png">
 </p>
 
 #### Good vs Bad hotels: 
 The clustering results indicate that the model has given higher rating to a hotel listing when customers recorded more and more positive experiences in the comments. And the review comments of listings which scored low on ratings contained some kind of dissatisfaction expressed by customers regarding the hotel.
 </br>
 eg. Good rated hotel - Hotel listing with predicted rating of 5 along with reviewer comments
 <p align="center"> <img width="574" alt="Screenshot 2023-04-20 at 1 29 52 PM" src="https://user-images.githubusercontent.com/98439391/233481098-09715c5f-0443-4852-8d71-21b02e4afb91.png">
  </p>
 eg. Bad rated hotel - Hotel listing with predicted rating of 1 along with reviewer comments
 <p align="center"> <img width="572" alt="Screenshot 2023-04-20 at 1 31 58 PM" src="https://user-images.githubusercontent.com/98439391/233481316-134f192c-800e-462b-9d2b-708425e56d92.png">
  </p>
</br>

#### 4. Build recommendation system: 
Employed collaborative filtering technique in Apache Spark, made use of Spark ML, ALS algorithm, to build recommendation engine.
</br>

#### 5. Check predicted ratings
We can see that for the first three rows the (actual rating, predicted rating) are (4, 2.941), (3, 2.88), (3, 3.007) which is quite close but we still have some error. To reduce the error and improve the performance we did hyperparameter tuning.
<p align= "center"><img width="402" alt="Screenshot 2023-04-20 at 1 39 42 PM" src="https://user-images.githubusercontent.com/98439391/233482916-5e0090b5-e293-477d-96da-62eb78a3f385.png">
</p>
</br>

#### 6. Hyperparameter tuning and cross-validation: 
To improve the prediction accuracy we choose to do hyperparameter tuning and find the best parameters. We performed grid search on the hyperparameters with three-fold cross validation to obtain the best parameters. We then tuned our ALS model with these best parameters.
</br>
#### 7. Model evaluation using test data: 
I chose to evaluate the model using Root Mean Square Error as in RMSE the errors are squared before they are averaged, thus RMSE gives a relatively high weight to large errors. This makes RMSE more useful when large errors are particularly undesirable like in this recommendation system.
</br>

#### 8. Generate recommendations: 
The recommendation system recommends listing to the user, based on collaborative filtering. The recommendation system takes as input the ALS model, “reviewer_id” and an integer indicating the number of listings we would like to suggest to the user and suggest those many recommended properties to the user.
recommendListings function definition:
<p align= "center"><img width="1189" alt="Screenshot 2023-04-20 at 1 44 06 PM" src="https://user-images.githubusercontent.com/98439391/233483594-82b88871-8aa6-4951-9b33-7ca421bc67c6.png">
</p>
The method prints “n” most favorable listings for the user.
</br>

#### 9. Results
Example 1: For the user with a reviewer_id = 50740909 the three most favorable listings recommended by our system with their predicted ratings are-
<p align="center"><img width="562" alt="Screenshot 2023-04-20 at 1 51 24 PM" src="https://user-images.githubusercontent.com/98439391/233485249-749dec2f-3007-455b-96dd-aa15540270c0.png">
</p>
Example 2: For the user with a reviewer_id = 21814 the three most favorable listings recommended by our system with their predicted ratings are-
<p align="center"><img width="563" alt="Screenshot 2023-04-20 at 1 51 46 PM" src="https://user-images.githubusercontent.com/98439391/233485203-1b10e30f-1bcf-4d99-9d13-12d795c56da9.png">
</p>
Example 3: For the user with a reviewer_id = 32040267 the three most favorable listings recommended by our system with their predicted ratings are- 
<p align="center"><img width="561" alt="Screenshot 2023-04-20 at 1 52 03 PM" src="https://user-images.githubusercontent.com/98439391/233485176-9a1320ae-9b89-4bc9-9eef-e1a64497ec4f.png">
</p>
</br>
