# Rock, Paper, Scissors

This is a Python implementation of the classic "Rock, Paper, Scissors" game. The player competes against the computer by selecting one of the three options: Rock, Paper, or Scissors.

## How It Works

1. The player is prompted to choose:

-   `0` for Rock
-   `1` for Paper
-   `2` for Scissors

2. The computer randomly selects Rock, Paper, or Scissors.

3. The game compares the player’s and computer’s choices and declares a winner based on the following rules:

-   Rock beats Scissors.
-   Scissors beats Paper.
-   Paper beats Rock.
-   If both choose the same, it's a draw.

## How to Run

To play the game, make sure Python is installed on your machine. Follow these steps:

1. Download or clone the repository.
2. Navigate to the directory where main.py is located.
3. Open a terminal or command prompt and run the following command:

```
python main.py
```

4. The game will ask you to enter:

-   `0` for Rock
-   `1` for Paper
-   `2` for Scissors

5. The game will then display both your choice and the computer's choice, followed by the result.

## Example

```
What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.
> 1
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
Computer chose:
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

You win!
```

If you enter an invalid number, the game will automatically consider it a loss.

## Requirements

Python 3.x
