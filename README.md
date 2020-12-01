# airline-tweet-sentiment

This project can be found on GitHub here:
https://github.com/lstodd/airline-tweet-sentiment

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

We create a multi binary model using XGBoost. We create feature for the starting noun of a tweet to help us with the sentiment. 

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
We have a good overall precision for picking up negative tweets, however, we might want to improve on this model before
deploying in the real world. Missing negative tweets can have bad consequences for a company PR. 

## Reflection
We have good performance with only minor preprocessing of the data. Using the web app to test new messages seems to 
work well with spot checks. 

The model took a very long time to train with a large grid for cross validation. 

## Improvement
In terms of the repository as a whole, I would propose to add tests so we can ensure the code is working as it is 
supposed to. 

We could add more preprocessing on the text to generate more interesting Natural Language Processing (NLP) indicators 
for the model to learn from. We could also make sure to split the data for different airlines equally between the 
test/train samples to ensure we perform well on all airlines. To this end, we could even report the performance metrics 
per airline. 

To improve on model training time for a larget hyperparameter grid, we could try and use a parallised approach for
 searching for the optimum parameters. 
