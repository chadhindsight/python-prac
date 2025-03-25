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


# Use a loop to add together all the donations and store the resulting number in a variable called donations_total
donations_total = 0 

for val in donations.values():
    donations_total += val

print(donations_total)    

# Example of how to check if something is in a dictionary
"name" in user_info.keys() 
"Koya" in user_info.values()

# Dictionary methods
inventory = {'croissant': 19, 'bagel': 4, 'muffin': 8, 'cake': 1} #DON'T CHANGE THIS LINE!

# Make a copy of inventory and save it to a variable called stock_list USE A DICTIONARY METHOD
stock_list = inventory.copy()

# add the value 18 to stock_list under a new key called "cookie"
stock_list['cookie'] = 18


# remove 'cake' from stock_list (USE A DICTIONARY METHOD)
stock_list.pop('cake')

# Dictionary comprehension {__:__ for __ in __}
# Dictionary comprehension iterates through keys by default
list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]

answer = {list1[i]: list2[i] for i in range(len(list2))}

# NB: to iterate over keys and values, use .items()

# Conditional logic with dictionary comprehension
num_list = [2, 4, 6, 12]
{num: ("even" if num % 2 == 0 else "odd") for num in num_list}

# Create a dictionary with the key as a vowel in the alphabet and the value as 0. Your dictionary should look like this {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}.
answer = {char:0 for char in 'aeiou'}

# Create dictionary that maps ASCII keys to their corresponding letters.  Use a dictionary comprehension and chr()
answer =  {i: chr(i) for i in range(65,91)}