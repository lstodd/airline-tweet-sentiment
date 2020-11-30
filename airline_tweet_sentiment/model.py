import os
from typing import Tuple, List

import pandas as pd
import numpy as np
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.metrics import classification_report
from sklearn.model_selection import GridSearchCV
from sklearn.base import BaseEstimator, TransformerMixin
import nltk

from airline_tweet_sentiment.config import Config, Paths, Files

nltk.download(['punkt', 'wordnet', 'averaged_perceptron_tagger'])

from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer


class StartingNounExtractor(BaseEstimator, TransformerMixin):

    def starting_noun(self, text: str):
        sentence_list = nltk.sent_tokenize(text)
        for sentence in sentence_list:
            pos_tags = nltk.pos_tag(tokenize(sentence))
            first_word, first_tag = pos_tags[0]
            if first_tag in ['NN', 'NNS']:
                return True
        return False

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X_tagged = pd.Series(X).apply(self.starting_noun)
        return pd.DataFrame(X_tagged)


def _load_data(data_filepath: str) -> Tuple[np.array, np.array, np.array]:
    """
    Load the training data from the SQLite database.
    :param data_filepath: Database name to load cleaned data from.
    :return: Training data, target and category nanes for target values.
    """
    df = pd.read_csv(data_filepath)
    X = df[Config.tweet_col].values
    y = df[Config.target_col].values

    return X, y


def tokenize(text: str) -> List[str]:
    """
    Lowers and splits a string up into separate tokens.
    :param text: Raw string to tokenize.
    :return: List of separated tokens.
    """
    tokens = word_tokenize(text)
    lemmatizer = WordNetLemmatizer()

    clean_tokens = []
    for tok in tokens:
        clean_tok = lemmatizer.lemmatize(tok).lower().strip()
        clean_tokens.append(clean_tok)

    return clean_tokens


def _build_model() -> GridSearchCV:
    """
    Build the sklearn model pipeline with paramters to grid search over.
    :return: Sklearn grid searchable pipeline.
    """
    pipeline = Pipeline([
        ('features', FeatureUnion([

            ('text_pipeline', Pipeline([
                ('vect', CountVectorizer(tokenizer=tokenize)),
                ('tfidf', TfidfTransformer())
            ])),

            ('starting_noun', StartingNounExtractor())
        ])),

        ('clf', RandomForestClassifier())
    ])

    # specify parameters for grid search
    parameters = {
        'features__text_pipeline__tfidf__smooth_idf': (True, False),
        # 'clf__estimator__warm_start': (True, False),
        # 'clf__estimator__min_samples_leaf': [2, 3, 4],
    }

    # create grid search object
    cv = GridSearchCV(pipeline, param_grid=parameters, verbose=2)

    return cv


def _evaluate_model(model, X_test, y_test):
    """
    Returns the best parameters from a grid search.
    :param model: Trained model.
    :param X_test: Data for features.
    :param y_test: Actual labels to check against.
    :return: Return the parameters of the best model from grid search.
    """
    y_pred = model.predict(X_test)

    report = classification_report(y_test, y_pred, output_dict=True)
    df_report = pd.DataFrame(report).transpose()
    df_report.to_csv(os.path.join(Paths.data_path, Files.metrics_file))

    print(df_report)

    print("\nBest Parameters:", model.best_params_)


def _save_model(model: GridSearchCV, model_filepath: str) -> None:
    """
    Save the serialised model object.
    :param model: Model object.
    :param model_filepath: Model filename.
    """
    joblib.dump(model, model_filepath)


def create_model(data_filepath: str, model_filepath: str):
    print(f"Loading data...{data_filepath}")
    X, y = _load_data(data_filepath)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

    print('Building model...')
    model = _build_model()

    print('Training model...')
    model.fit(X_train, y_train)

    print('Evaluating model...')
    _evaluate_model(model, X_test, y_test)

    print('Saving model...\n    MODEL: {}'.format(model_filepath))
    _save_model(model, model_filepath)

    print('Trained model saved!')
