# -*- coding: utf-8 -*-

# reads a html file from kicker manager sites
# as the xml.etree solution throws errors due to encoding problems this replaces it

from bs4 import BeautifulSoup
import os, sqlite3

# Folder containing scrpaed html files
inFol = 'D:/Test/kicker/'

# define used season (starting year), used for naming within database
season = '2015'
league = '1'



### ###  DB creation  ### ### 

# connect to SQLite3 DB
conDB = sqlite3.connect('D:/Test/kicker_db/test1.sqlite')
# conncect cursor to DB
c = conDB.cursor()

# create table to store Manager ID (as primary key) and Manager Name as Text
c.execute('CREATE TABLE IF NOT EXISTS Manager(Manager_ID INTEGER PRIMARY KEY, Manager_Name TEXT)')


# create a table for the current season and league
pointTblName = 'BL'+league+"_"+season[2:]
c.execute('CREATE TABLE IF NOT EXISTS ' + pointTblName + ' (Manager_ID INTEGER PRIMARY KEY)')

# store the  points of each Manager for each day in a column, GD = GameDay
# try/except used for already exisiting columns, as these would throw an error
try:
    for colName in ['GD' + str(n) for n in range(1,35)]:
        c.execute('ALTER TABLE %s ADD COLUMN %s INTEGER' % (pointTblName, colName) )
except:
    pass
    


### ###  DB filling  ### ### 

for extFile in os.listdir(inFol):
    
    # skip file if not a txt file
    if extFile[-3:] != 'txt':
        continue

    #myFile = 'D:/Test/kicker/1BL_' + str(gameDay) +'_511.txt'  
    
    # extract number of GameDay, finds the number between both underscores
    gameDay =  extFile[extFile.find("_")+1:extFile.rfind("_")]
    
    myFile = inFol + extFile
    print(myFile)
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
            
            # write Manager IDs and Names in table, ignore if already exists
            c.execute('INSERT OR IGNORE INTO Manager VALUES (?,?)', (int(kickerID),kickerName))
            
            
            # write Manager's ID in pointTblName if not yet exists
            c.execute('INSERT OR IGNORE INTO ' + pointTblName + '(Manager_ID) VALUES (?)', (kickerID,))
            
            tblName = 'GD' + gameDay
            # write Manager's point of respective GameDay in pointTblName
            c.execute('INSERT OR IGNORE INTO ' + pointTblName + ' (' + tblName + ') VALUES (?)', (kickerPoints,))
  
      
conDB.commit()
conDB.close()