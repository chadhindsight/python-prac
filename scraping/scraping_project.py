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
            'author': quote.find(class_="author").text,
            "bio_link":  quote.find("a") ["href"]
        })
    next_btn = soup.find(class_="next")
    url = next_btn.find("a")["href"] if next_btn else None
    
    # standard protocol to do some rough rate limiting
    # sleep(2)

quote = choice(all_quotes)
remaining_guesses = 4
print("Check out this quote: ")
print(quote["text"])
print(quote["author"])
guess = ""

while guess.lower() != quote["author"].lower() and remaining_guesses > 0:
    guess = input(f"Who said this quote? Guesses remaining: {remaining_guesses}\n")
    if guess.lower() == quote["author"].lower():
        print("You guessed correctly, congrats!")
        break
    remaining_guesses -= 1
    
    if remaining_guesses == 3:
      res = requests.get(f"{base_url}{quote['bio_link']}")
      soup = BeautifulSoup(res.text, "html.parser")
      birth_date = soup.find(class_="author-born-date").get_text()
      birth_place = soup.find(class_="author-born-location").get_text()
      print(f"Here's a hint: The author was born on {birth_date} {birth_place}")
    elif remaining_guesses == 2:
        print(f"Here's a hint: The author's first name starts with {quote['author'][0]}")
    elif remaining_guesses == 1:
        last_initial = quote['author'].split(" ")[1][0]
        print(f"Here's a hint: The author's last name starts with {last_initial}")
    else:
        print(f"Sorry, game over! The answer was {quote['author']}")
