import sys

import pandas as pd

from airline_tweet_sentiment.config import Config


# TODO add docstrings for functions

def _load_data(tweet_file: str) -> pd.DataFrame:
    """
    Load tweet data from file.

    :param tweet_file: Filename containing tweets and target.
    :return: DataFrame containing text and target.
    """
    df = pd.read_csv(tweet_file)

    return df


def _clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Preprocess categories into separate columns.
    :param df: Raw DataFrame containing single column for all labels.
    :return: Cleaned DataFrame.
    """

    df = df[[Config.target_col, Config.tweet_col]]
    df.loc[~(df[Config.target_col] == Config.target_negative_value), Config.target_col] = Config.target_other_value

    return df


def _save_data(df, cleaned_file) -> None:
    """
    Save DataFrame to SQL engine.
    :param df: Cleaned DataFrame.
    :param cleaned_file: Filename to store cleaned data.
    """

    df.to_csv(cleaned_file, index=False)


def preprocess(tweet_file: str, cleaned_file: str):
    print(f"Loading data from {tweet_file}")
    df = _load_data(tweet_file)

    print('Cleaning data...')
    df = _clean_data(df)

    print(f"Saving data to {cleaned_file}")
    _save_data(df, cleaned_file)

    print('Cleaned data saved to database!')
