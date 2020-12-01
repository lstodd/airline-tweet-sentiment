class Config:
    target_col: str = "airline_sentiment"
    tweet_col: str = "text"
    target_negative_value: str = "negative"
    target_other_value: str = "other"


class Paths:
    data_path: str = "data"


class Files:
    raw_file: str = "Tweets.csv"
    preprocessed_file: str = "preprocessed_data.csv"
    model_file: str = "model.pkl"
    metrics_file: str = "metrics.csv"
