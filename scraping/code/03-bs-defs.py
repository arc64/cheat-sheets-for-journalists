import requests

from bs4 import BeautifulSoup

# from string import ascii_lowercase
## http://stackoverflow.com/questions/4967103/beautifulsoup-and-lxml-html-what-to-prefer

def make_soup(url):
    page = requests.get(url)
    soupdata = BeautifulSoup(page.content)
    #soupdata = BeautifulSoup(page, "html.parser")
    return soupdata

soup  = make_soup('https://www.parliament.uk/mps-lords-and-offices/lords/deceased-lords/')

#print(soup.prettify())
table = soup.find(id="deceasedLords")
print(table)
