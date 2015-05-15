Here are some next steps you may be excited about after this workshop.

# Get Better at Python
[Dive Into Python](http://www.diveintopython.net/) (great tutorial for someone with some programming experience. It walks you through very practical and useful examples.)

[Learn Python The Hard Way](http://learnpythonthehardway.org/book/) (recommended for total beginners; this tutorial assumes you know nothing - which means you’ll be learning about conditionals and loops. it also helps familiarize you with the syntax)

[Hitchhiker’s Guide to Python (DON’T PANIC)](http://docs.python-guide.org/en/latest/index.html) (if you already know how to code, how to get Python to do what you want)

# Dive deeper on NLTK and TextBlob
* [NLTK Intro, Python 3](http://www.nltk.org/book/)
* [NLTK Intro, Python 2](http://www.nltk.org/book_1ed/)
* [TextBlob Quickstart Tutorial](http://textblob.readthedocs.org/en/dev/quickstart.html)

# Regular Expressions
A way to define specific patterns of characters. Useful for searching searching and filtering. Not particularly easy to read, but very powerful.

[RegexOne](http://regexone.com/) - Learn regular expressions interactively online.

# Topic Modeling
Topic Modeling models features of documents by assuming they were created from a mix of a user-defined number of “topics”, which themselves are distributions of words. 

These topics can be informative but can also be kind of confusing. They’re most helpful for boiling down texts to a reduced set of “features”, for use in other modeling techniques.

* [Gensim](https://radimrehurek.com/gensim/), Python library for topic modeling. Gets mixed reviews.
* [An intro to how LDA works](http://blog.echen.me/2011/08/22/introduction-to-latent-dirichlet-allocation/)
* [Another intro to how LDA works](http://tedunderwood.com/2012/04/07/topic-modeling-made-just-simple-enough/)

## An Alternative to Traditional Topic Modeling
We at Datascope have had good luck using Wikipedia as a labeled corpus, and doing paragraph-wise or sentence-wise similarity between a document and every article on Wikipedia to create “topic” features for that document. These article-based labels are much easier for humans to read and use than LDA “bags of words“.

We use ElasticSearch to do similarity quickly. It’s kind of a pain to set up and use, but it’s very fast.

# Sentiment Analysis
[A comparison of sentiment analysis tools on Yelp data](http://fotiad.is/blog/sentiment-analysis-comparison/?utm_content=bufferecaeb&utm_medium=social&utm_source=twitter.com&utm_campaign=buffer) (the outshot: it’s much easier to do well with labeled data + a classifier than it is to assign “sentiment scores” accurately)

# Machine Learning
[How to build a simple classifier with TextBlob](http://textblob.readthedocs.org/en/dev/classifiers.html)

[Scikit Learn](http://scikit-learn.org/stable/), Python’s premier machine learning library 

[Accuracy is Not Enough](http://machinelearningmastery.com/classification-accuracy-is-not-enough-more-performance-measures-you-can-use/) - how to tell is actually informative at all


# Other Useful Python Packages
## Text stuff
* [newspaper](http://newspaper.readthedocs.org/en/latest/) helps you download news articles off the web.

from Datascope:
* [Textract](https://github.com/deanmalmgren/textract): extract text (or at least attempt to) from images, PDF,  MS Office files, audio, and more…
* [Scrubadub](https://github.com/deanmalmgren/scrubadub): tool for removing personally identifiable data from text while retaining traceable identities (currently in alpha) 

## Data acquisition
* [Requests](http://docs.python-requests.org/en/latest/) is the best way to download data from websites and APIs into Python

## Data manipulation
* [Pandas](http://pandas.pydata.org/) adds some convenient data structures to Python for dealing with time series and tabular data. If you’re familiar with R, Pandas makes Python a little more R-like

## Data modeling
* [Statsmodels](http://statsmodels.sourceforge.net/), a library for stats nerds
* [Scikit Learn](http://scikit-learn.org/stable/), Python’s premier machine learning library 
* [Gensim](https://radimrehurek.com/gensim/), for topic modeling techniques. Gets mixed reviews.

## Data presentation
* [Matplotlib](http://matplotlib.org/) is Python’s main plotting library, with Matlab-like syntax and flexibility, if not the nicest defaults.
* [Seaborn](http://stanford.edu/~mwaskom/software/seaborn/) tweaks the matplotlib defaults to make them nicer, and adds on additional plot types, color theming abilities, and other niceties.
