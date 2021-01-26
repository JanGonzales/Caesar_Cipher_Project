alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(plain_text, plain_shift):
    # TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
    new_list = ""
    for letter in plain_text:
        letter_number = alphabet.index(letter) + plain_shift
        new_list += alphabet[letter_number]
    print(new_list)
    # e.g.
    # plain_text = "hello"
    # shift = 5
    # cipher_text = "mjqqt"
    # print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    # https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

# def encrypt(plain_text, plain_shift): ALTERNATIVE METHOD
#     counter = 0
#     new_list = ""
#     while len(new_list)< len(text):
#         for var in range(0, len(alphabet) -1):
#             if text[counter] in alphabet[var]:
#                 var += shift
#                 new_list += alphabet[var]
#         counter += 1

# TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.
encrypt(plain_text=text, plain_shift=shift)
