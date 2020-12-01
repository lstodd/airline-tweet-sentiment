# airline-tweet-sentiment
Classifying tweets about airlines into positive, negative and neutral. 

With an increasing social media presence for airlines, there is a demand for immediate responses to issues that may 
arise when travelling. In order to respond to tweets appropriately, it makes sense for us to target our resources to
 answering negative tweets first, and help sort out our customer issues. 

In order to do this appropriately, we might want to classify tweets to be able to provide a targeted response. In the 
future we might want to build a bot to reply, and for this we will need to be able to know about the sentiment of the tweets.

## Data

The original data consists of messages of different sentiments, sourced from Kaggle:
https://www.kaggle.com/crowdflower/twitter-airline-sentiment

The three main sentiments are:
* neutral
* positive
* negative

Since we care about responding to the negative tweets quicker, in this project we create a binary target with negative 
sentiment vs other. 

Data has been saved in this repository:
**data/Tweets.csv**

![Classify](/app/screenshots/sentiment_histogram.PNG)

![Classify](/app/screenshots/airline_histogram.PNG)

## Model

We create a multi binary model using XGBoost.

## Requirements:
* pandas
* jupyter
* matplotlib
* seaborn
* nltk
* scikit-learn
* flask
* plotly
* luigi
* xgboost

## Running

To run the luigi pipeline:

1. First create a venv with the requirements installed.
1. Start the luigi scheduler by running the following command in a terminal
    ```luigid --port 8082```
1. Run the ```run.py``` script from the top directory to run the pipeline
1. Run the following command in the app's directory to run the web app. 
```python run.py```
   Go to http://localhost:3001

## Web App

To classify a new message using the trained model you can enter a message on the web app:

![Classify](/app/screenshots/classify_tweet.PNG)

After clicking the 'classify' button, you will see the selected categories for your message highlighted in green:

![Sentiment](/app/screenshots/highlighted_sentiment.PNG)

## Conclusion
# TODO add feature importance note

### Reflection

### Improvement

