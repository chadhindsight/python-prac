
from time import sleep
from scraping_project import scrape_quotes


# List that will store all quotes received 
all_quotes = []
base_url = "https://quotes.toscrape.com/"
url = "/page/1"

quotes = scrape_quotes()

