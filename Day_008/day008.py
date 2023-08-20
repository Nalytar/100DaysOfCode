# udemy Course - 100 Days of Code - Python

# Create a function called greet()
# Write 3 print statements inside the function
# Call the function

def greet():
    print("Hello")
    print("Hallo")
    print("Bonjour")


greet()


def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}")


greet_with_name("Michael")


def greet_with_name_and_location(name, location):
    print(f"Hello {name}")
    print(f"{location} is really pretty")


greet_with_name_and_location("Paul", "Berlin")

# Using keyword arguments (name = "", location = "")
greet_with_name_and_location(location="Paris", name="Sarah")

# Exercise 1
# Paint Area Calculator

print("Exercise 1")

import math


def paint_calc(height, width, cover):
    cans = math.ceil(height * width / cover)
    print(f"You'll need {cans} of paint.")


test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

print("----------------------------------------------")

# Exercise 2
# Prime Number Checker

print("Exercise 2")


def prime_checker(number):
    counter = number - 1
    while counter > 2:
        if number % counter == 0:
            print("It`s not a prime number.")
            return
        counter -= 1
    print("It's a prime number.")


n = int(input("Check this number: "))
prime_checker(number=n)

print("----------------------------------------------")
