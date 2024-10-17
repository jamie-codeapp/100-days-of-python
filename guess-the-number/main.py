from random import randint
from art import logo


def set_difficulty():
    if input("Choose a difficulty. Type 'easy' or 'hard':\n").lower() == "easy":
        return 10
    else:
        return 5


def check_answer(user_guess, actual_answer, remaining_lives):
    if user_guess > actual_answer:
        print("Too high.")
        return remaining_lives - 1
    elif user_guess < actual_answer:
        print("Too low.")
        return remaining_lives - 1
    else:
        print(f"You got it! The answer was {actual_answer}.")
        return remaining_lives


print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

answer = randint(1, 100)

lives = set_difficulty()

while lives >= 1:
    print(f"You have {lives} attempts remaining to guess the number.")

    guess = int(input("Make a guess:\n"))

    lives = check_answer(guess, answer, lives)

    if guess != answer and lives != 0:
        print("Guess again.")
    else:
        break

if lives == 0:
    print("You've run out of guesses, you lose.")
