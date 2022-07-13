# this is the "game.py" file...

print("Rock, Paper, Scissors, Shoot!")

print ("Welcome to the rock-paper-scissors game!")

# player's choice
player_choice = input("Please choose 'rock' paper' or 'scissors':")
print ("You chose:", (player_choice))

# validate user inputs
valid_options= {"rock_one": "Rock", "rock_two": "rock", "rock_three": "ROCK","paper_one": "Paper", "paper_two": "paper", "paper_three": "PAPER", "scissors_one":"Scissors", "scissors_two": "scissors", "scissors_three": "SCISSORS"}






# computer's choice

import random
random.random()
arr = ["rock", "paper", "scissors"]
computer_choice = (random.shuffle(arr))
print ("The computer chose:", random.choice(arr))

# determine the winner



print ("Thanks for playing! Please play again.")
# display the results




