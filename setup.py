import os

import setuptools

rootdir = os.path.abspath(os.path.dirname(__file__))
long_description = open(os.path.join(rootdir, 'README.md')).read()

setuptools.setup(
    name="airline-tweet-sentiment",
    version="0.1",
    author="Laura Stoddart",
    author_email="laurastoddart@hotmail.com",
    description="A package containing a the airline tweet sentiment code.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lstodd/airline-tweet-sentiment.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)