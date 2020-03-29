import requests 
import sys
from bs4 import BeautifulSoup
from PyQt4.QtWebKit import QWebPage
from PyQt4.QtCore import QUrl
from PyQt4.QtGui import QApplication

class client(QWebPage):
    def __init__(self, url):
        self.app = QApplication(sys.argv)
        QWebPage.__init__(self)
        self.loadFinished.connect(self.on_page_load)
        self.mainFrame().load(QtUrl(url))
        self.app.exec_()
    
    def on_page_load(self):
        self.app_quit()
        
url = "https://in.tradingview.com/symbols/XETR-DAX/"
client_response = client(url)
source = client_response.mainFrame().toHtml()
soup = BeautifulSoup.(source,'lxml')
s = soup.find('div',class_="tv-symbol-price-quote__row js-last-price-block-value-row")
print(s.text)
