# Write a function called copy, which takes in a file name and a new file name and copies the contents of the first file to the second file. 
def copy(file_name, new_file_name):
    with open(file_name) as file:
        text = file.read()
    
    with open(new_file_name, "w") as new_file: 
        new_file.write(text) 