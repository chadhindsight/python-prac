from csv import reader 

# Importing and reading data with the reader module
with open("fighters.csv") as file:
    csv_reader = reader(file)
    data = list(csv_reader)
    print(data)