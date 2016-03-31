
#http://stackoverflow.com/questions/20039643/how-to-scrape-a-website-that-requires-login-first-with-python

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.common.by import By

#from selenium.webdriver.support.ui import Select
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.common.exceptions import TimeoutException
#from selenium.webdriver.support import expected_conditions as EC
#from selenium.common.exceptions import NoSuchElementException
#from selenium.common.exceptions import NoAlertPresentException

url = "http://www.kicker.de/games/interactive/startseite/gamesstartseite.html"

uName = "Edwor1987@fleckens.hu"
uPass = "123456!"

#driver = webdriver.Firefox()
driver = webdriver.Chrome()

driver.get(url)

# Get the Username and Password fields by their ID
login_name_form = driver.find_element_by_id('nicknameLoginBox')
login_pw_form = driver.find_element_by_id('passwordLoginBox')
# Get the LOS Button by its name
LOS_Button = driver.find_element_by_name('Submit')

# Fill in Username and Password and confirm with Enter
login_name_form.send_keys(uName)
login_pw_form.send_keys(uPass)
LOS_Button.send_keys(Keys.ENTER)


#driver.close()