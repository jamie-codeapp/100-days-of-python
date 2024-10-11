# Calculator

This is a simple command-line calculator program built in Python. It supports basic arithmetic operations—addition, subtraction, multiplication, and division. The program features continuous calculation mode and clears the terminal between new calculations.

## How It Works

1. The program displays an ASCII art logo.
2. The user is prompted to input a number and select an arithmetic operation (`+`, `-`, `*`, `/`).
3. After inputting the second number, the program calculates the result.
4. The user can either:
    - Continue calculating with the current result, or
    - Start a new calculation from scratch.
5. The process repeats until the user decides to exit.

## Features

-   Performs basic arithmetic operations: addition, subtraction, multiplication, and division.
-   Allows continuous calculations using the result of previous operations.
-   Displays a custom ASCII art logo.

## How to Run

1. Ensure you have Python installed on your machine.
2. Download or clone the repository.
3. Navigate to the directory containing `main.py` and `art.py`.
4. Run the following command:

```
python main.py
```

5. Follow the prompts to input numbers and select operations:
    - You will be asked to enter the first number.
    - Pick an arithmetic operation (`+`, `-`, `*`, `/`).
    - Enter the second number.
    - The result will be displayed.
    - You can continue calculating with the result or start a new calculation.

## Example

```
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------.
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------'
|_____________________|

What's the first number?:
> 10

Pick an operation:
> +
What's the next number?:
> 5

10 + 5 = 15

Type 'y' to continue calculating with 15, or type 'n' to start a new calculation:
> n
```

## Files

1. `main.py` - This file implements a simple calculator that:
    - Performs basic arithmetic operations (addition, subtraction, multiplication, division).
    - Displays the logo from art.py.
    - Allows continuous calculations using previous results.
    - Clears the terminal between calculations.
2. `art.py` - Contains the ASCII art logo displayed at the start of the program.

## Requirements

Python 3.x
