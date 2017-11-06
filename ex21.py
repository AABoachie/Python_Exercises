import requests
from bs4 import BeautifulSoup

filename = input("Filename?: ")

file = open(filename, 'w')

url = 'https://www.nytimes.com'

r = requests.get(url)

soup = BeautifulSoup(r.content, 'html.parser')

h2 = soup.find_all('h2', {'class' : 'story-heading'})

content = 0

for i in h2:
    file.write(str(content) + " " + i.text.strip() + "\n")
    content += 1
    
file.close()
