# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 09:26:43 2016

@author: jdegene

https://impythonist.wordpress.com/2015/01/06/ultimate-guide-for-scraping-javascript-rendered-web-pages/

http://stackoverflow.com/questions/20039643/how-to-scrape-a-website-that-requires-login-first-with-python

http://www.analyticsvidhya.com/blog/2015/10/beginner-guide-web-scraping-beautiful-soup-python/

https://blog.hartleybrody.com/web-scraping/


https://github.com/downloads/davegb3/NppTidy2/Tidy2_0.2.zip
"""

import requests

import sys  
from PyQt4.QtGui import *  
from PyQt4.QtCore import *  
from PyQt4.QtWebKit import *  
from lxml import html 


class Render(QWebPage):  
  def __init__(self, url):  
    self.app = QApplication(sys.argv)  
    QWebPage.__init__(self)  
    self.loadFinished.connect(self._loadFinished)  
    self.mainFrame().load(QUrl(url))  
    self.app.exec_()  
  
  def _loadFinished(self, result):  
    self.frame = self.mainFrame()  
    self.app.quit() 


#url = 'http://www.kicker.de/news/fussball/bundesliga/spieltag/1-bundesliga/2015-16/spieltag.html'
url = 'http://manager.kicker.de/interactive/bundesliga/meinteam/ranking/'
#This does the magic.Loads everything
r = Render(url) 

#result is a QString.
result = r.frame.toHtml()



"""
#storing response
response = requests.get('http://www.kicker.de/')

#creating lxml tree from response body
tree = html.fromstring(response.text)

#Finding all anchor tags in response
print(tree.xpath('//div[@class="campaign"]/a/@href'))
"""