from csv import reader 
from csv import DictReader

# Example of importing and reading data with the reader module 
with open("fighters.csv") as file:
    csv_reader = reader(file)
    # NB: data is cast into a list because the csv.reader() function returns an iterable, 
    # and wrapping it with list() allows you to access all the rows at once
    # NB: keys are automatically set to be the headers from the given CSV file
    data = list(csv_reader)
    print(data)

# Reading/Parsing CSV Using a DictReader. jay white
with open("fighters.csv") as file:
    csv_reader = DictReader(file)
    for row in csv_reader:
        # Each row is an OrderedDict!
        print(row['Name'])