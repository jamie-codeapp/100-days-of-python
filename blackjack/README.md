# Blackjack

This is a simple terminal-based Blackjack game implemented in Python. The game allows a user to play Blackjack against the computer, following the standard rules of the game.

## How the Game Works

-   Each player (you and the computer) is dealt two cards initially.
-   The goal is to get as close to a score of 21 as possible without going over.
-   You can choose to draw more cards or hold your current hand.
-   The game uses a scoring system where face cards (Jack, Queen, King) are worth 10 points, Aces can be worth 11 or 1, and other cards are worth their face value.
-   If either player gets 21 points with the first two cards, that’s a "Blackjack" and an automatic win.
-   If you or the computer exceed 21 points, you "bust" and lose the game.

## Features

-   Clear and simple interface with card symbols.
-   A random card dealer that mimics the drawing of cards from a shuffled deck.
-   Automatic calculation of card values with special handling for Aces.
-   A scoring system that compares the player's and the computer's scores and announces the winner.
-   Ability to play multiple rounds.

## Game Flow

1. The user is prompted to start a new game.
2. Cards are dealt to both the user and the computer.
3. The user's score is displayed, and the user decides whether to draw another card or pass.
4. The computer draws cards until its score is at least 17 or it gets a Blackjack.
5. The final scores are displayed, and the winner is determined.

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
Do you want to play a game of Blackjack? Type 'y' or 'n': y

.------.            _     _            _    _            _
|A_  _ |.          | |   | |          | |  (_)          | |
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
|  \/ | /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
| \  /| /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   <
`-----| \/ |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\

Your cards: [10, 7], current score: 17
Computer's first card: 6
Type 'y' to get another card, type 'n' to pass: n
Your final hand: [10, 7], final score: 17
Computer's final hand: [6, 10, 2], final score: 18
You lose 😤
```

## Files

1. `main.py` - This file contains the main logic for running the game, including card dealing, score calculation, and game control.
2. `art.py` - This file includes ASCII art used to display the logo for the game.

## Requirements

Python 3.x
