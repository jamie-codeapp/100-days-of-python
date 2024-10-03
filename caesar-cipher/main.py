from art import logo

alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]

should_continue = True


def caesar(original_text, shift_amount, encode_decode):
    output_text = ""

    if encode_decode == "decode":
        shift_amount *= -1

    for letter in original_text:
        if letter in alphabet:
            index = alphabet.index(letter) + shift_amount
            index %= len(alphabet)
            output_text += alphabet[index]
        else:
            output_text += letter

    print(f"Here's the {encode_decode}d result: {output_text}")


print(logo)

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, encode_decode=direction)

    again = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")

    if again != "yes":
        should_continue = False
        print("Goodbye")
