import requests
import pandas as pd
import time
import random
import json
import re
import os
import sys
import datetime
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import math
import itertools
import functools
import operator
import collections, functools, operator, itertools, re, string, unicodedata
import nltk
from tqdm import tqdm
# because we will be dealing with stock data it might be useful to import yfinance
import yfinance as yf
import pywaffle

# import now from datetime
from datetime import datetime
import warnings

import tldextract # for getting the domain name from a url

# rate limits
from ratelimit import limits, sleep_and_retry
from bs4 import BeautifulSoup as soup

# for sentiment analysis
from textblob import TextBlob
# for grid plots
from bokeh.plotting import figure, show, output_file
from bokeh.models import HoverTool, ColumnDataSource
from bokeh.transform import factor_cmap
from bokeh.palettes import Spectral6
from bokeh.io import output_notebook

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


# example eight
def make_swarmplot():
    """
    You are a python coder, make a swarmplot using Seaborn. The swarmplot shows the sentiment scores of all article titles on the drudge report page right now. where the color of the square is the sentiment score, the position has no meaning, and the size of the square is the number of words in the title. The function should return the plot and save it to a file called `drudge_report_sentiment_date.png` where date is the current date and time converted to string format suitable for a filename.
    """
    #* get the sentiment scores
    sentiment_scores = drudge_sentiment_mapping()
    #* initialize a list to hold the number of words in the title
    # to get the values to plot we want to extract the second element from the tuples in the sentiment_scores list (i.e. ('over killed after catastrophic earthquakes hit turkey syria', -0.2) has a value of -0.2) and then get the length of the first element in the tuple (i.e. 'over killed after catastrophic earthquakes hit turkey syria' has a length of 9)
    num_words = [len(i[0].split()) for i in sentiment_scores]
    #* initialize a list to hold the sentiment scores
    sentiment = [i[1] for i in sentiment_scores]
    #* initialize a list to hold the titles
    titles = [i[0] for i in sentiment_scores]
    #* make a dataframe to hold the data
    df = pd.DataFrame({'num_words': num_words, 'sentiment': sentiment, 'titles': titles})
    # let's add some features to the dataframe
    # the theme for the plot
    sns.set_theme(style="whitegrid", palette="pastel", color_codes=True, font_scale=1.5, rc={"lines.linewidth": 2.5}, font='sans-serif')
    # Draw a categorical scatterplot to show each observation
    ax = sns.swarmplot(data=df, x="sentiment", y="num_words", palette="muted", dodge=True, size=8)
    # set the x axis to be the sentiment score
    ax.set(xlabel="Sentiment Score")
    # set the y axis to be the number of words in the title
    ax.set(yticks=np.arange(0, 10, 1))
    # label the y axis
    ax.set(yticklabels=['1', '2', '3', '4', '5', '6', '7', '8', '9'])
    ax.set(ylabel="Number of Words in Title")
    ax.set(title="Drudge Report Sentiment Analysis")
    #* save the plot
    plt.savefig(f'drudge_report_sentiment_{datetime.now().strftime("%Y-%m-%d-%H-%M-%S")}.png')
    #* show the plot
    plt.show()


# now let's make a function that looks at a href value and returns the domain name of the link for example "CNN" or "FOX News" we can add this to the function that gets the titles and then we can make a plot that shows the sentiment score of the titles from each news source on the drudge report page
def get_domain_name(url):
    """
    takes a url and returns the domain name of the url. This feeds into function nine.
    """
    #* get the domain name
    domain_name = tldextract.extract(url).domain
    #* return the domain name
    return domain_name



# example eight
def make_swarmplot_v2():
    """
    You are a python coder, make a swarmplot using Seaborn.

    The swarmplot shows the sentiment scores of all article titles on the drudge report page right now.
    The y axis is categorical and shows the domain name of the article (i.e. CNN, FOX News, etc.)
    The x axis is the sentiment score
    The position of the points in the swarm plot along the x-axis is set by the sentiment score of the title and the position along the y-axis is set by the domain name of the article.
    Finally, save the plot to a file called `drudge_report_sentiment_date.png` where date is the current date and time converted to string format suitable for a filename.
    """
    links = get_drudge_links()
    sentiment_scores, links = drudge_sentiment_mapping2()
    num_words = [len(i[0].split()) for i in sentiment_scores]
    sentiment = [i[1] for i in sentiment_scores]
    titles = [i[0] for i in sentiment_scores]


    df = pd.DataFrame({'domains': domains, 'sentiment': sentiment, 'titles': titles})

    sns.set_theme(style="whitegrid", palette="pastel", color_codes=True, font_scale=1.5, rc={"lines.linewidth": 2.5}, font='sans-serif')
    ax = sns.swarmplot(data=df, x="sentiment", y="domains", palette="muted", dodge=True, size=8)
    ax.set(xlabel="Sentiment Score")
    ax.set(ylabel="Domain Name")
    ax.set(title="Drudge Report Sentiment Analysis")
    plt.savefig(f'drudge_report_sentiment_{datetime.now().strftime("%Y-%m-%d-%H-%M-%S")}.png')





def main():
    # #* example one
    # print('example one')
    # print(get_drudge_links())
    # print()

    # #* example two
    # print('example two')
    # print(get_csv_column_types('data.csv'))
    # print()

    # #* example three
    # print('example three')
    # print(capitalize_list_of_strings(['hello', 'world']))
    # print()

    # #* example four
    # print('example four')
    # print(get_aapl_price())
    # print()

    # #* example five
    # print('example five')
    # print(request_page('https://www.google.com/'))
    # print()

    # #* example six
    # print('example six')
    # print(title_diviner('https://www.google.com/search?q=python+is+awesome&rlz=1C1CHBF_enUS927US927&oq=python+is+awesome&aqs=chrome..69i57j0l7.1178j0j7&sourceid=chrome&ie=UTF-8'))
    # print()

    # #* example seven
    # print('example seven')
    # print(get_drudge_titles())
    # print()

    # get the sentiment scores
    #sentiment_scores = drudge_sentiment_mapping()
    # plot the sentiment scores with a swarmplot
    make_swarmplot_v2()
    print("done")

if __name__ == '__main__':
    main()