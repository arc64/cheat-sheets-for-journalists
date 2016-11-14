#dynamic page

#things happen in the broswer, happen in the server

import sys #system arguments
from QtPy.QtGui import QApplication # applications
from QtPy.QtCore import QUrl #url
from QtPy.QtWebKit import QWebPage #runs as browser

from bs4 import BeautifulSoup

urllib.request

## html5lib alt to urllib?

# sauce = urllib.request.urlopen('https//pythonprogramming.net').read()
# soup = BeautifulSoup.BeautifulSoup(sauce,'lxml')
# ## not a browser, so js not running
# js_test = soup.find('p', class_='jstest')


class Client(QWebPage):
    def __init__(self, url):
        self.app = QApplication(sys.argv)
        QWebPage.__init__(self)
        self.loadFinished.connect(self.on_page_load)
        self.mainFrame().load(Qurl(url))
        self.app.exec_()

    def on_page_load(self):
        self.app.quit()


## PyQT,
#self

url = 'https//pythonprogramming.net'
client_response = Client(url)
source = client_response
soup = BeautifulSoup.BeautifulSoup(sauce,'lxml')
js_test = soup.find('p', class_='jstest')
print(js_test.text)
