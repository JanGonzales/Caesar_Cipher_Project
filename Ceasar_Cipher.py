alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text, plain_shift):
    new_list = ""
    for letter in plain_text:
        if letter == " ":
            new_list += letter
        elif alphabet.index(letter) + plain_shift > len(alphabet) -1:
            a = len(alphabet) - 1
            x = (alphabet.index(letter) + plain_shift) - a
            new_list += alphabet[x]
        else:
            letter_number = alphabet.index(letter) + plain_shift
            new_list += alphabet[letter_number]
    print(f"The encoded text is {new_list}")

# def encrypt(plain_text, plain_shift): ALTERNATIVE METHOD
#     counter = 0
#     new_list = ""
#     while len(new_list)< len(text):
#         for var in range(0, len(alphabet) -1):
#             if text[counter] in alphabet[var]:
#                 var += shift
#                 new_list += alphabet[var]
#         counter += 1

encrypt(plain_text=text, plain_shift=shift)
