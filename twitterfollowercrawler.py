import requests
from bs4 import BeautifulSoup as bs
x = 'Facebook'#
URL = 'https://twitter.com/'+x
page = requests.get(URL)
inputTag = soup.find(href="/"+x+"/followers")
output = inputTag['title']
print(output)#To get uformatted output

#
#followers=''.join(i for i in output if i.isdigit())
#print(followers)
