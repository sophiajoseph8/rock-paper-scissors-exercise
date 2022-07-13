# this is the "game.py" file...

print("Rock, Paper, Scissors, Shoot!")

print ("Welcome to the rock-paper-scissors game!")

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
arr = ["rock", "paper", "scissors"]
computer_choice = (random.choice(arr))
# standardize the input
computer_choice = computer_choice.lower()
print ("The computer chose:", (computer_choice))

# determine the winner and display the results.
if player_choice == "rock" and computer_choice == "rock":
    print ("Oh it's a tie!")
elif player_choice == "rock" and computer_choice == "paper":
    print ("Oh, the computer won. Maybe next time!")
elif player_choice == "rock" and computer_choice == "scissors":
    print ("Congratulations - you win!")
elif player_choice == "paper" and computer_choice == "paper":
    print ("Oh it's a tie!")
elif player_choice == "paper" and computer_choice == "rock":
    print ("Congratuations - you win!")
elif player_choice == "paper" and computer_choice == "scissors":
    print ("Oh, the computer won. Maybe next time!")
elif player_choice == "scissors" and computer_choice == "scissors":
    print ("Oh it's a tie!")
elif player_choice == "scissors" and computer_choice == "rock":
    print ("Oh, the computer won. Maybe next time!")
elif player_choice == "scissors" and computer_choice == "paper":
    print ("Congratulations - you win!")
else:
    print ("Sorry, please try again.")


# finish the game
print ("Thanks for playing. Please play again!")






