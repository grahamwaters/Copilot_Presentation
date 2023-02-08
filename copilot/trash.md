
## Stage Two: Data Collection
<!-- explain how you collected the data and what the data looks like -->
I used the Spotify API to collect data on songs. I collected data on the following attributes of each song:
* name
* artist
* album
* genre
* danceability
* energy
* key
* loudness
* mode
* speechiness
* acousticness
* instrumentalness
* liveness
* valence
* tempo
* duration_ms
* time_signature

## Stage Three: Data Analysis
<!-- explain how you analyzed the data and what the results were -->
I used Pandas to clean the data and then used Seaborn to visualize the data. I also used Scikit-Learn to run a linear regression model to predict the danceability of a song based on the other attributes of the song. The results of the model were not very good, but I was able to use the model to identify the most important attributes for predicting danceability.

## Stage Four: Machine Learning
<!-- explain how you used the data to build a machine learning model and what the model is -->
I used the Scikit-Learn library to build a K-Nearest Neighbors model. The model takes in a song as input and returns the three most similar songs based on the attributes of the song. The model is currently only trained on songs in the Top 200 charts of the US, UK, and Canada, but I plan to extend the model to include songs from other countries and other genres.

## Stage Five: Deployment
<!-- explain how you deployed the model and how it is being used -->
I deployed the model using Flask. The model is currently being used by a small group of friends and family members. I plan to extend the model to include songs from other countries

## Stage One: Brainstorming


https://open.spotify.com/track/3a8b6uo4vnQSJroGhaNhgG?si=356d59465eb548a0
