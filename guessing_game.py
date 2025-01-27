from random import randint

player_choice = int(input("Guess a number between 1 and 10: "))
computer_choice = randint(1, 10)
keep_going = True

while(keep_going):
    if(player_choice == computer_choice):
        print("Wow, you and the machine are on the same wavelength")
    elif(player_choice > computer_choice):
        print("You guessed too high!")
    else:
        print("You guessed too low!")
        
    cont = input("Keep going? y or n: ")
    if cont.lower() != 'n' or cont.lower() != 'no':
        keep_going = False
    else:
        player_choice = int(input("Guess a number between 1 and 10: "))
        computer_choice = randint(1, 10) 
 