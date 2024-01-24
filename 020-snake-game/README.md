# Snake Game

A classic Snake game implemented in Python using the Turtle graphics library.

## Files

1. **main.py**:
   - The main entry point of the Snake game. It initializes the game screen, creates instances of the Snake, Food, and Scoreboard classes, sets up key listeners, and runs the main game loop. It handles user input and updates the game state accordingly.

2. **snake.py**:
   - Defines the Snake class, responsible for managing the snake's behavior, movement, and user input. It also contains constants for starting positions, move distance, and direction. The Snake class interacts with the Turtle graphics library to create and manipulate the snake.

3. **food.py**:
   - Implements the Food class, which represents the blue food that the snake can consume to grow. It uses the Turtle graphics library to create a blue circular object at random positions on the screen. The `refresh` method is used to relocate the food when it is consumed by the snake.

4. **scoreboard.py**:
   - Defines the Scoreboard class, responsible for tracking and displaying the player's score. It uses the Turtle graphics library to display the current score on the screen. The class includes methods to update the scoreboard, increase the score, and display the "GAME OVER" message when the game ends.

## How to Play

- Use the arrow keys (Up, Down, Left, Right) to control the snake's direction.
- Eat the blue food to grow the snake and increase your score.
- Avoid collisions with the walls and the snake's own tail.
