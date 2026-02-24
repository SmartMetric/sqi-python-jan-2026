import requests
from bs4 import BeautifulSoup
url = "https://quotes.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text,"html.parser")
quote_divs = soup.select("div.quote")
print(len(quote_divs))
authors = soup.select("div.quote small.author")
print(authors)
author_names = authors.text
print(author_names)



