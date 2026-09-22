# Beautiful Soup lets us navigate through HTML with Python
from bs import BeautifulSoup

soup = BeautifulSoup(html, "html.parser")
print(soup.body.div)