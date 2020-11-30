import luigi
from tasks import Run

if __name__ == "__main__":
    luigi.build([Run()])
