# Rock-Paper-Scissors-Exercise

This is a python application that allows you to play rock paper scissors with a computer. Good luck!

# Setup
Optionally fork or clone this [remote repository](https://github.com/sophiajoseph8/rock-paper-scissors-exercise) to create a copy under your own control. Then "clone" or download the remote repository(or your forked copy) onto your local computer, for example your Desktop. Then navigate to wherever you downloaded the repo using the Terminal:

```
cd ~/Desktop/rock-paper-scissors-exercise-py
```

Create a virtual environment:
```
conda create -n rps-env python=3.8
```

Activate the virtual environment:
```
conda activate rps-env
```
Install package dependencies within the virtual environment:
```
pip install -r requirements.txt
```
# Requirements
Once you have completed the setup described above, you can now start coding as noted below. To develop good version control habits, aim to make a separate commit after completeting each section.

## Processing User Inputs
The application should prompt the user to input (i.e., "rock", "paper", or "scissors") via command-line interface (CLI). It should store the user's selection in a variable for later reference (i.e., "player_choice")

## Validating User Inputs
The application should compare the user's selections against the list of valid options (i.e., "rock", "paper", "scissors") to determine whether the user has selected a valid option to play the game.

It should be able to handle various capitalizations and iterations of the valid options (e.g., "ROCK", "rock" or "Rock"). One way to do this would be standardize the input (e.g., put the input in lowercase).

If the selection is invalid, the program should display a friendly message to the user and prevent further program execution. The program should not try to further process an invalid input as it may lead to runtime errors.

## Simulating Computer Selection
The application should select one of the options for the game (i.e., "rock", "paper", "scissors") at random, and assign it as the computer's choice for the game.

## Determining the Winner
The application should compare the user's selection to the computer's selection, and determine which is the winner. The following logic should govern that determination:
1. Rock beats Scissors
2. Paper beats Rock
3. Scissors beats Paper
4. Rock vs Rock, Paper vs Paper, and Scissors vs Scissors each results in a "tie".

## Displaying the Results
After determing the winner, the application should display the results to the user. Outputs (from start to finish) should include at least the following:

+ A friendly welcome message including the player's name (by default, use "Player One").
+The user's selected option
+ The computer's selected option
+ Whether the user or the computer was the winner
+ A friendly farewell message


 Desired output may look like this:

 ```
 -------------------
Welcome 'Player One' to my Rock-Paper-Scissors game...
-------------------
Please choose either 'rock', 'paper', or 'scissors': rock
You chose: 'rock'
The computer chose: 'paper'
-------------------
Oh, the computer won. It's ok.
-------------------
Thanks for playing. Please play again!

```

# Game Play
Play rock paper scissors with the computer:

```
python game.py
```
