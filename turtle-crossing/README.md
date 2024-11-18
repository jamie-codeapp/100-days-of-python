# Turtle Crossing Game

The Turtle Crossing Game is a simple Python game built using the `turtle` module. In this game, the player controls a turtle that must avoid oncoming cars by moving upwards on the screen. The objective is to reach the top of the screen without colliding with any cars. The game includes a scoring system that increases the level after each successful crossing, and the speed of the cars increases with each level.

## How to Run

1. Ensure you have Python 3.x installed on your machine.
2. Download or clone this repository to your local machine.
3. Navigate to the project directory.
4. Run the game.

    ```
    python main.py
    ```

## How to Play

-   Use the **Up Arrow** key to move the player turtle upwards.
-   The goal is to reach the top of the screen without colliding with any oncoming cars.
-   Each time the player reaches the finish line, the level increases, and the speed of the cars also increases.
-   The game ends when the player collides with a car, and a "GAME OVER" message is displayed.

## Files

-   **player.py**: Contains the `Player` class, which controls the turtle. It handles movement and resetting the player's position.
-   **car_manager.py**: Contains the `CarManager` class that handles creating and moving cars. It also increases the car speed as the game progresses.
-   **scoreboard.py**: Manages the display of the game’s level and shows a "GAME OVER" message when the player loses.
-   **main.py**: The main game logic where the game runs, and the player interacts with the game world.

## Requirements

-   Python 3.x
-   No external libraries are required.
