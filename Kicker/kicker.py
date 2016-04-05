# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 09:26:43 2016

@author: jdegene


http://stackoverflow.com/questions/20039643/how-to-scrape-a-website-that-requires-login-first-with-python

http://www.analyticsvidhya.com/blog/2015/10/beginner-guide-web-scraping-beautiful-soup-python/

https://blog.hartleybrody.com/web-scraping/


https://github.com/downloads/davegb3/NppTidy2/Tidy2_0.2.zip
"""

import requests, datetime, subprocess
import sys  
from lxml import html 


# Define the Python exe path and the script for the subprocess
python_path = "C:/Anaconda3/Pythonw.exe"
python_script = "D:/Python/Git/Various-Python-3.x/kicker_child.py"


url = 'http://manager.kicker.de/interactive/bundesliga/meinteam/ranking/suchelfdnr/31/rankinglist/0/spieltag/27'

# run the actual subprocess
p = subprocess.check_output([python_path, python_script, url])

# Return from subprocess is in bytecode, must be converted first. 'windows-1252' is obviously
# for windows systems, try UTF-8 if not working (or OS related)
q = p.decode('windows-1252')


# Write result to a file with timestamp in name (for testing purposes)
nowTime = str(datetime.datetime.now().time().hour) + "_" + str(datetime.datetime.now().time().minute)
txtFile = 'D:/Test/kicker/rndrd_' + nowTime + '.txt'
w = open(txtFile, 'w')
w.write(q)
w.close()




"""
#storing response
response = requests.get('http://www.kicker.de/')

#creating lxml tree from response body
tree = html.fromstring(response.text)

#Finding all anchor tags in response
print(tree.xpath('//div[@class="campaign"]/a/@href'))
"""