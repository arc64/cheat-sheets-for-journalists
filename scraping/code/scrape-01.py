import requests

from bs4 import BeautifulSoup

# from string import ascii_lowercase

def make_soup(url):
    page = requests.get(url)
    soupdata = BeautifulSoup(page.content)
    #soupdata = BeautifulSoup(page, "html.parser")
    return soupdata

soup  = make_soup('https://www.parliament.uk/mps-lords-and-offices/lords/deceased-lords/')
# link = soup.find(attrs=["class":"lsakj flkj flksfj "])
# print(link.get("href"))

print soup