# Getting it into a file

import csv
import requests

from bs4 import BeautifulSoup

## html5lib alt to urllib?


#url = 'https://en.wikipedia.org/wiki/European_migrant_crisis'
url = 'https://www.parliament.uk/mps-lords-and-offices/lords/deceased-lords/'

def make_soup(url):
    page = requests.get(url)
    soupdata = BeautifulSoup(page.content, "lxml")
    return soupdata


soup  = make_soup(url)

# def extract_story(data):
#     d = {}
#     d['link'] = data[0].findChildren()[0]['href']
#     d['name'] = data[0].findChildren()[0].string
#     d['death'] = data[0].findChildren()[0].string

    # try:
    #     d['num_comments'] = int(s[1].findChildren()[2].string.split(" ")[0])
    # except ValueError:
    #     d['num_comments'] = 0

    # return d

#titles = soup.findAll('td','title')
#titles = soup.findAll('div', class_='body')

with open('output_file.csv', 'wb') as f:

    table = soup.find('table', {'id': 'deceasedLords'})

    for row in table.findAll("tr"):
        cells = row.findAll("td")
        print(cells)
        if len(cells) == 3:
            lord = cells[0].find(text=True)
            link = cells[0].a.get('href')
            party = cells[1].find(text=True)
            dod = cells[2].find(text=True)

            print(lord, link, dod)
            writer = csv.writer(f)
            writer.writerow( (lord, link, dod) )

f.close()

# .reverse()
# special file

#posters[story['poster']] = score + int(story['score'].split(" ")[0])


# subtexts = soup.findAll('td','subtext')
# stories = zip(titles,subtexts)

# print(titles)

# try:
#     writer = csv.writer(f)
#     writer.writerow( ('Title 1', 'Title 2', 'Title 3') )
#     for i in range(10):
#         writer.writerow( (i+1, chr(ord('a') + i), '08/%02d/07' % (i+1)) )
# finally:
#     f.close()

# print open(sys.argv[1], 'rt').read()


    #writer.writerow(headers)
    #writer.writerows(row for row in rows if row)
