from knowledgebase import * # import all the libraries into memory

# 1. Parsing Drudge Report
## Write a function that parses the text on Drudge Report and returns a list of links to articles
def drudge_scrape():
    # get the html from the drudge report
    response = requests.get('http://drudgereport.com')
    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    # get the list of links
    links = soup.find_all('a')
    # filter for only the links that have http in them
    links = [link for link in links if 'http' in link.get('href')]
    # return the list of links
    return links