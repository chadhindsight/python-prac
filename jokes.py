import requests
term = input("What would you like to search for? ")
url = "https://icanhazdadjoke.com/"

response = requests.get(url)

print(response.text)
