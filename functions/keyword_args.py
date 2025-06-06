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

# return the sum of all the arguments that are divisible by 2. If there are no numbers divisible by 2, return 0
def sum_even_values(*args):
    return sum(arg for arg in args if arg % 2 == 0)

# **KWARGS: gathers remaining arguments as a dictionary
def fav_colors(**kwargs):
	for person, color in kwargs.items():
		print(f"{person}'s favorite color is {color}")

fav_colors(colt="purple", ruby="red", ethel="teal")
fav_colors(colt="purple", ruby="red", ethel="teal", ted="blue")
fav_colors(colt="royal deep amazing purple")  

# NB: parameter ordering when mixing all this together: 1. params, 2. *args, 3. default params, 4. **kwargs

# Tuple unpacking:
def count_sevens(*args):
    return args.count(7)

nums = [90,1,35,67,89,20,3,1,2,3,4,5,6,9,34,46,57,68,79,12,23,34,55,1,90,54,34,76,89,18,9,12,34,14,15,16,17,11,7,11,8,4,6,2,5,8,7,10,12,13,14,15,7,8,7,7,345,23,34,45,56,67,1,7,3,6,7,2,3,4,5,6,7,8,9,8,7,6,5,4,2,1,2,3,4,5,6,7,8,9,0,9,8,7,8,7,6,5,4,3,2,1,7]

result2 = count_sevens(*nums)