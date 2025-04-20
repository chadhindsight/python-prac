# A regular named function
def square(num): return num * num

# An equivalent lambda, saved to a variable. NB: lambda's are similar to anonymous functions in JS
square2 = lambda num: num * num

# Another lambda
add = lambda a,b: a + b

# Write a lambda that accepts a single number and cubes it. Save it in a variable called cube.
cube = lambda num: num ** 3

# Executing the lambdas
print(square2(7))
print(add(3,10))
print(cube(4))

# Notice that the square function has a name, but the two lambdas do not
print(square.__name__)
print(square2.__name__)
print(add.__name__)