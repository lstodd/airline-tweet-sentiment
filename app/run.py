import os

import json
import plotly
import pandas as pd

from flask import Flask
from flask import render_template, request, jsonify
from plotly.graph_objs import Bar
import joblib

from airline_tweet_sentiment.model import tokenize, StartingNounExtractor

app = Flask(__name__)

# load data
df = pd.read_csv(os.path.join("..", "data", "preprocessed_data.csv"))

# load model
model = joblib.load(os.path.join("..", "model.pkl"))


# index webpage displays cool visuals and receives user input text for model
@app.route('/')
@app.route('/index')
def index():
    # extract data needed for visuals
    sentiment_counts = df.airline_sentiment.value_counts()
    sentiment_names = list(sentiment_counts.index)

    sentiment_counts = df.airline_sentiment.value_counts()
    sentiment_names = list(sentiment_counts.index)

    # create visuals
    # TODO: Below is an example - modify to create your own visuals
    graphs = [
        {
            'data': [
                Bar(
                    x=sentiment_names,
                    y=sentiment_counts
                )
            ],

            'layout': {
                'title': 'Histogram of Sentiments',
                'yaxis': {
                    'title': "Count"
                },
                'xaxis': {
                    'title': "Sentiment"
                }
            }
        },
        {
            'data': [
                Bar(
                    x=sentiment_names,
                    y=sentiment_counts
                )
            ],

            'layout': {
                'title': 'Histogram of Sentiments',
                'yaxis': {
                    'title': "Count"
                },
                'xaxis': {
                    'title': "Sentiment"
                }
            }
        }
    ]

    # encode plotly graphs in JSON
    ids = ["graph-{}".format(i) for i, _ in enumerate(graphs)]
    graphJSON = json.dumps(graphs, cls=plotly.utils.PlotlyJSONEncoder)

    # render web page with plotly graphs
    return render_template('master.html', ids=ids, graphJSON=graphJSON)


# web page that handles user query and displays model results
@app.route('/go')
def go():
    # save user input in query
    query = request.args.get('query', '')

    # use model to predict classification for query
    classification_label = model.predict([query])[0]
    categories_dict = {"neutral": 0, "positive": 0, "negative": 0, classification_label: 1}

    # This will render the go.html Please see that file.
    return render_template(
        'go.html',
        query=query,
        category_dict=categories_dict
    )


def main():
    app.run(host='0.0.0.0', port=3001, debug=True)


if __name__ == '__main__':
    main()
