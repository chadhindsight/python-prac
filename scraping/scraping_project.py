from bs4 import BeautifulSoup
import requests

response = requests.get("https://quotes.toscrape.com/")

soup = BeautifulSoup(response.text, "html.parser")


print(soup.find_all(class_="zyte"))
# NB: response.text gives HTML as a string (str) and .content gives HTML as raw bytes (bytes). Use this most of the time with the  BeautifulSoup module.