# Turtle Crosser Game

## Introduction
Welcome to Turtle Crosser, a Python-based game that challenges your reflexes and strategic thinking. In this game, you control a turtle trying to cross a busy road while avoiding oncoming traffic. The game features randomly moving cars, score tracking, and increasing difficulty levels.

## Files

### 1. main.py
- `main.py` serves as the main script orchestrating the Turtle Crosser game.
- The script initializes the game window using the Turtle graphics library, creates instances of the Player, CarManager, and Scoreboard classes, and handles user input.
- The game loop continuously updates the screen, generates cars, moves them, and detects collisions with the player.
- It includes features for increasing difficulty levels and displaying a game over message.

### 2. scoreboard.py
- `scoreboard.py` defines the `Scoreboard` class, responsible for tracking and displaying the player's level.
- The class inherits from the Turtle class to utilize Turtle graphics for presenting the player's progress.
- Methods such as `update_scoreboard`, `increase_level`, and `game_over` manage the display of the level and game over messages.

### 3. player.py
- `player.py` contains the `Player` class, representing the turtle player in the Turtle Crosser game.
- The turtle is initialized at the bottom of the screen and can be moved north using the "Up" arrow key.
- Methods like `go_up`, `is_at_finish_line`, and `go_to_start` handle player movement, finish line detection, and position resetting.

### 4. car_manager.py
- `car_manager.py` defines the `CarManager` class, responsible for managing the creation, movement, and difficulty progression of cars.
- The class keeps track of all cars on the screen and includes methods for creating new cars, moving them, and leveling up the game.

## How to Play
1. Run the script `main.py` to start the game.
2. Control the turtle player using the "Up" arrow key to move north.
3. Avoid collisions with randomly moving cars.
4. Successfully cross the road to earn points and advance to the next level.
5. The game ends if the turtle collides with a car.
