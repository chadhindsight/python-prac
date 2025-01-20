from random import randint
player_wins = 0
computer_wins = 0
win_score = 3

while player_wins < win_score and computer_wins < win_score:
	print(f"player Score: {player_wins} computer's score : {computer_wins}")

    # Computer choices
	player = input("Player, make your move: ").lower()
	if player == "q" or player == "quit":
		break
	rand_num = randint(0,2)
	if rand_num == 0:
		computer = "rock"
	elif rand_num == 1:
		computer = "paper"
	else:
		computer = "scissors"
	print(f"Computer plays {computer}" )
	#  Player choices 
	if player == computer:
		print("It's a tie!")
	elif player == "rock":
		if computer == "scissors":
			print("player wins!")
			player_wins += 1
		else:
			print("computer wins!")
			computer_wins += 1
	elif player == "paper":
		if computer == "rock":
			print("player wins!")
			player_wins += 1
		else:
			print("computer wins!")
			computer_wins += 1
	elif player == "scissors":
		if computer == "paper":
			print("player wins!")
			player_wins += 1
		else:
			print("computer wins!")	
			computer_wins += 1
	else:
		print("Please enter a valid move!")
