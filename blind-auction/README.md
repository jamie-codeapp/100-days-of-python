# Blind Auction

This Python program simulates a simple auction system. Multiple users can place bids, and the program determines the highest bidder. It also features a console-clearing function to keep the interface clean during input.

## How It Works

1. The program starts by displaying an ASCII art logo.
2. Users input their name and bid amount.
3. After each bid, the program asks if there are any other bidders.
4. Once all bids are placed, the program displays the highest bid and the corresponding bidder's name.

## Features

-   Console Clearing: Depending on the operating system (Windows, Mac, or Linux), the console is cleared between bids to provide a cleaner interface.
-   Multiple Bidders: The program allows multiple bidders to input their bids.
-   Highest Bid Calculation: Once bidding ends, the highest bidder and their bid are displayed.

## How to Run

1. Ensure you have Python installed on your machine.
2. Download or clone the repository.
3. Navigate to the directory containing `main.py` and `art.py`.
4. Run the following command:

```
python main.py
```

5. Follow the prompts:

-   Enter your name and bid.
-   Indicate whether there are more bidders.

6. The program will display the highest bid at the end.

## Example

```
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\
                       .-------------.
                      /_______________\

What is your name?: Alice
What is your bid?: $100
Are there any other bidders? Type 'yes' or 'no'.
> yes
What is your name?: Bob
What is your bid?: $150
Are there any other bidders? Type 'yes' or 'no'.
> no
The winner is Bob with a bid of $150
```

## Files

1. `main.py` - The main program logic for collecting bids and determining the winner.
2. `art.py` - Contains the ASCII art logo displayed at the start of the program.

## Requirements

Python 3.x
