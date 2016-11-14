
## how to import
## parsing XML and HTML documents
from lxml import html

## web page with our data
import requests

#thePage = requests.get('https://en.wikipedia.org/wiki/European_migrant_crisis')
thePage = requests.get('https://www.parliament.uk/mps-lords-and-offices/lords/deceased-lords/')

tree = html.fromstring(thePage.content)

# r.headers['content-type']
# r.encoding
# r.text
# r.json()

# print(r.headers['content-type'])
# print(r.text)

## https://www.parliament.uk/mps-lords-and-offices/lords/deceased-lords/

## http://www.w3schools.com/xml/xpath_syntax.asp

#theDead = tree.xpath('//*[@id="deceasedLords"]/tbody/tr[1]/td[1]/a/text()')

theDead = tree.xpath('//*[@id="deceasedLords"]/tbody/tr/td[1]/a/text()')

print(theDead)


# http://stackoverflow.com/questions/419163/what-does-if-name-main-do