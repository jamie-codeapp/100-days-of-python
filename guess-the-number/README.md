# Guess The Number

This is a simple terminal-based number guessing game where the player has to guess a number between 1 and 100. The game provides feedback on whether the guess was too high or too low, and the player has a limited number of attempts depending on the difficulty level.

## How It Works

1. The player is prompted to choose a difficulty level.
2. A random number between 1 and 100 is generated.
3. The player guesses the number.
4. The game provides feedback on whether the guess was too high or too low.
5. The game continues until the player guesses correctly or runs out of attempts.

## Features

-   Two difficulty levels: easy (10 attempts) and hard (5 attempts).
-   Random number generation between 1 and 100 for each game.
-   Feedback on whether the guess is too high or too low.
-   Endgame messages indicating whether the player won or lost.

## How to Run

1. Ensure you have Python installed on your machine.
2. Download or clone the repository.
3. Navigate to the directory containing `main.py` and `art.py`.
4. Run the following command:

    ```
    python main.py
    ```

5. Follow the on-screen instructions to play the game.

## Example

```
   ___                       _____ _                __                 _
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|


Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
Choose a difficulty. Type 'easy' or 'hard':
> hard
You have 5 attempts remaining to guess the number.
Make a guess:
> 52
Too high.
Guess again.
You have 4 attempts remaining to guess the number.
Make a guess:
> 38
Too high.
Guess again.
You have 3 attempts remaining to guess the number.
Make a guess:
> 23
Too high.
Guess again.
You have 2 attempts remaining to guess the number.
Make a guess:
> 12
Too high.
Guess again.
You have 1 attempts remaining to guess the number.
Make a guess:
> 8
Too low.
You've run out of guesses, you lose.
```

## Files

1. `main.py` - This file contains the main logic for the game, including number generation, input handling, and feedback on the player's guesses.
2. `art.py` - This file contains ASCII art that displays the game's logo.

## Requirements

Python 3.x
