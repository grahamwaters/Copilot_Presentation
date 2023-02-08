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

# because we will be dealing with stock data it might be useful to import yfinance
import yfinance as yf

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
# 6 - Create a grid plot of the sentiment scores of all article titles on the drudge report page right now. where the color of the square is the sentiment score, the position has no meaning, and the size of the square is the number of words in the title. The function should return the plot and save it to a file called drudge_report_sentiment_date.png where date is the current date and time converted to string format suitable for a filename.


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

# example five
def drudge_sentiment_mapping():
    #* get the links
    links = get_drudge_links()
    #* initialize a list to hold the titles
    titles = []
    #* loop over the links
    for link in links:
        #* get the html
        r = requests.get(link)
        #* parse the html
        page_soup = soup(r.text, 'html.parser')
        #* get the title
        title = page_soup.title.text
        #* add the title to the list
        titles.append(title)
    #* initialize a list to hold the sentiment scores
    sentiment_scores = []
    #* loop over the titles
    for title in titles:
        #* get the sentiment score
        sentiment_score = TextBlob(title).sentiment.polarity
        #* add the sentiment score to the list
        sentiment_scores.append(sentiment_score)
    #* zip the titles and the sentiment scores together
    zipped = zip(titles, sentiment_scores)
    #* return the zipped list
    return list(zipped)




if __name__ == '__main__':
    # example one
    print(get_drudge_links())
    # example two
    df, column_names, column_types = get_csv_column_types('./example_repo/data/feb1/2d_Agg_AS_Offers_OFFNS-01-FEB-23.csv')
    print(column_names)
    print(column_types)
    # example three
    print(capitalize_list_of_strings(['hello', 'world']))
    # example four
    print(get_aapl_price())
    # example five
    print(get_aapl_price_with_date('2019-03-26'))
    # example six
    print(get_aapl_price_with_date_and_symbol('2019-03-26', 'AAPL'))
