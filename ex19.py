import requests
from bs4 import BeautifulSoup

url = 'https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture'

r = requests.get(url)
soup = BeautifulSoup(r.content, 'lxml')

for i in soup.find_all('p'):
    print(i.text)
