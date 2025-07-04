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
instructors.append("Jessica") 

# Remove the last value from a list
instructors.pop()
 
# Remove the first value from the list
instructors.pop(0)
 
# Add the string "Done" to the beginning of the list
instructors.insert(0, 'Done')

# Example of swapping values 
sounds[1], sounds[3] = sounds[3], sounds[1] 

#Example of List comprehension(basic syntax: [val for val in val])
numbers = [34, 50, 78, 100, 60]

doubleUp = [number * 2 for number in numbers]
quadUp = [number * 4 for number in numbers]
            
answer1 = [val for val in numbers if val in [3, 78, 50, 6, 12, 22]] 

#the slice [::-1] is a quick way to reverse a string
answer2 = [val[::-1].lower() for val in ["Elie", "Nicole", "Matt"]]

# create a variable called answer, which contains a list with all the numbers that are divisible by 12.
answer3 = [ num for num in range(1, 101) if (num % 12 == 0)]

# This remove all vowels from the word "amazing"
answer4 = [char for char in "amazing" if char not in "aeiouAEIOU"]
