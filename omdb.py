# -*- coding: utf-8 -*-

# Small project to analyize movies and series data from http://www.omdbapi.com/
# uses the folowing wrapper: https://pypi.python.org/pypi/omdb/0.2.0 

import omdb
import wikipedia
from bs4 import BeautifulSoup

# load raw wiki pages for US and GB TV series
wikiUS_text = wikipedia.page(title="List_of_American_television_series", auto_suggest=True, redirect=True, preload=False).content
wikiGB_html = wikipedia.page(title="List_of_British_television_programmes", auto_suggest=True, redirect=True, preload=False).html()


# Create ==US== List of pure series name strings
# split US list into single entries by \n separator. Exclude everything before first "\n\n\n" (intro text)
wikiUSlist = wikiUS_text[wikiUS_text.find("\n\n\n")+3:wikiUS_text.find("See also")].split("\n")
wikiUSlist = list(filter(None, wikiUSlist)) # remove empty strings

# remove subsection headings and years/genres from series names
for i in wikiUSlist:
    if i[:2] == '==':
        wikiUSlist.remove(i)
    elif '(' in i:
        wikiUSlist.remove(i)
        wikiUSlist.append( i[ : i.find('(')-1] )
        


# Create ==UK== List of pure series name strings, still contains 'Other Languages' series
soup = BeautifulSoup(wikiGB_html, "lxml")
entry = soup.find_all('i')
wikiGBlist = [x.get_text() for x in entry if x.get_text() != 'citation needed']
