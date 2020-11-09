import sys

import pandas as pd

from airline_tweet_sentiment.config import Config


# TODO add docstrings for functions

def load_data(tweet_file: str) -> pd.DataFrame:
    """
    Load tweet data from file.

    :param tweet_file: Filename containing tweets and target.
    :return: DataFrame containing text and target.
    """
    df = pd.read_csv(tweet_file)

    return df


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Preprocess categories into separate columns.
    :param df: Raw DataFrame containing single column for all labels.
    :return: Cleaned DataFrame.
    """

    df = df[[Config.target_col, Config.tweet_col]]

    return df


def save_data(df, cleaned_file) -> None:
    """
    Save DataFrame to SQL engine.
    :param df: Cleaned DataFrame.
    :param cleaned_file: Filename to store cleaned data.
    """

    df.to_csv(cleaned_file, index=False)


def main():
    if len(sys.argv) == 3:

        tweet_file, cleaned_file = sys.argv[1:]

        print(f"Loading data from {tweet_file}")
        df = load_data(tweet_file)

        print('Cleaning data...')
        df = clean_data(df)

        print(f"Saving data to {cleaned_file}")
        save_data(df, cleaned_file)

        print('Cleaned data saved to database!')

    else:
        print('Please provide the filepaths of the tweets' \
              'as the first argument, as ' \
              'well as the cleaned filepath to save the cleaned data ' \
              'to as the second argument. \n\nExample: python process_data.py ' \
              'tweets.csv cleaned_tweets.csv')


if __name__ == '__main__':
    main()
