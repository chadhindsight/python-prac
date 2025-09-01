# We can pass functions as args to other functions
def sum(n, func):
	total = 0
	for num in range(1,n+1):
		total += func(num)
	return total

def square(y):
	return y*y

def cube(x):
	return x*x*x


print(sum(4,cube))
print(sum(3,square))

