user_info = {
    "name": 'Koya',
    "age": 7,
    "is_cute": True
}

# Accessing values
artist = {
    "first": "Neil",
    "last": "Young",
}

full_name = f"{artist['first']} {artist['last']}"
print(full_name)

# DON'T TOUCH PLEASE!
donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0, lisa=50.25, harrison=10.0)
# DON'T TOUCH PLEASE!


# Use a loop to add together all the donations and store the resulting number in a variable called total_donations
total_donations = 0 

for val in donations.values():
    total_donations += val

print(total_donations)    

# Example of how to check if something is in a dictionary
"name" in user_info.keys() 
"Koya" in user_info.values()

# Dictionary methods
