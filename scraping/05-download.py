import os
import urllib
import urllib2
from bs4 import BeautifulSoup

url = "http://icecat.biz/p/toshiba/pscbxe-01t00een/satellite-pro-notebooks-4051528049077-Satellite+Pro+C8501GR-17732197.html"
html = urllib2.urlopen(url)
soup = BeautifulSoup(html)

imgs = soup.findAll("div", {"class":"thumb-pic"})
for img in imgs:
        imgUrl = img.a['href'].split("imgurl=")[1]
        urllib.urlretrieve(imgUrl, os.path.basename(imgUrl))