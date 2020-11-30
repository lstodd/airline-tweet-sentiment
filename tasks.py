import os
import logging

import luigi

from airline_tweet_sentiment.config import Paths, Files
from airline_tweet_sentiment.preprocess_data import preprocess
from airline_tweet_sentiment.model import create_model

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Global(luigi.Config):
    data_file_path = luigi.Parameter()
    model_file_path = luigi.Parameter()


class PreProcessing(luigi.Task):
    """PreProcess tweet data"""

    @property
    def input_f(self):
        return os.path.join(Paths.data_path, Files.raw_file)

    @property
    def output_f(self):
        return os.path.join(Paths.data_path, Files.preprocessed_file)

    def output(self):
        return [luigi.LocalTarget(self.output_f)]

    def run(self):
        preprocess(tweet_file=self.input_f,
                   cleaned_file=self.output_f)


class Model(luigi.Task):
    """Generate model from preprocessed data."""

    @property
    def output_f(self):
        return Files.model_file

    @property
    def input_f(self):
        return PreProcessing().output()[0].path

    @property
    def metrics_f(self):
        return Files.metrics_file

    def requires(self):
        return [PreProcessing()]

    def output(self):
        return [luigi.LocalTarget(self.output_f),
                luigi.LocalTarget(self.metrics_f)]

    def run(self):
        create_model(data_filepath=self.input_f,
                     model_filepath=self.output_f)


class Run(luigi.WrapperTask):
    def requires(self):
        return Model()
