import requests
from bs4 import BeautifulSoup as bs

x = 'Facebook'
URL = 'https://twitter.com/'+x
page = requests.get(URL)
inputTag = soup.find(href="/"+x+"/followers")
output = inputTag['title']
print(output)
