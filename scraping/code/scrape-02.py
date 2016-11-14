bs4 as bs4
urllib.request

## html5lib alt to urllib?

sauce = urllib.request.urlopen('https//pythonprogramming.net').read()

soup = bs.BeautifulSoup(sauce,'lxml')

# print(sauce)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.title.text)
# print(soup.p)
# print(find_all('p'))

#
## could use regular expressions
# for p in soup.find_all('p'):
#     print(p)
#     print(p.string)
    # string navigatable string (don't have child tags, else None) vs text which returns unicode.

#
# print(soup.get_text())
#     # probably better if you can't rely on the tags

#
# for url in soup.find_all('a')
#     print url.get('href')

#
# nav = soup.nav
# for url in nav.find_all('a'):
#     print(url.get('href'))

# body = soup.body
# for paragraph in body.find_all('p')
#     print(paragraph.text)

# for div in soup.find_all('div', class_='body'):
#         print(div.text)



