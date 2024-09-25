# Treasure Island

This is a simple text-based adventure game where players make choices that will determine whether they find the treasure or face various game-over scenarios.

## How It Works

1. The player is presented with a series of decisions, such as choosing directions or actions.
2. Each choice leads to different outcomes:

-   Successful choices bring the player closer to the treasure.
-   Incorrect choices may lead to "Game Over" scenarios like falling into a hole or being attacked by creatures.

3. The goal is to make the right choices and find the hidden treasure.

## How to Run

To play the game, ensure that Python is installed on your machine, and follow these steps:

1. Download or clone the repository.
2. Navigate to the directory where main.py is located.
3. Open a terminal or command prompt and run the following command:

```
python main.py
```

4. Follow the on-screen prompts to play the game. You will be asked to make choices such as:

-   Choosing a direction at a crossroad.
-   Deciding whether to wait or swim at a lake.
-   Selecting the color of a door when you reach the island.

## Example

```
Welcome to Treasure Island.
Your mission is to find the treasure.

You're at a cross road. Where do you want to go? Type "left" or "right"
> left
You've come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.
> wait
You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose?
> yellow
You find the treasure! You win!
```

If you make the wrong choice, the game will print a "Game Over" message.

## Requirements

Python 3.x
