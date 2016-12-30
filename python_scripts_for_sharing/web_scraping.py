import requests
from bs4 import BeautifulSoup
import re

html  = requests.get("http://menuism.com") 
data = html.text   #Store the text from the url into object 'data'
soup = BeautifulSoup(data, "html.parser") #Create instance of beautiful Soup
print soup.prettify()