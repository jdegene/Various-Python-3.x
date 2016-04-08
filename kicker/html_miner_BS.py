# -*- coding: utf-8 -*-

# reads a html file from kicker manager sites
# as the xml.etree solution throws errors due to encoding problems this replaces it

from bs4 import BeautifulSoup
import sqlite3

#DB creation

# connect to SQLite3 DB
conDB = sqlite3.connect('D:/Test/kicker_db/test1.db')

# conncect cursor to DB
c = conDB.cursor()

# create table to store Manager ID (as primary key) and Manager Name as Text
c.executescript("""CREATE TABLE Manager(Manager_ID INTEGER PRIMARY KEY, Manager_Name TEXT);""")



# DB filling
gameDay = 10

myFile = 'D:/Test/kicker3/1BL_' + str(gameDay) +'_511.txt'

htmlData = open(myFile,'r').read()

# Define Parent element, use lxml parser
soup = BeautifulSoup(htmlData, "lxml")

# Find the 'Ranking' table and move to child tbody
entry = soup.find(summary='Ranking').tbody

# iterate over all <tr> elements
for tr_elem in entry("tr"):
    
    # find 'a' elements = links
    a_elem = tr_elem('a')
    
    # iterate over the sub-elements and extract tag link and text
    for elem in a_elem:
        kickerURL = elem.get('href')
        # extract the UserID from the URL
        kickerID = kickerURL[kickerURL.find('manid')+6 : kickerURL.find('/', kickerURL.find('manid')+6)]
        kickerName = elem.text

    # find the points gained on every gameDay in the 'td' tag with attribute 'alignright last'
    td_elem = tr_elem('td', class_="alignright last")
    for elem in td_elem:
        kickerPoints = elem.text
        
        print(kickerID, kickerName,  kickerPoints)
        
