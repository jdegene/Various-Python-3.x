# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 09:26:43 2016

@author: jdegene

https://impythonist.wordpress.com/2015/01/06/ultimate-guide-for-scraping-javascript-rendered-web-pages/
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


url = 'http://www.kicker.de/news/fussball/bundesliga/spieltag/1-bundesliga/2015-16/spieltag.html'

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