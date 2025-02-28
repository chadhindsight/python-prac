# NB: Tuples use () instead of []

# NB: Tuples are faster than Lists and are also immutable

# Example of looping in a Tuple
names = ('Koya', 'Dollie', 'Devin')

for name in names:
    print(name)

# Tuple Methods(count & index)
t = (12, 5, 9, 8, 12)
t.index(1) # returns the index at which a value is found in a tuple

t.count(12) # returns the number of times a value appears in a tuple

##### SETS #####
# Sets are a collection of data that do not have duplicate values, Elements in sets aren't ordered.
s = set({4,5,6})

# Another way of creating a set
vals = {'Bayley', 'Jordynne Grace', 'Io Sky'}

# Accessing all values in a set
for val in vals:
    print(val) 

# Set Methods
vals.add('Queen Aminata')
vals.remove('Jordynne Grace') # Will throw an error if the item is not in set
vals_copy = vals.copy() # Makes a copy of the set
vals.clear() # remove all items from the set

# 3 - Given the following variable:

values = [10,20,30]

# Create a variable called static_values which is the result of the values variable converted to a tuple
static_values = tuple(values)

# 4 - Given the following variable

stuff = [1,3,1,5,2,5,1,2,5]

# Create a variable called unique_stuff which is a set of only the unique values in the stuff list
unique_stuff = set(stuff)