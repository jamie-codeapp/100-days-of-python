from os import system, name
import random
from art import logo, vs
from game_data import data


def clear():
    """Clear screen."""
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")


def format_data(account):
    """Takes the account data and returns the printable format."""
    return f"{account["name"]}, a {account["description"]}, from {account["country"]}"


def check_answer(user_guess, a_followers, b_followers):
    """Take a user's guess and the follower counts and returns if they got it right."""
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"


score = 0
is_game_over = False

account_a = random.choice(data)
account_b = random.choice(data)

while not is_game_over:
    clear()

    account_a = account_b
    while account_a == account_b:
        account_b = random.choice(data)

    print(logo)

    if score > 0:
        print(f"You're right! Current score: {score}.")

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    if check_answer(guess, account_a["follower_count"], account_b["follower_count"]):
        score += 1
    else:
        is_game_over = True

clear()
print(logo)
print(f"Sorry, that's wrong. Final score: {score}")
