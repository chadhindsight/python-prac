player_choice = input("Guess a number between 1 and 10: ")

# NB: randint is inclusive, not exclusive 
computer_choice = randint(1, 10)
keep_going = True

while(keep_going == True):
    if(player_choice == computer_choice):
        print("Wow, you and the machine are on the same wavelength")
        
    elif(player_choice > computer_choice):
        print("You guessed too high!")
    else:
        print("You guessed too low!")        