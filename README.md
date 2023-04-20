# Hotel-recommendation-system
Recommendation system is a useful tool that takes into account an individual's opinion in order to identify their contents more correctly and selectively. Due to the abundance of internet information, the growth rate of online hotel searching has been significantly faster in recent years, making this online hotel searching a very challenging work.Travelers' reviews replace word-of-mouth, but searching becomes a time-consuming job dependent on user preferences.
Reviews scraped from tourists visiting sites are a popular and useful source of information for hotel suggestions, but little attention has been made to how to show reviewers' reviews in a comprehensible style. As a result, our project has focused on predicting ratings for the hotels based on reviewer comments and establishing a recommendation system that proposes the top three hotels in the area that are exclusive to the user, taking into account the aforementioned tendencies.

### Steps
1. Predict ratings: Predicting ratings for hotels based on reviewer comments by using K-means clustering algorithm.
2. Spark recommendation model: Building an Apache Spark model to generate recommendations for hotels using Alternating Least Squares algorithm.

### System 
1. Data pre-processing: Collecting the data on the hotels and users which is - review comments given by user and rating received by hotels. For each hotel listing, created a feature vector representing its attributes - listing_id,Hotel_name,reviewer_id,reviewer_name,rating,comments etc. For each user, created a vector representing their preferences, based on their past behavior, ratings, and interactions.
</br>
2. TF-IDF vectorization: Term Frequency - Inverse Document Frequency is a method to transform text or documents into a vector form which can be used for analysis. 
Term Frequency(TF) - which is the number of times a specific word or text appears in the document. 
Inverse document frequency(IDF) - Weight of the word or term which is given by (IDF), it gives the rarer term a higher weight and lower weight for a common term.
<p align="center"> <img width="586" alt="Screenshot 2023-04-20 at 1 13 08 PM" src="https://user-images.githubusercontent.com/98439391/233477639-693584cc-d2ff-43d2-a726-c4a573da89e7.png">
</p>
</br>
3. k-means clustering: Used k-means clustering to group similar listings together based on their feature vectors. Each listing will belong to one and only  one cluster. The number of clusters will depend on the size of the dataset and the desired level of granularity.
Generated clusters look like this - 
<p align="center"> <img width="568" alt="Screenshot 2023-04-20 at 1 25 05 PM" src="https://user-images.githubusercontent.com/98439391/233479998-2efec6e9-4304-4f46-bace-0ff455558fa6.png">
 </p>
 Good vs Bad hotels: The clustering results indicate that the model has given higher rating to a hotel listing when customers recorded more and more positive experiences in the comments. And the review comments of listings which scored low on ratings contained some kind of dissatisfaction expressed by customers regarding the hotel.
 eg. Good rated hotel - Hotel listing with predicted rating of 5 along with reviewer comments
 <p align="center"> <img width="574" alt="Screenshot 2023-04-20 at 1 29 52 PM" src="https://user-images.githubusercontent.com/98439391/233481098-09715c5f-0443-4852-8d71-21b02e4afb91.png">
  </p>
 eg. Bad rated hotel - Hotel listing with predicted rating of 1 along with reviewer comments
 <p align="center"> <img width="572" alt="Screenshot 2023-04-20 at 1 31 58 PM" src="https://user-images.githubusercontent.com/98439391/233481316-134f192c-800e-462b-9d2b-708425e56d92.png">
  </p>
</br>
4. Build recommendation system: 
</br>
5. Check predicted ratings
<p align= "center"><img width="402" alt="Screenshot 2023-04-20 at 1 39 42 PM" src="https://user-images.githubusercontent.com/98439391/233482916-5e0090b5-e293-477d-96da-62eb78a3f385.png">
</p>
</br>
6. Hyperparameter tuning and cross-validation: To improve the prediction accuracy we choose to do hyperparameter tuning and find the best parameters. 
We performed grid search on the hyperparameters with three-fold cross validation to obtain the best parameters. We then tuned our ALS model with these best parameters.
</br>
7. Model evaluation using test data: We choose to evaluate our model using Root Mean Square Error. Since the errors are squared before they are averaged, the RMSE gives a relatively high weight to large errors. This makes RMSE more useful when large errors are particularly undesirable like in our recommendation system.
</br>
8. Generate recommendations: Our recommendation system recommends listing to the user, based on collaborative filtering. Our recommendation system takes as input the ALS model, “reviewer_id” and an integer indicating the number of listings we would like to suggest to the user and suggest those many recommended properties to the user.
recommendListings function definition:
<p align= "center"><img width="1189" alt="Screenshot 2023-04-20 at 1 44 06 PM" src="https://user-images.githubusercontent.com/98439391/233483594-82b88871-8aa6-4951-9b33-7ca421bc67c6.png">
</p>
The method prints “n” most favorable listings for the user.
</br>
9. Results
</br>
