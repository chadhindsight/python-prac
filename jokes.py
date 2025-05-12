import requests
user_input = input("What would you like to search for? ")
url = "https://icanhazdadjoke.com/"

response = requests.get(
    url, 
    headers={"Accept": "application/json"},
    params={"term": user_input}).json()

print(response)

num_jokes = response["total_jokes"]
if num_jokes > 1:
    print("We got mad jokes!")
elif num_jokes:
    print("There is one joke only")
else:
    print(f"Sorry, could not find a joke with the term {user_input}")    