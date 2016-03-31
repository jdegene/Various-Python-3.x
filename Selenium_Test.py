
#http://stackoverflow.com/questions/20039643/how-to-scrape-a-website-that-requires-login-first-with-python

#from bs4 import BeautifulSoup

import os, shutil

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.common.by import By

#from selenium.webdriver.support.ui import Select
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.common.exceptions import TimeoutException
#from selenium.webdriver.support import expected_conditions as EC
#from selenium.common.exceptions import NoSuchElementException
#from selenium.common.exceptions import NoAlertPresentException

loginURL = "http://www.kicker.de/games/interactive/startseite/gamesstartseite.html"

# Username and PW read from separate file (first and second line)
uName = open('D:\Python\Info.txt', "r").readlines()[0].rstrip('\n')
uPass = open('D:\Python\Info.txt', "r").readlines()[1].rstrip('\n')

#driver = webdriver.Firefox()
driver = webdriver.Chrome()

driver.get(loginURL)

# Get the Username and Password fields by their ID
login_name_form = driver.find_element_by_id('nicknameLoginBox')
login_pw_form = driver.find_element_by_id('passwordLoginBox')
# Get the LOS Button by its name
LOS_Button = driver.find_element_by_name('Submit')

# Fill in Username and Password and confirm with Enter
login_name_form.send_keys(uName)
login_pw_form.send_keys(uPass)
LOS_Button.send_keys(Keys.ENTER)

# 1. Bundesliga
for Spieltag in range(1,28):
    for counter in range(1,200000,30):
    
        try:        
            BLrankURL = "http://manager.kicker.de/interactive/bundesliga/meinteam/ranking/suchelfdnr/" \
            + str(counter) + "/rankinglist/0/spieltag/" + str(Spieltag)
            
            # open URL that contains ranking points BL1
            driver.get(BLrankURL)        
            
            BLrankHTLM = driver.page_source
            
            # As long as "Keine Daten vorhanden" is absent, it continues
            # if it appears, no more data is available, exception is raised and loop left
            assert "Keine Daten vorhanden" not in BLrankHTLM        
        
            txtFile = 'D:/Test/kicker/1BL_' + str(Spieltag) + "_" + str(counter) + '.txt'
            w = open(txtFile, 'w')
            w.write(BLrankHTLM)
            w.close()
            
        except:
            break


  
# 2. Bundesliga      
for Spieltag in range(1,28):
    for counter in range(1,200000,30):
    
        try:        
            BLrankURL = "http://manager.kicker.de/interactive/2bundesliga/meinteam/ranking/suchelfdnr/" \
            + str(counter) + "/rankinglist/0/spieltag/" + str(Spieltag)
            
            # open URL that contains ranking points BL1
            driver.get(BLrankURL)        
            
            BLrankHTLM = driver.page_source
            
            # As long as "Keine Daten vorhanden" is absent, it continues
            # if it appears, no more data is available, exception is raised and loop left
            assert "Keine Daten vorhanden" not in BLrankHTLM        
        
            txtFile = 'D:/Test/kicker/2BL_' + str(Spieltag) + "_" + str(counter) + '.txt'
            w = open(txtFile, 'w')
            w.write(BLrankHTLM)
            w.close()
            
        except:
            break   


driver.close()

for files in os.listdir('D:/Test/kicker/'):
    shutil.copyfile('D:/Test/kicker/'+ files, 'P:/Kicker/' + files)
    