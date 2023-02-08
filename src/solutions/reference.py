# Basic Libraries
import collections, datetime, functools, itertools, json, math, operator, os, random, re, string, sys, time, unicodedata, warnings
from datetime import datetime

# Data Visualization
import matplotlib.pyplot as plt, numpy as np, pyplot, pywaffle, seaborn as sns
import bokeh.io as bkio, bokeh.models as bkmd, bokeh.palettes as bkpl, bokeh.plotting as bkpt, bokeh.transform as bktr
import plotly.express as px, plotly.graph_objs as go

# Data Storage and Analysis
import nltk, pandas as pd

# Excel Files
import openpyxl, xlrd, xlwt, xlsxwriter

# Text Analysis
import textblob, vaderSentiment, sentiment_analyzer, afinn, textatistic

# Web Scraping and Requests
import requests, bs4, tldextract

# Financial Data
import yfinance as yf

# Rate Limiting
from ratelimit import limits, sleep_and_retry

# Machine Learning
import catboost as cat, keras, lightgbm as lgb, numpy.linalg as linalg, scipy, scipy.stats as stats, sklearn, statsmodels.api as sm, statsmodels.formula.api as smf, xgboost as xgb
import keras.callbacks as krcb, keras.layers as krly, keras.models as krmd, keras.preprocessing as krpp
import patsy, sklearn.cluster as skc, sklearn.decomposition as skd, sklearn.ensemble as ske, sklearn.linear_model as sklm, sklearn.manifold as skm, sklearn.metrics as skmtr, sklearn.model_selection as skms, sklearn.naive_bayes as sknb, sklearn.neighbors as skn, sklearn.preprocessing as skpp, sklearn.svm as sksvm, sklearn.tree as skt
import tensorflow as tf, tensorflow_datasets as tfds

# Deep Learning
import keras.applications as kra, torch, torch.autograd as tat, torch.nn as tnn, torch.optim as top, torch.utils.data as tud, torchvision, torchvision.transforms as tvt
import torchtext, torchtext.data as ttd, torchtext.datasets as ttds

# Stochastic Libraries
import numpy.fft as nfft, numpy.matlib as nmlib, numpy.polynomial as npoly, numpy.random as npr, pyro, sympy
import pyro.contrib.autoguide as pyca, pyro.distributions as pyd, pyro.infer as pyi, pyro.optim as pyop, pyro.poutine as pyp
import pyro.ops.indexing as pyi, pyro.ops.sample as pys, pyro.ops.stats as pys, pyro.ops.stats.gaussian_kernel as pysgk, pyro.ops.stats.histogram as pysh, pyro.ops.stats.median as pysm, pyro.ops

# Natural Language Processing
import gensim, nltk, spacy, textblob, vaderSentiment, sentiment_analyzer, afinn, textatistic

# Image Processing
import cv2, imageio, matplotlib.image as mpimg, matplotlib.pyplot as plt, numpy as np, PIL, PIL.Image as Image, PIL.ImageDraw as ImageDraw, PIL.ImageFont as ImageFont, PIL.ImageOps as ImageOps, scipy, scipy.ndimage as ndimage, skimage, skimage.color as skc, skimage.feature as skf, skimage.filters as skfi, skimage.io as skio, skimage.measure as skm, skimage.morphology as skmo, skimage.transform as skt, skimage.util as sku

# Audio Processing
import librosa, librosa.display, matplotlib.pyplot as plt, numpy as np, scipy, scipy.io.wavfile as wav, scipy.signal as sig, soundfile as sf, sounddevice as sd

# Video Processing
import cv2, imageio, matplotlib.pyplot as plt, numpy as np, PIL, PIL.Image as Image, PIL.ImageDraw as ImageDraw, PIL.ImageFont as ImageFont, PIL.ImageOps as ImageOps, scipy, scipy.ndimage as ndimage, skimage, skimage.color as skc, skimage.feature as skf, skimage.filters as skfi, skimage.io as skio, skimage.measure as skm, skimage.morphology as skmo, skimage.transform as skt, skimage.util as sku


## prompts to highlight in the presentation
# 1 - write a function that parses the text on drudge report and returns a list of links to articles
# 2 - write a function that uses pandas to automatically generate a dataframe with the columns cast to the type of the first row in a csv file passed to the function as an argument. The function should return the dataframe and the column names as a list of strings.
# 3 - write a function that takes a list of strings and returns a list of strings with the first letter capitalized
# 4 - write a function to tell me the last price of AAPL stock and print it to the screen
# 5 - write a function that pulls the titles of all articles on the drudge report and then performs a basic sentiment analysis on them. The function should return a list of tuples with the title and the sentiment score. This feeds into function six.
# 6 - Rewrite function 1 to find the titles of the articles instead of the links. This feeds into function 7.
# 7 - Create a grid plot of the sentiment scores of all article titles on the drudge report page right now. where the color of the square is the sentiment score, the position has no meaning, and the size of the square is the number of words in the title. The function should return the plot and save it to a file called drudge_report_sentiment_date.png where date is the current date and time converted to string format suitable for a filename.
# example one
def get_drudge_links():
    #* get the html from drudge report
    r = requests.get('http://www.drudgereport.com/')
    #* parse the html
    page_soup = soup(r.text, 'html.parser')
    #* get the links
    links = page_soup.findAll('a')
    #* initialize a list to hold the links
    link_list = []
    #* loop over the links and add them to the list
    for link in links:
        link_list.append(link['href'])
    #* return the list
    return link_list
# example two
def get_csv_column_types(csv_file):
    #* read in the csv file as a dataframe
    df = pd.read_csv(csv_file)
    #* get the column names
    column_names = list(df.columns)
    #* convert the dataframe to a list of lists
    df = df.values.tolist()
    #* initialize a list to hold the types of the first row
    column_types = []
    #* loop over the first row to get the types
    for i in df[0]:
        column_types.append(type(i))
    return df, column_names, column_types
# example three
def capitalize_list_of_strings(list_of_strings):
    return [i.capitalize() for i in list_of_strings]
# example four
def get_aapl_price():
    #* get the data for AAPL
    aapl = yf.Ticker('AAPL')
    #* get the last price
    last_price = aapl.history(period='1d')['Close'][0]
    return last_price
# helper function to rate limit the requests
@sleep_and_retry
def request_page(url):
    #* get the html
    r = requests.get(url)
    #* parse the html
    page_soup = soup(r.text, 'html.parser')
    #* get the title
    title = page_soup.title.text
    #* get the sentiment score
    sentiment_score = TextBlob(title).sentiment.polarity
    #* return the title and the sentiment score
    return title, sentiment_score
# example six and seven and their helper functions
#! I asked for these to be generated
def title_diviner(href):
    # get the title of the article from a link passed to the function. The title is the text between the last / and the last - in the link.
    #* get the index of the last /
    last_slash = href.rfind('/')
    #* get the index of the last -
    last_dash = href.rfind('-')
    #* get the title
    title = href[last_slash+1:last_dash]
    # replace the dashes with spaces
    title = title.replace('-', ' ')
    #* return the title
    return title
def get_drudge_titles():
    """
    parses the html returned by bs4 from drudge report and returns a list of the article titles. This feeds into function seven.
    """
    #* get the html from drudge report
    r = requests.get('http://www.drudgereport.com/')
    #* parse the html
    page_soup = soup(r.text, 'html.parser')
    #* get the links
    links = page_soup.findAll('a')
    #* initialize a list to hold the links
    titles = []
    #* loop over the links and add them to the list
    for link in links:
        real_title = title_diviner(link['href'])
        # remove any numbers from the title to avoid errors by replacing them with blank spaces
        real_title = re.sub(r'\d+', '', real_title)
        # remove double spaces
        real_title = re.sub(' +', ' ', real_title)
        titles.append(real_title)
    #* return the list
    return titles
def drudge_sentiment_mapping():
    """
    takes the titles of the articles on the drudge report and performs a basic sentiment analysis on them. The function returns a list of tuples with the title and the sentiment score. This feeds into function seven.
    """
    #* get the titles
    titles = get_drudge_titles()
    links = get_drudge_links()
    #* initialize a list to hold the titles and sentiment scores
    title_sentiment = []
    #* loop over the titles and get the sentiment scores
    for title in titles:
        #* get the sentiment score
        sentiment_score = TextBlob(title).sentiment.polarity
        #* add the title and the sentiment score to the list if the title is more than 1 word
        if len(title.split()) > 1:
            title_sentiment.append((title, sentiment_score))
        else:
            pass
    #* return the list
    return title_sentiment

def get_domain_name(url):
    """
    takes a url and returns the domain name of the url. This feeds into function nine.
    """
    #* get the domain name
    domain_name = tldextract.extract(url).domain
    #* return the domain name
    return domain_name

# creating a swarm plot
def swarm_plot(df, x, y, hue, title, xlabel, ylabel, filename):
    """
    swarm_plot Make a swarmplot of these five domains using their sentiment scores with individual points representing titles, y-axis representing the domain name and x-axis representing the sentiment score.

    :param df: _description_
    :type df: _type_
    :param x: _description_
    :type x: _type_
    :param y: _description_
    :type y: _type_
    :param hue: _description_
    :type hue: _type_
    :param title: _description_
    :type title: _type_
    :param xlabel: _description_
    :type xlabel: _type_
    :param ylabel: _description_
    :type ylabel: _type_
    :param filename: _description_
    :type filename: _type_
    """

    #* initialize the plot
    plt.figure(figsize=(10, 5))
    #* make the swarm plot
    sns.swarmplot(x=x, y=y, hue=hue, data=df)
    #* set the title
    plt.title(title)
    #* set the x label
    plt.xlabel(xlabel)
    #* set the y label
    plt.ylabel(ylabel)
    #* set the legend
    plt.legend(loc='upper right')
    #* save the plot
    plt.savefig(filename)
    #* show the plot
    plt.show()


def main():
    # part 1 - Get links from the drudge report
    drudge_links = get_drudge_links()
    # part 2 - Get the titles from the links
    drudge_titles = get_drudge_titles()
    # part 3 - Get the sentiment scores from the titles
    drudge_sentiment = drudge_sentiment_mapping()
    # part 4 - Get the domain names from the links
    drudge_domains = [get_domain_name(i) for i in drudge_links]
    # part 5 - Get the top 5 domains
    top_five_domains = Counter(drudge_domains).most_common(5)
    # part 6 - Get the top 5 domains and their sentiment scores
    top_five_domains_sentiment = []
    for domain in top_five_domains:
        #* get the domain name
        domain_name = domain[0]
        #* get the sentiment scores for the domain
        domain_sentiment = [i[1] for i in drudge_sentiment if domain_name in i[0]]
        #* get the average sentiment score
        domain_sentiment_average = sum(domain_sentiment) / len(domain_sentiment)
        #* add the domain name and the average sentiment score to the list
        top_five_domains_sentiment.append((domain_name, domain_sentiment_average))
    # part 7 - Make a swarmplot of these five domains using their sentiment scores with individual points representing titles, y-axis representing the domain name and x-axis representing the sentiment score.
    #* create a dataframe
    df = pd.DataFrame(top_five_domains_sentiment, columns=['domain', 'sentiment'])
    #* make the swarm plot
    swarm_plot(df, 'sentiment', 'domain', None, 'Sentiment of the top 5 domains on the Drudge Report', 'Sentiment', 'Domain', 'swarm_plot.png')

if __name__ == '__main__':
    main()