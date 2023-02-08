
# use sentiment analysis in VADER to analyze the sentiment of each chapter of Great Expectations by Charles Dickens. Use the Gutenberg Project API to get the text of the book. Use the nltk library to tokenize the text into sentences. Use the VADER sentiment analyzer to get the sentiment of each sentence. Use the seaborn library to plot the sentiment of each sentence as a swarm plot. Use the matplotlib library to add a title to the plot. Use the matplotlib library to save the plot as a png file.

import requests
import nltk
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import sent_tokenize
import seaborn as sns
import matplotlib.pyplot as plt

def get_book():
    """
    get_book Use the Gutenberg Project API to get the text of the book.
    """
    book = requests.get('http://www.gutenberg.org/files/1400/1400-0.txt').text
    return book

def tokenize(book):
    """
    tokenize Use the nltk library to tokenize the text into sentences.
    """
    sentences = sent_tokenize(book)
    return sentences

def get_sentiment(sentences):
    """
    get_sentiment Use the VADER sentiment analyzer to get the sentiment of each sentence.
    """
    analyzer = SentimentIntensityAnalyzer()
    sentiment_scores = []
    for sentence in sentences:
        sentiment_score = analyzer.polarity_scores(sentence)
        sentiment_scores.append({'sentence': sentence, 'compound': sentiment_score['compound']})
    return sentiment_scores

def swarm_plot(sentiment_scores):
    """
    swarm_plot Use the seaborn library to plot the sentiment of each sentence as a swarm plot.
    """
    df = pd.DataFrame(sentiment_scores)
    plt.figure(figsize=(10, 5))
    sns.swarmplot(x='compound', y='sentence', data=df)
    plt.title('Sentiment of each sentence in Great Expectations')
    plt.xlabel('Sentiment Score')
    plt.ylabel('Sentence')
    plt.legend(loc='upper right')
    plt.savefig('sentiment.png')
    plt.show()

def add_title():
    """
    add_title Use the matplotlib library to add a title to the plot.
    """
    plt.title('Sentiment of each sentence in Great Expectations')

def save_plot():
    """
    save_plot Use the matplotlib library to save the plot as a png file.
    """
    plt.savefig('greatexpectations_sentmap.png')

def great_expectations():
    """
    great_expectations Use sentiment analysis in VADER to analyze the sentiment of each chapter of Great Expectations by Charles Dickens. Use the Gutenberg Project API to get the text of the book. Use the nltk library to tokenize the text into sentences. Use the VADER sentiment analyzer to get the sentiment of each sentence. Use the seaborn library to plot the sentiment of each sentence as a swarm plot. Use the matplotlib library to add a title to the plot. Use the matplotlib library to save the plot as a png file.
    """
    book = get_book()
    sentences = tokenize(book)
    sentiment_scores = get_sentiment(sentences)
    swarm_plot(sentiment_scores)
    add_title()
    save_plot()

if __name__ == '__main__':
    great_expectations()
