# -*- coding: utf-8 -*-

# handles the website rendering. Handy when the website is rendered using JavaScript
# This script returns a html Version of the Website
# All credits go to:
# https://impythonist.wordpress.com/2015/01/06/ultimate-guide-for-scraping-javascript-rendered-web-pages/
#
# Changed to subprocess: If run within one application MULTIPLE times -> kernel crashes
 

import sys

from PyQt4.QtGui import *  
from PyQt4.QtCore import *  
from PyQt4.QtWebKit import *  



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


url = sys.argv[1]

#This does the magic.Loads everything
r = Render(url) 

#result is a QString.
result = r.frame.toHtml()


print(result)


