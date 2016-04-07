# -*- coding: utf-8 -*-

# reads a html file from kicker manager sites
# as the xml.etree solution throws errors due to encoding problems this replaces it

from bs4 import BeautifulSoup

Spieltag = 1

myFile = 'D:/Test/kicker/1BL_' + str(Spieltag) +'_721.txt'

htmlData = open(myFile,'r').read()

soup = BeautifulSoup(htmlData)

# Find the 'Ranking' table and move to child tbody
entry = soup.find(summary='Ranking').tbody

for tr_elem in entry("tr"):
    
    a_elem = tr_elem('a')
    for elem in a_elem:
        kickerURL = elem.get('href')
        kickerID = kickerURL[kickerURL.find('manid')+6 : kickerURL.find('/', kickerURL.find('manid')+6)]
        kickerName = elem.text
        #print(kickerURL, kickerID)
    
    td_elem = tr_elem('td', class_="alignright last")
    for elem in td_elem:
        kickerPoints = elem.text
        
        print(kickerID, kickerName,  kickerPoints)
        

