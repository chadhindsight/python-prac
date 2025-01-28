sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]

result = ""

for sound in sounds:
    result += sound.upper()





# Changing/Manipulating vals in lists
# Create a list called instructors
instructors = []
 
# Add the following strings to the instructors list 
    # "Colt"
    # "Blue"
    # "Lisa"
instructors.extend(["Colt", "Blue", "Lisa"])
 
# Remove the last value in the list
instructors.pop()
 
# Remove the first value in the list
instructors.pop(0)
 
# Add the string "Done" to the beginning of the list
instructors.insert(0, 'Done')

# Example of swapping values 
# sounds[1], sounds[3] = sounds[3], sounds[1] 

#Example of List comprehension
numbers = [34, 50, 78, 100, 60]

doubleUp = [number * 2 for number in numbers]