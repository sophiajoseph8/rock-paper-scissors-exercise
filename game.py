# this is the "game.py" file...

print("Rock, Paper, Scissors, Shoot!")

print ("-" * 20)
print ("Welcome 'Player One' to the rock-paper-scissors game!")
print ("-"*20)

# player's choice
player_choice = input("Please choose 'rock' paper' or 'scissors':")

# standardize the input
player_choice = player_choice.lower()
print ("You chose:", (player_choice))

# valid options for the game
valid_options = ["rock", "paper", "scissors"]

# if not in the list, terminate the game
if player_choice not in valid_options:
    print ("Oops - invalid selection. Please try again.")
    exit()

# computer's choice

import random
random.random()
computer_choice = (random.choice(valid_options))
# standardize the input
computer_choice = computer_choice.lower()
print ("The computer chose:", (computer_choice))
print ("-"*20)

# determine the winner and display the results.
# rock options
if player_choice == "rock" and computer_choice == "rock":
    print ("Oh it's a tie!")
    print ("-"*20)
elif player_choice == "rock" and computer_choice == "paper":
    print ("Oh, the computer won. Maybe next time!")
    print ("-"*20)
elif player_choice == "rock" and computer_choice == "scissors":
    print ("Congratulations - you win!")
    print ("-"*20)
# paper
elif player_choice == "paper" and computer_choice == "paper":
    print ("Oh it's a tie!")
    print ("-"*20)
elif player_choice == "paper" and computer_choice == "rock":
    print ("Congratuations - you win!")
    print("-"*20)
elif player_choice == "paper" and computer_choice == "scissors":
    print ("Oh, the computer won. Maybe next time!")
    print ("-"*20)
# scissors options
elif player_choice == "scissors" and computer_choice == "scissors":
    print ("Oh it's a tie!")
    print ("-"*20)
elif player_choice == "scissors" and computer_choice == "rock":
    print ("Oh, the computer won. Maybe next time!")
    print("-"*20)
elif player_choice == "scissors" and computer_choice == "paper":
    print ("Congratulations - you win!")
    print ("-"*20)
else:
    print ("Sorry, please try again.")
    print ("-"*20)


# finish the game
print ("Thanks for playing. Please play again!")






