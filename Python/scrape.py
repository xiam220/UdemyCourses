import requests #allows us to download the HTML
from bs4 import BeautifulSoup

            #web browser without the actual window
response = requests.get('https://news.ycombinator.com/news')
# print(response.text)

# parse HTML; creates a soup object
soup = BeautifulSoup(response.text, 'html.parser')
# print(soup.body.contents)

# print(soup.find_all('div'))
# print(soup.title)

# find the first a
# print(soup.find('a'))

# print(soup.find(id='score_24954495'))

# uses CSS selectors
# . --> class
# print(soup.select('.score'))
# # --> id
# print(soup.select('#score_24954495'))

links = soup.select('.storylink')
votes = soup.select('.score')
# print(votes[0])

print(votes[0].get('id'))

