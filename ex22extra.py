import requests
from bs4 import BeautifulSoup

url = 'http://www.practicepython.org/assets/Training_01.txt'

tally = {}

r = requests.get(url)

soup = BeautifulSoup(r.content, 'lxml')

items = soup.find_all('p')[0].text.split()

for i in items:
    key = i.split("/")[2]
    if key in tally:
        tally[key] += 1
    else:
        tally[key] = 1
        

for i in tally:
    print(i, tally[i])
