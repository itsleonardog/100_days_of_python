# Pong Game

## Introduction
This is a simple implementation of the classic Pong game using Python's Turtle graphics library. The game includes paddles, a ball, and a scoreboard to keep track of the score.

## Files

### 1. main.py
- `main.py` is the main script that orchestrates the entire Pong game.
- It sets up the game window using the Turtle graphics library, creates instances of the Paddle, Ball, and Scoreboard classes, and handles user input.
- The game loop continuously updates the screen and moves the ball and paddles based on user input and game logic.
- It includes collision detection for the ball with the walls and paddles, and updates the score on the scoreboard accordingly.

### 2. scoreboard.py
- `scoreboard.py` defines the `Scoreboard` class, which is responsible for keeping track of and displaying the scores of both players.
- It inherits from the Turtle class to utilize Turtle graphics for displaying the scores on the game window.
- The `l_point` and `r_point` methods increment the scores for the left and right players, respectively.
- The `update_scoreboard` method updates the displayed scores on the screen.

### 3. paddle.py
- `paddle.py` contains the `Paddle` class, representing the paddles in the Pong game.
- Each paddle is a rectangular shape with specific dimensions and movement methods (`go_up` and `go_down`).
- The paddles are controlled by user input and are responsible for moving up and down within the game window.

### 4. ball.py
- `ball.py` defines the `Ball` class, representing the game ball.
- The ball is a circular shape with attributes such as movement speed and direction.
- The `move` method updates the ball's position based on its current speed and direction.
- The `bounce_y` and `bounce_x` methods handle bouncing the ball off the top/bottom and left/right walls, respectively.
- The `reset_position` method resets the ball to the center of the screen when a point is scored.

## How to Play
- Use the Up and Down arrow keys for the right paddle.
- Use 'w' and 's' keys for the left paddle.

Enjoy the game!