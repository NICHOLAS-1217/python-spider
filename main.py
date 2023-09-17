import requests
from bs4 import BeautifulSoup

#making get request
r = requests.get('https://www.geeksforgeeks.org/python-programming-language/')

#show reponse
print(r)

soup = BeautifulSoup(r.content, 'html.parser')
#show html
print(soup.prettify())
#show title tag
print(soup.title)
#show tag name
print(soup.title.name)
#show tag parent name
print(soup.title.parent.name)
