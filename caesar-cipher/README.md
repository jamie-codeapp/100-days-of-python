# Caesar Cipher

This Python program implements a simple Caesar Cipher for encoding and decoding messages. The Caesar Cipher shifts the letters of the alphabet by a specified number, wrapping around if necessary. Users can encode or decode messages interactively.

## How It Works

1. The user selects whether they want to "encode" (encrypt) or "decode" (decrypt) a message.
2. The user inputs the message they want to encrypt or decrypt.
3. The user provides the shift number, which determines how many positions to shift the letters in the alphabet.
4. The program shifts the letters of the message by the specified amount and prints the encoded or decoded result.

### Caesar Cipher Rules:

-   The alphabet is shifted in one direction for encoding and the opposite direction for decoding.
-   Non-alphabet characters (such as spaces and punctuation) remain unchanged.

## How to Run

1. Download or clone the repository.
2. Navigate to the directory where main.py is located.
3. Open a terminal or command prompt and run the following command:

```
python main.py
```

4. Follow the prompts:

-   Choose to encode or decode.
-   Enter the message.
-   Enter the shift amount.

5. The program will display the encoded or decoded message and ask if you'd like to run it again.

## Example

```
Type 'encode' to encrypt, type 'decode' to decrypt:
> encode
Type your message:
> hello world
Type the shift number:
> 5
Here's the encoded result: mjqqt btwqi

Type 'yes' if you want to go again. Otherwise type 'no'.
> no
Goodbye
```

## Files

1. `main.py` - Contains the logic for encoding and decoding using the Caesar Cipher.
2. `art.py` - Contains an ASCII art logo that is displayed when the program starts.

## Requirements

Python 3.x
