import requests
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import sent_tokenize
import seaborn as sns
import matplotlib.pyplot as plt

# use sentiment analysis in VADER to analyze the sentiment of each chapter of Great Expectations by Charles Dickens. Use the Gutenberg Project API to get the text of the book. Use the nltk library to tokenize the text into sentences. Use the VADER sentiment analyzer to get the sentiment of each sentence. Use the seaborn library to plot the sentiment of each sentence as a swarm plot. Use the matplotlib library to add a title to the plot. Use the matplotlib library to save the plot as a png file.

def get_book():
    """
    get_book Use the Gutenberg Project API to get the text of the book.
    """
    #* get the text of the book
    book = requests.get('http://www.gutenberg.org/files/1400/1400-0.txt').text
    #* return the text
    return book

def tokenize(book):
    """
    tokenize Use the nltk library to tokenize the text into sentences.
    """
    #* tokenize the text into sentences
    sentences = sent_tokenize(book)
    #* return the sentences
    return sentences

def get_sentiment(sentences):
    """
    get_sentiment Use the VADER sentiment analyzer to get the sentiment of each sentence.
    """
    #* initialize the sentiment analyzer
    analyzer = SentimentIntensityAnalyzer()
    #* initialize a list to hold the sentiment scores
    sentiment_scores = []
    #* loop over the sentences
    for sentence in sentences:
        #* get the sentiment score
        sentiment_score = analyzer.polarity_scores(sentence)
        #* add the score to the list
        sentiment_scores.append(sentiment_score)
    #* return the list
    return sentiment_scores

def swarm_plot(sentiment_scores):
    """
    swarm_plot Use the seaborn library to plot the sentiment of each sentence as a swarm plot.
    """
    #* initialize the plot
    plt.figure(figsize=(10, 5))
    #* make the swarm plot
    sns.swarmplot(x='compound', y='sentence', data=sentiment_scores)
    #* set the title
    plt.title('Sentiment of each sentence in Great Expectations')
    #* set the x label
    plt.xlabel('Sentiment Score')
    #* set the y label
    plt.ylabel('Sentence')
    #* set the legend
    plt.legend(loc='upper right')
    #* save the plot
    plt.savefig('sentiment.png')
    #* show the plot
    plt.show()

def add_title():
    """
    add_title Use the matplotlib library to add a title to the plot.
    """
    #* add a title to the plot
    plt.title('Sentiment of each sentence in Great Expectations')

def save_plot():
    """
    save_plot Use the matplotlib library to save the plot as a png file.
    """
    #* save the plot
    plt.savefig('greatexpectations_sentmap.png')



def great_expectations():
    """
    great_expectations Use sentiment analysis in VADER to analyze the sentiment of each chapter of Great Expectations by Charles Dickens. Use the Gutenberg Project API to get the text of the book. Use the nltk library to tokenize the text into sentences. Use the VADER sentiment analyzer to get the sentiment of each sentence. Use the seaborn library to plot the sentiment of each sentence as a swarm plot. Use the matplotlib library to add a title to the plot. Use the matplotlib library to save the plot as a png file.
    """
    #* get the text of the book
    book = get_book()
    #* tokenize the text into sentences
    sentences = tokenize(book)
    #* get the sentiment of each sentence
    sentiment_scores = get_sentiment(sentences)
    #* plot the sentiment of each sentence as a swarm plot
    swarm_plot(sentiment_scores)
    #* add a title to the plot
    add_title()
    #* save the plot as a png file
    save_plot()

if __name__ == '__main__':
    great_expectations()