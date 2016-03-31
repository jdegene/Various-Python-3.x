# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET

myFile = 'D:/Test/kicker/1BL_1_91.txt'
xmlPath = 'D:/Test/kicker/_TEST3.xml'


# first convert xml txt file from windows to utf8 encoding
# xml doesnt allow some characters and throws exceptoion otherwise
with open(myFile,encoding='Windows-1252') as f:
    data = f.read()
with open(myFile,'w',encoding='utf8') as f:
    f.write(data)

# then parse file into a tree
tree = ET.parse(myFile)