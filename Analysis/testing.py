import pickle
import pandas as pd
import numpy as np
import xgboost
import xgboost as xgb
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob
import nltk
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import FeatureUnion, Pipeline
from sklearn.feature_extraction import DictVectorizer
from nltk.stem import WordNetLemmatizer, PorterStemmer
from sklearn.preprocessing import MinMaxScaler
import re
import string
from nltk.corpus import stopwords
import streamlit as st
seed=42


normalizer = pd.read_pickle('normalizer.pickle')
analyzer = SentimentIntensityAnalyzer()


def sentiment_scores(s):
    return analyzer.polarity_scores(s)['compound']


def exclamation_percentage(tweet):
    count = np.char.count(tweet, sub='!').sum()
    return count / len(tweet)


def capital_percentage(tweet):
    tokens = nltk.word_tokenize(tweet)
    cap_count = 0
    for item in tokens:
        if item.isupper():
            cap_count += 1
    return cap_count / len(tokens)


def check_profanity(tweet):
    profane = pd.read_csv("profane_words.csv", header=None)

    profane = list(profane.loc[:, 0])
    count = 0
    tweet = tweet.lower()
    tokens = nltk.word_tokenize(tweet)
    for word in tokens:
        if word in profane:
            count += 1
    return count / len(tweet)


def get_subjectivity(tweet):
    b = TextBlob(tweet)
    return b.sentiment.subjectivity


def process_tweet(tweet):
    tweet = str(tweet).lower()
    tokens = nltk.word_tokenize(tweet)
    stopwords_removed = [token.lower() for token in tokens if token.lower() not in stopwords]
    return stopwords_removed


stopwords = stopwords.words('english')
stopwords += list(string.punctuation)
stopwords += ["n't", "' '", "'re'", "”", "``", "“", "''", "’", "'s", "'re", "http", "https", "rt"]
alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
        'w', 'x', 'y', 'z']
stopwords += alph
stopwords = list(set(stopwords))


def remove_http(tweet):
    pattern = '((http|https)\w+\s\w+\s\w+\s\w+)'
    try:
        return tweet.replace(re.findall(pattern, tweet)[0][0], "")
    except:
        return tweet


lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()


def remove_username(tweet):
    try:
        p = '[\w\s]+(@\w+)'
        return tweet.replace(re.findall(p, tweet)[0], "")
    except:
        return tweet


def ReplaceThreeOrMore(tweet):
    # pattern to look for three or more repetitions of any character, including
    # newlines.
    pattern = re.compile(r"(.)\1{2,}", re.DOTALL)
    return pattern.sub(r"\1\1", tweet)


def clean_txt(tweet):
    tweet = remove_http(tweet)
    tweet = remove_username(tweet)
    tweet = ReplaceThreeOrMore(tweet)
    tokens = process_tweet(tweet)
    return ' '.join([lemmatizer.lemmatize(w) for w in tokens])


def clean_txt_2(tweet):
    tweet = remove_http(tweet)
    tweet = remove_username(tweet)
    tweet = ReplaceThreeOrMore(tweet)
    return tweet.lower()


class ItemSelector(BaseEstimator, TransformerMixin):
    def __init__(self, key):
        self.key = key

    def fit(self, x, y=None):
        return self

    def transform(self, data_dict):
        return data_dict[self.key]


class TextStats(BaseEstimator, TransformerMixin):
    """Extract features from each document for DictVectorizer"""

    def fit(self, x, y=None):
        return self

    def transform(self, data):
        rs = []
        for row in data.iterrows():
            to_add = {}
            for item in row[1:]:
                for ind, val in zip(item.index, item.values):
                    to_add[ind] = val
            rs.append(to_add)
        return rs


pipe = pd.read_pickle('pipeline_all.pickle')
model = pd.read_pickle('xgboost.pickle')

try:
    st.title("Election emoji guessing machine!")
    st.text('Type an election related tweet in the box below:')
    data = {'tweet': st.text_input("Enter a tweet! ")}
    data['sentiment_score'] = sentiment_scores(data['tweet'])
    data['sentiment_score'] = normalizer.transform(np.array(data['sentiment_score']).reshape(1, -1))[0][0]
    data['exclamation_points'] = exclamation_percentage(data['tweet'])
    data['capitalization'] = capital_percentage(data['tweet'])
    data['profanity'] = check_profanity(data['tweet'])
    data['subjectivity'] = get_subjectivity(data['tweet'])
    data = pd.DataFrame(data, index=[0])
    train_vec = pipe.transform(data)
    pred = model.predict(train_vec)[0]
    st.write(f"I am guessing your tweet can represented with this: {pred}")
except:
    pass
