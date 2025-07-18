from random import random

def flip_coin():
    if random() > 0.5:
        return "HEADS!"
    else:
        return "TAILS!"

# call the function
print(flip_coin())    



    