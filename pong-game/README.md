# Pong Game

This is a classic Pong game built using Python's turtle graphics module. The game features two paddles and a ball that bounces off the walls and paddles. Players control the paddles to prevent the ball from passing through and score points when the opponent misses

## Features

-   Two-player control:
    -   **Player 1**: Uses the `Up` and `Down` arrow keys to control the right paddle.
    -   **Player 2**: Uses the `W` and `S` keys to control the left paddle.
-   Scorekeeping with a digital scoreboard.
-   Ball speed increases after each paddle hit.
-   Automatic ball reset after scoring.

## Installation

1. Ensure you have Python 3.x installed on your machine.
2. Download or clone this repository to your local machine.
3. Navigate to the project directory.
4. Run the game.

    ```
    python main.py
    ```

## Controls

-   **Right Paddle (Player 1)**:
    -   `Up Arrow`: Move Up
    -   `Down Arrow`: Move Down
-   **Left Paddle (Player 2)**:
    -   `W`: Move Up
    -   `S`: Move Down

## Files

The project consists of the following files:

-   `main.py`: This is the main game loop file where the game setup, event listeners, and game logic are implemented.
-   `ball.py`: This file contains the `Ball` class, which manages the ball's behavior, including movement and collisions.
-   `paddle.py`: This file contains the `Paddle` class, which manages the paddle objects and their movements.
-   `scoreboard.py`: This file contains the `Scoreboard` class, which manages the game score display.

## Requirements

-   Python 3.x
-   No external libraries are required.
