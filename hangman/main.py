import random
from hangman_art import stages, logo
from hangman_words import word_list

print(logo)

chosen_word = random.choice(word_list)

placeholder = ""
for _ in range(len(chosen_word)):
    placeholder += "_"
print(f"Word to guess: {placeholder}")

is_game_over = False
lives = 6
display_list = list(placeholder)

while not is_game_over:
    guess = input("Guess a letter:\n").lower()

    if guess in chosen_word:
        if guess in display_list:
            print(f"You've already guessed {guess}")
        else:
            for index, letter in enumerate(chosen_word):
                if guess == letter:
                    display_list[index] = letter

        display = "".join(display_list)
        print(f"Word to guess: {display}")

    else:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

    if "_" not in display_list:
        is_game_over = True
        print("***********************YOU WIN!**********************")
    else:
        print(
            f"****************************{lives}/6 LIVES LEFT****************************"
        )

    print(stages[lives])

    if lives == 0:
        is_game_over = True
        print(
            f"***********************IT WAS {chosen_word}! YOU LOSE**********************"
        )
