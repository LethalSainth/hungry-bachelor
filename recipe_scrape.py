# Import rquired libraries i.e request and Beautifulsoup

import requests
from bs4 import BeautifulSoup as bs

query = input('Search for food >> ')

search = query.split()

url = "https://www.allrecipes.com/search?q="+'+'.join(search)


response = requests.get(url)
# print(response)

html = response.content
# print(html)

soup = bs(html , "lxml")
# print(soup)

# Getting all food recipes.
recipes = soup.find_all("span", class_="card__title-text")
# print(recipes)

for rec in recipes:
    print(rec.get_text(strip=True))
