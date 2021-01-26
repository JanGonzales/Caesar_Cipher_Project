alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text, plain_shift):
    new_list = ""
    for letter in plain_text:
        if letter == " ":
            new_list += letter
        elif alphabet.index(letter) + plain_shift > len(alphabet) - 1:
            a = len(alphabet)
            x = (alphabet.index(letter) + plain_shift) - a
            new_list += alphabet[x]
        else:
            letter_number = alphabet.index(letter) + plain_shift
            new_list += alphabet[letter_number]
    print(f"The encoded text is {new_list}")

def decrypt(plain_text, plain_shift):
    new_list = ""
    for letter in plain_text:
        if letter == " ":
            new_list += letter
        elif alphabet.index(letter) + plain_shift < 0:
            a = len(alphabet)
            x = plain_shift - (alphabet.index(letter) - a)
            new_list += alphabet[x]
        else:
            letter_number = (alphabet.index(letter) - plain_shift)
            new_list += alphabet[letter_number]
    print(f"The encoded text is {new_list}")

if direction == "encode":
    encrypt(plain_text=text, plain_shift=shift)
elif direction == "decode":
    decrypt(plain_text=text, plain_shift=shift)