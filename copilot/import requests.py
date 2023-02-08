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

# Function 1
def get_drudge_links():
    """
    This function parses the text on drudge report and returns a list of links to articles
    """
    # get the html of the drudge report
    drudge_html = requests.get('https://www.drudgereport.com/')
    # parse the html
    drudge_soup = soup(drudge_html.text, 'html.parser')
    # get the links
    drudge_links = drudge_soup.find_all('a')
    # get the links to articles
    drudge_article_links = [link['href'] for link in drudge_links if link['href'].startswith('https://')]
    return drudge_article_links

# Function 2
def csv_to_dataframe(csv_file):
    """
    This function uses pandas to automatically generate a dataframe with the columns cast to the type of the first row in a csv file passed to the function as an argument. The function should return the dataframe and the column names as a list of strings.
    """
    # read the csv file
    df = pd.read_csv(csv_file)
    # get the column names
    column_names = list(df.columns)
    return df, column_names