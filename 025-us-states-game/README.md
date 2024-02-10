# U.S. States Guessing Game

## Overview
Welcome to the U.S. States Guessing Game! This simple Python program utilizes the turtle graphics library and pandas to create an interactive game where players can guess the names of various U.S. states.

## Features
- Utilizes turtle graphics for an interactive and visually appealing experience.
- Displays a map of the United States with states labeled as players guess their names.
- Keeps track of correct guesses out of 50.
- Allows players to exit the game and saves the list of states yet to be guessed in a CSV file (`states_to_learn.csv`).

## How to Play
1. Run the Python script in your preferred environment.
2. A window will appear displaying a map of the United States with some states labeled.
3. Input the name of a U.S. state when prompted.
4. If the guessed state is correct, it will be labeled on the map.
5. Repeat steps 3-4 until all 50 states are correctly identified or choose "Exit" to save progress and exit the game.

## Setup
1. Download the repository containing the script and the required data file.
2. Ensure you have Python, turtle, and pandas installed on your system.
3. Run the script in your preferred Python environment.

## Data
The game uses a CSV file named `50_states.csv` containing information about each U.S. state. The file includes columns for state names, x and y coordinates for turtle graphics, and additional data.

## Saving Progress
If you decide to exit the game before guessing all 50 states, the program will save the list of remaining states to a file named `states_to_learn.csv`. You can use this file to continue your progress in future sessions.
