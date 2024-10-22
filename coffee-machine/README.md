# Coffee Machine

This is a terminal-based simulation of a coffee machine. Users can order different types of coffee (espresso, latte, or cappuccino), pay for the drinks using virtual coins, and the machine keeps track of resources like water, milk, and coffee beans. The program also reports the machine's current resource status and the money earned.

## How It Works

1. The program presents a prompt asking the user what they would like to order: `espresso`, `latte`, or `cappuccino`.
2. The machine checks if there are enough resources to make the chosen drink.
3. The user is asked to insert coins. The machine calculates the total amount of money inserted.
4. The machine checks if the amount is sufficient to cover the cost of the drink.
5. If the transaction is successful, the drink is made, the resources are deducted, and the user's change is returned.
6. The machine continues until the user types `off`, which turns the machine off.

## Features

-   Coffee Selection: Users can choose from espresso, latte, or cappuccino.
-   Resource Management: The machine checks whether there are enough resources to make the selected drink.
-   Coin Handling: Users can insert coins (quarters, dimes, nickels, and pennies) to purchase drinks.
-   Transaction Verification: The machine verifies if enough money was inserted and provides change if necessary.
-   Report Generation: Users can request a report to view the remaining resources and the total money earned.
-   Shut Down: The machine can be turned off by typing `off`.

## How to Run

1. Ensure you have Python installed on your machine.
2. Download or clone the repository.
3. Navigate to the directory containing `main.py`.
4. Run the following command:

    ```
    python main.py
    ```

5. Usage:
    - Order a Drink:
        - Type `espresso`, `latte`, or `cappuccino` when prompted.
        - Insert coins as requested to complete the transaction.
    - Check Resources and Money:
        - Type `report` to see the current levels of water, milk, coffee, and the money earned.
    - Turn Off the Machine:
        - Type `off` to stop the program.

## Example

```
What would you like? (espresso/latte/cappuccino): latte
Please insert coins.
how many quarters?: 10
how many dimes?: 0
how many nickles?: 0
how many pennies?: 0
Here is $0.00 in change.
Here is your latte ☕️. Enjoy!
```

## Requirements

Python 3.x
