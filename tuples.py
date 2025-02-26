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
