# Rock-Paper-Scissors-Exercise

This is a python application that allows a human to play rock paper scissors with a computer. Good luck!

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
Once you have completed the setup described above, you can now start coding as noted below. To develop good version control habis, aim to make a separate commit after completeting each section.

## Processing User Inputs
The application should prompt the user to input (i.e., "rock", "paper", or "scissors") via command-line interface (CLI). It should store the user's selection in a variable for later reference (i.e., "player_choice")

## Validating User Inputs
The application should compare the user's selections agains the list of valid options (i.e., "rock", "paper", "scissors") to determine whether the user has selected a valid option to play the game.

# Usage
## Game Play
Play rock paper scissors with the computer:

```
python game.py
```
 
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

