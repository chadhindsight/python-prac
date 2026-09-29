from bs4 import BeautifulSoup
import requests

# List that will store all quotes received 
all_quotes = []

response = requests.get("https://quotes.toscrape.com/")
soup = BeautifulSoup(response.text, "html.parser")


quotes = soup.find_all(class_="quote")
# NB: response.text gives HTML as a string (str) and .content gives HTML as raw bytes (bytes). Use this most of the time with the  BeautifulSoup module.

for quote in quotes:
    all_quotes.append({
        "text": quote.find(class_="text").text,
        "author": quote.find(class_="author").text,
        "bio_link":  quote.find("a") ["href"]
    })

print(all_quotes[0])