from bs4 import BeautifulSoup
import requests
from random import choice
from time import sleep
# List that will store all quotes received 
all_quotes = []
base_url = "https://quotes.toscrape.com/"
url = "/page/1"

while url:
    response = requests.get(f"{base_url}{url}")
    soup = BeautifulSoup(response.text, "html.parser")
    quotes = soup.find_all(class_="quote")

    # NB: response.text gives HTML as a string (str) and .content gives HTML as raw bytes (bytes). Use this most of the time with the  BeautifulSoup module
    for quote in quotes:
        all_quotes.append({
            "text": quote.find(class_="text").text,
            "author": quote.find(class_="author").text,
            "bio_link":  quote.find("a") ["href"]
        })
    next_btn = soup.find(class_="next")
    url = next_btn.find("a")["href"] if next_btn else None
    
    # standard protocol to do some rough rate limiting
    sleep(2)
    print(all_quotes)

