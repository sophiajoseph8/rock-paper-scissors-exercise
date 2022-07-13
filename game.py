# this is the "game.py" file...

print("Rock, Paper, Scissors, Shoot!")

print ("----------")
print ("Welcome to the rock-paper-scissors game!")
print ("----------")
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
print ("----------")

# determine the winner and display the results.
# rock options
if player_choice == "rock" and computer_choice == "rock":
    print ("Oh it's a tie!")
    print ("----------")
elif player_choice == "rock" and computer_choice == "paper":
    print ("Oh, the computer won. Maybe next time!")
    print ("----------")
elif player_choice == "rock" and computer_choice == "scissors":
    print ("Congratulations - you win!")
    print ("----------")
# paper
elif player_choice == "paper" and computer_choice == "paper":
    print ("Oh it's a tie!")
    print ("----------")
elif player_choice == "paper" and computer_choice == "rock":
    print ("Congratuations - you win!")
    print("----------")
elif player_choice == "paper" and computer_choice == "scissors":
    print ("Oh, the computer won. Maybe next time!")
    print ("----------")
# scissors options
elif player_choice == "scissors" and computer_choice == "scissors":
    print ("Oh it's a tie!")
    print ("----------")
elif player_choice == "scissors" and computer_choice == "rock":
    print ("Oh, the computer won. Maybe next time!")
    print("----------")
elif player_choice == "scissors" and computer_choice == "paper":
    print ("Congratulations - you win!")
    print ("----------")
else:
    print ("Sorry, please try again.")
    print ("----------")


# finish the game
print ("Thanks for playing. Please play again!")






