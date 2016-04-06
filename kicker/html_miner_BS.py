# -*- coding: utf-8 -*-

# reads a html file from kicker manager sites
# as the xml.etree solution throws errors due to encoding problems this replaces it

from bs4 import BeautifulSoup

Spieltag = 1

myFile = 'D:/Test/kicker/1BL_' + str(Spieltag) +'_241.txt'

htmlData = open(myFile,'r').read()

soup = BeautifulSoup(htmlData)

entry = soup.find(summary='Ranking')
