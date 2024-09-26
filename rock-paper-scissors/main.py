import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

rock_paper_scissors = [rock, paper, scissors]

player_choice = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
)
if 0 <= player_choice <= 2:
    print(rock_paper_scissors[player_choice])

    print("Computer chose:")
    computer_choice = random.randint(0, 2)
    print(rock_paper_scissors[computer_choice])

    if player_choice == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == 0 and player_choice == 2:
        print("You lose")
    elif player_choice < computer_choice:
        print("You lose")
    elif player_choice > computer_choice:
        print("You win!")
    elif player_choice == computer_choice:
        print("It's a draw")
else:
    print("You type invalid number. You lose!")
