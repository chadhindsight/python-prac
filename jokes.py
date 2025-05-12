import requests
term = input("What would you like to search for? ")
url = "https://icanhazdadjoke.com/"

response = requests.get(
    url, 
    headers={"Accept": "application/json"},
    params={"term": term}).json()

print(response)
