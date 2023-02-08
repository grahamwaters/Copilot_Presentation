# imports
import requests, pandas as pd
from bs4 import BeautifulSoup as soup
import re
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime
from ratelimit import limits, sleep_and_retry
from textblob import TextBlob
# import Counter
from collections import Counter
import tldextract
# import Vader Sentiment Analyzer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
# import tqdm
from tqdm import tqdm
# import nltk
import nltk
#& Helper Functions
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

def get_domain_name(url):
    """
    takes a url and returns the domain name of the url. This feeds into function nine.
    """
    #* get the domain name
    domain_name = tldextract.extract(url).domain
    #* return the domain name
    return domain_name


# Step 1 - get the links and the titles from those links as well as their sentiment scores
def scrape_drudge():
    #* get the html from drudge report
    r = requests.get('http://www.drudgereport.com/')
    #* parse the html
    page_soup = soup(r.text, 'html.parser')
    #* get the links
    links = page_soup.findAll('a')
    #* initialize a list to hold the links
    link_list = []
    title_list = []
    sentiment_scores = []
    domains = []
    #* loop over the links and add them to the list
    for link in links:
        link_list.append(link['href'])
        title_text = title_diviner(link['href'])
        title_list.append(title_text)
        sentiment_score = TextBlob(title_text).sentiment.polarity
        sentiment_scores.append(sentiment_score)
        domains.append(get_domain_name(link['href']))
    #* return the list
    return link_list, title_list, sentiment_score, domains

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
    # part 1 - get the links and the titles from those links as well as their sentiment scores, and the domains
    link_list, title_list, sentiment_score, domains = scrape_drudge()
    # part 2 - get the top 5 domains
    top_five_domains = Counter(domains).most_common(5)
    # part 6 - Get the top 5 domains and their sentiment scores
    top_five_domains_sentiment = []
    for domain in top_five_domains:
        try:
            #* get the domain name
            domain_name = domain[0]
            #* get the sentiment scores for the domain's titles in drudge_titles
            domain_sentiment = [sentiment_score[i] for i, domain in enumerate(domains) if domain == domain_name]
            #* get the average sentiment score
            domain_sentiment_average = sum(domain_sentiment) / len(domain_sentiment)
            #* add the domain name and the average sentiment score to the list
            top_five_domains_sentiment.append((domain_name, domain_sentiment_average))
        except Exception as e:
            print(e)
    # part 7 - Make a swarmplot of these five domains using their sentiment scores with individual points representing titles, y-axis representing the domain name and x-axis representing the sentiment score.
    #* create a dataframe
    df = pd.DataFrame(top_five_domains_sentiment, columns=['domain', 'sentiment_score'])
    #* make the swarm plot
    swarm_plot(df, 'sentiment_score', 'domain', None, 'Top 5 Domains and Sentiment Scores', 'Sentiment Score', 'Domain', 'top_five_domains_sentiment.png')


if __name__ == '__main__':
    main()