import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
# - doing that!

generated_password = []

for _ in range(0, nr_letters):
    generated_password.append(random.choice(letters))

for _ in range(0, nr_symbols):
    generated_password.append(random.choice(symbols))

for _ in range(0, nr_numbers):
    generated_password.append(random.choice(numbers))

# Why we shuffle 7 times? Well i like to play card games. It's just to honor Bayer and Diaconis who showed that after
# seven random riffle shuffles of a deck of 52 cards every configuration is nearly equally likely.
# There is no other use, for performance you might want to delete this for-loop, !watch out for the indentation!
for _ in range(0, 7):
    random.shuffle(generated_password)

generated_password_string = ""

for char in generated_password:
    generated_password_string += char

print(generated_password_string)
