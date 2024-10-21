# Higher Lower Game

This is a terminal-based game where players guess which of two accounts has more followers on social media. The player is presented with two accounts from the dataset, and their goal is to guess which one has a higher follower count.

## How It Works

1. The game starts by displaying a random account `A` and another random account `B`.
2. The player guesses which account has more followers by typing either 'A' or 'B'.
3. If the guess is correct, the player scores a point, and a new account is presented for comparison.
4. If the guess is incorrect, the game ends, and the player's final score is displayed.

## Features

-   Random selection of accounts from a predefined dataset.
-   Feedback on whether the guess was correct.
-   The game continues until the player makes an incorrect guess, and the final score is displayed.

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
    __  ___       __
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /
/_/ ///_/\__, /_/ /_/\___/_/
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /
/_____/_____/|__/|__/\___/_/

Compare A: Instagram, a Social media platform, from United States.
 _    __
| |  / /____
| | / / ___/
| |/ (__  )
|___/____(_)

Against B: Cristiano Ronaldo, a Footballer, from Portugal.
Who has more followers? Type 'A' or 'B': B

    __  ___       __
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /
/_/ ///_/\__, /_/ /_/\___/_/
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /
/_____/_____/|__/|__/\___/_/

You're right! Current score: 1.
Compare A: Cristiano Ronaldo, a Footballer, from Portugal.
 _    __
| |  / /____
| | / / ___/
| |/ (__  )
|___/____(_)

Against B: Ariana Grande, a Musician and actress, from United States.
Who has more followers? Type 'A' or 'B':

```

## Files

1. `main.py` - This file contains the main logic of the game, including the user interface, score tracking, and game loop.
2. `art.py`: This file contains ASCII art used to display the game's logo and visual separator (`vs`).
3. `game_data.py`: This file contains the data used in the game, including names, follower counts, professions, and countries of various accounts.

## Requirements

Python 3.x
