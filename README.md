# airline-tweet-sentiment
Classifying tweets about airlines into positive, negative and neutral. 

With an increasing social media presence for airlines, there is a demand for immediate responses to issues that may 
arise when travelling. In order to respond to tweets appropriately, it makes sense for us to target our resources to
 answering negative tweets first, and help sort out our customer issues. 

We want to be able to target our responses to messages. In order to do this appropriately, we might want 
to classify tweets to be able to provide a targeted response. In the future we might want to build a bot to reply, and 
for this we will need to be able to know about the sentiment of the tweets.

Having a classification system for incoming tweets will enable us to target our response and focus answering the 
negative tweets quicker.

## Data

The original data consists of messages from multiple sources and the annotated categories and was sourced from Kaggle:
https://www.kaggle.com/crowdflower/twitter-airline-sentiment

Data has been saved in this repository:
**data/Tweets.csv**

## Model

We create a multi class model.

## Requirements:
* pandas
* jupyter
* matplotlib
* seaborn
* nltk
* scikit-learn

## Running
Run the following commands in the project's root directory to set up your database and model.

1. To run ETL pipeline that cleans data and stores in database python airline_tweet_sentiment/process_data.py data/Tweets.csv data/preprocessed_data.csv
2. To run ML pipeline that trains classifier and saves python airline_tweet_sentiment/model.py data/preprocessed_data.csv models.pkl
3. Run the following command in the app's directory to run your web app. 
```python run.py```

    Go to http://localhost:3001

## Conclusion

### Reflection

### Improvement

