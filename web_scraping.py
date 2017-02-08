#!/usr/bin/env python

"""PYTHON 2 Web Scraping Tutorial
"""

#!/usr/bin/env python

#this first example uses Python2, urllib, urlopen
"""
from urllib import urlopen
from bs4 import BeautifulSoup
import re

html  = urlopen("http://www.menuism.com/restaurant-locations/dominos-pizza-7144") 
soup = BeautifulSoup(html) #Create instance of beautiful Soup
print soup.prettify().encode('utf-8')
"""

##########################################################################################
#this next example uses the requests module
"""
import requests
from bs4 import BeautifulSoup

html  = requests.get("http://www.menuism.com/restaurant-locations/dominos-pizza-7144") 
data = html.text   #Store the text from the url into object 'data'
soup  = BeautifulSoup(data) #Create instance of beautiful Soup
print soup.prettify().encode('utf-8') #prints all html
"""
##########################################################################################
#this one uses an html parser. 
"""
import requests
from bs4 import BeautifulSoup

html  = requests.get("http://www.menuism.com/restaurant-locations/dominos-pizza-7144") 
data = html.text   #Store the text from the url into object 'data'
soup = BeautifulSoup(data, "html.parser")
print soup.prettify().encode('utf-8') #prints all html
"""
##########################################################################################
"""NOTICE THAT URLOPEN (THE FIRST ONE IS MUCH PRETTIER THAN THE OTHERS. THIS IS BECAUSE
URLOPEN IS DIFFERENT THAN REQUESTS.
"""



