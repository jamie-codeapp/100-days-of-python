# Hangman

This is a Python implementation of the classic Hangman game. Players try to guess a randomly selected word by suggesting letters, while avoiding too many incorrect guesses that could lead to losing the game.

## How It Works

1. The computer randomly selects a word from the word list.
2. Players guess letters one by one to try and figure out the word.
3. For every incorrect guess, a part of the hangman is drawn. The game is over when the entire hangman is drawn (6 incorrect guesses) or if the word is guessed correctly.

## Features

-   Random word selection from a predefined list.
-   ASCII art for each stage of the hangman.
-   Interactive input for letter guesses.
-   Tracks and displays player progress (guessed letters, number of lives remaining).
-   A fun and simple game that can be played from the terminal.

## How to Run

1. Download or clone the repository.
2. Navigate to the directory where main.py is located.
3. Open a terminal or command prompt and run the following command:

```
python main.py
```

4. The game will start, and you will be prompted to guess letters.

## Example

```
 _
| |
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |
                   |___/

Word to guess: _ _ _ _ _

Guess a letter:
> a

Word to guess: _ _ a _ _

You guessed b, that's not in the word. You lose a life.
```

## Files

1. `main.py` - The main game script.
2. `hangman_art.py` - Contains ASCII art for the hangman stages and logo.
3. `hangman_words.py` - Contains a list of words for the game.

## Requirements

Python 3.x
