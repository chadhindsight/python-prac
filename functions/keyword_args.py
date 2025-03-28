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