from bs4 import BeautifulSoup
import requests

response = requests.get("https://quotes.toscrape.com/")

soup = BeautifulSoup(response.content, "html.parser")


print(soup.find_all(class_="zyte"))