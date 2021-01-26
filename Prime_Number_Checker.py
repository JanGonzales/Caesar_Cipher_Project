# Write your code below this line 👇
def prime_checker(number):
    prime = False
    for i in range(2, number):
        if number % i == 0:
            prime = True
    if prime is True:
        print("Not a prime number")
    elif prime is False:
        print("Prime number")


# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
