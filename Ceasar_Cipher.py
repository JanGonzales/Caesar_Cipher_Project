import ACII_art
import os

print(ACII_art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def caesar(plain_text, plain_shift, plain_direction):
    new_list = ""
    if plain_shift > 26:
        plain_shift %= 26
    if plain_direction == "decode":
        plain_shift *= -1
    for letter in plain_text:
        if letter not in alphabet:
            new_list += letter
        elif alphabet.index(letter) + plain_shift > len(alphabet) - 1:
            a = len(alphabet)
            x = (alphabet.index(letter) + plain_shift) - a
            new_list += alphabet[x]
        else:
            letter_number = alphabet.index(letter) + plain_shift
            new_list += alphabet[letter_number]
    print(f"The encoded text is {new_list}")


restart = True
while restart is True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(plain_text=text, plain_shift=shift, plain_direction=direction)
    print("Please make sure to remember your password and shift number before quitting and restarting")
    user_restart = input("Do you want to try again y/N: ").lower()
    if user_restart == "y":
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
    elif user_restart == "n":
        print("Good Bye!")
        restart = False
