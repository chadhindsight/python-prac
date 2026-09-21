import csv

# update_users : Takes in an old first name, an old last name, a new first name, and a new last name. Updates that  given row
def update_users(old_first, old_last, new_first, new_last):
    with open("users.csv") as csvfile:
        csv_reader = csv.reader(csvfile)
        rows = list(csv_reader)
    # var used to keep track of how many values were updated
    count = 0
    
    with open("users.csv", "w") as csvfile:
        csv_writer = csv.writer(csvfile)
 
        for row in rows:
            if row[0] == old_first and row[1] == old_last:
                csv_writer.writerow([new_first, new_last])
                count += 1
            else:
                csv_writer.writerow(row)
    return f"Users updated: {count}!"