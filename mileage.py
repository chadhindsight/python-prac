print("How many kilometers did you cycle today?")
# get user input
kms = input()

miles = round(float(kms) / 1.60934, 2)
print(f"Your {kms}km ride converted to miles would be {miles}mi")
