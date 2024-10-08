from os import system, name
from art import logo


def clear():
    # for windows
    if name == "nt":
        _ = system("cls")
    # for mac and linux
    else:
        _ = system("clear")


def find_highest_bider(bidding_dictionary):
    winner = ""
    highest_bid = 0

    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            winner = bidder
            highest_bid = bid_amount

    print(f"The winner is {winner} with a bid of ${highest_bid}")


is_bidding = True
bids = {}

print(logo)

while is_bidding:
    name = input("What is your name?: ")
    price = float(input("What is your bid?: $"))

    bids[name] = price

    if input("Are there any other bidders? Type 'yes' or 'no'.\n").lower() != "yes":
        is_bidding = False
    else:
        clear()

find_highest_bider(bids)
