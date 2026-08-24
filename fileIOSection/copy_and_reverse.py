# Write a function called copy_and_reverse, which takes in a file name and a new file name and copies the reversed contents of the first file to the second file.
def copy_and_reverse(name_of_file, new_file_name):
    with open(name_of_file) as file:
        text = file.read()
 
    with open(new_file_name, "w") as new_file:
        new_file.write(text[::-1])