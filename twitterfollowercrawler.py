import requests
from bs4 import BeautifulSoup as bs

x = '<input the required account name wherever case sensitive>'
URL = 'https://twitter.com/'+x
page = requests.get(URL)
inputTag = soup.find(href="/"+x+"/followers")
output = inputTag['title']

print(output)#To get uformatted output

#uncomment the lines below to obtain only numerical output
#followers=''.join(i for i in output if i.isdigit())
#print(followers)
