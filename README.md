# Hotel-recommendation-system
Recommendation system is a useful tool that takes into account an individual's opinion in order to identify their contents more correctly and selectively. Due to the abundance of internet information, the growth rate of online hotel searching has been significantly faster in recent years, making this online hotel searching a very challenging work.Travelers' reviews replace word-of-mouth, but searching becomes a time-consuming job dependent on user preferences.
Reviews scraped from tourists visiting sites are a popular and useful source of information for hotel suggestions, but little attention has been made to how to show reviewers' reviews in a comprehensible style. As a result, our project has focused on predicting ratings for the hotels based on reviewer comments and establishing a recommendation system that proposes the top three hotels in the area that are exclusive to the user, taking into account the aforementioned tendencies.

### Steps
1. Predicting rating: Predict rating for hotels based on reviewer comments by using K-means clustering algorithm.
2. Spark recommendation model: Building a Apache Spark program to generate recommendations for hotels using Alternating Least Squares Algorithm.

### System 
1. Data pre-processing: This step involved dropping nulls, performing data cleaning to remove non-text characters/ html characters and performing data    validation to keep only valied english characters.</br>
<p align="center">     <img width="400" height="120" alt="Screenshot 2023-04-20 at 12 59 59 PM" src="https://user-images.githubusercontent.com/98439391/233475021-12453f4f-c4c0-4198-9ce8-550e29b55d9c.png" align="center">
   </br><img width="400" height="160" alt="Screenshot 2023-04-20 at 1 00 34 PM" src="https://user-images.githubusercontent.com/98439391/233475107-e848d6e2-d9cb-4272-95c7-7ec8b818a91a.png" align="center"> 
</p>
3. TF-IDF vectorization: Inverse Document Frequency Term Frequency is a method to transform text or a word into a vector form which can be used for analysis. It is the amalgamation of Term Frequency(TF) as shown in Fig A, which is the number of times a specific word or text appears in the document. And the weight of the word or term which is given by Inverse Document Frequency(IDF) as shown in Fig B. To conclude, it gives the rarer term a higher weight and lower weight for a common term.
4. k-means clustering: 
5. Build recommendation system: 
6. Check predicted ratings
7. Hyperparameter tuning and cross-validation
8. Model evaluation using test data
9. Generate recommendations
10. Results
