# Keyword arguments are named parameters passed to functions using key=value syntax, allowing default values and flexible argument order
def exponent(num, power=2):
	return num ** power

# Order doesn't matter anymore, if we use key word arguments:
print(exponent(num=2,power=3)) #8
print(exponent(power=3, num=2)) #8

# Without keywords args, order still matters:
print(exponent(3,4)) #81
print(exponent(4,3)) #64

total = 0

def increment():
	global total #use the global variable total
	total += 1
	return total

print(increment()) # 1
print(increment()) # 2
print(increment()) # 3

def single_letter_count(string,letter):
    return string.lower().count(letter.lower())

# Same, but for multiple letters
def multiple_letter_count(string):
    return {letter: string.count(letter) for letter in string}

# *ARGS: gathers remaining arguments as a tuple
def feed_me(*stuff):
	for thing in stuff:
		print(f"YUMMY I EAT {thing}")
feed_me("apple", "tire", "shoe", "salmon")


# **KWARGS: gathers remaining arguments as a dictionary
def fav_colors(**kwargs):
	for person, color in kwargs.items():
		print(f"{person}'s favorite color is {color}")

fav_colors(colt="purple", ruby="red", ethel="teal")
fav_colors(colt="purple", ruby="red", ethel="teal", ted="blue")
fav_colors(colt="royal deep amazing purple")  

# Tuple unpacking:
# NB: parameter ordering when mixing all this together: 1. params, 2. *args, 3. default params, 4. **kwargs