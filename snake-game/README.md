# Snake Game

This is a classic Snake Game built using Python's turtle graphics library. Control the snake, eat the food, and try to achieve the highest score without colliding with the walls or your own tail.

## Features

-   Classic snake game mechanics.
-   Simple controls using arrow keys.
-   Score tracking and display.
-   Game over screen when the snake collides with a wall or its own tail.

## Installation

1. Ensure you have Python 3.x installed on your machine.
2. Download or clone this repository to your local machine.
3. Navigate to the project directory.
4. Run the game.

    ```
    python main.py
    ```

## How to Play

-   Use the arrow keys to control the direction of the snake:
    -   **Up Arrow**: Move Up
    -   **Down Arrow**: Move Down
    -   **Left Arrow**: Move Left
    -   **Right Arrow**: Move Right
-   The goal is to eat the food (blue circle) to grow the snake and increase your score.
-   The game ends if the snake collides with the wall or its own tail.

## Files

The project consists of the following files:

-   `main.py`: The main script that initializes the game and contains the game loop.
-   `snake.py`: Defines the Snake class, which handles the snake's movement and growth.
-   `food.py`: Defines the Food class, which creates the food for the snake to eat.
-   `scoreboard.py`: Defines the Scoreboard class, which handles score tracking and game over display.

## Requirements

-   Python 3.x
-   No external libraries are required.
