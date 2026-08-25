# prints out all of the first and last names in the users.csv file
import csv
 
def print_users():
    with open("users.csv") as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for row in csv_reader: 
            print(f"{row['First Name']} {row['Last Name']}")