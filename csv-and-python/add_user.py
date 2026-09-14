from csv import writer;

# The "a" means append mode, lets us add things to the end of the file
def add_user(first, last):
    with open('users.csv', "a") as file:
        csv_writer = writer(file)
        csv_writer.writerow([first, last])