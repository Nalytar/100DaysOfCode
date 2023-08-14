# udemy Course - 100 Days of Code - Python

# Comparison Operator
# >, <, >=, <=, ==

# Exercise 1
# if-else and modulo operator

print("Exercise 1")

number = int(input("Which number do you want to check? "))

if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")

print("----------------------------------------------")

# Exercise 2
# BMI Calculator with interpretation of bmi

print("Exercise 2")

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
bmi = float(float(weight) / float(height)**2)
interpretation = ""

if bmi < 18.5:
    interpretation = "you are underweight"
elif bmi < 25:
    interpretation = "you have a normal weight"
elif bmi < 30:
    interpretation = "you are slightly overweight"
elif bmi < 35:
    interpretation = "you are obese"
else:
    interpretation = "you are clinically obese"

print(f"Your BMI is {bmi:.0f}, {interpretation}.")

print("----------------------------------------------")

# Exercise 3
# Checks if its Leap Year

print("Exercise 3")

year = int(input("Which year do you want to check? "))

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print("Leap year")
else:
    print("Not leap year")

print("----------------------------------------------")

# Exercise 4
# "Pizza Order Programm"

print("Exercise 4")

size = input("What size pizza do you want? S, M, or L ").upper()
add_peperoni = input("Do you want pepperoni? Y or N ").upper()
extra_cheese = input("Do you want extra cheese? Y or N ").upper()
bill = 0

if size == "S":
    bill = 15
    if add_peperoni == "Y":
        bill += 2
elif size == "M":
    bill = 20
    if add_peperoni == "Y":
        bill += 3
else:
    bill = 25
    if add_peperoni == "Y":
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: €/${bill}.")

print("----------------------------------------------")

# Exercise 5
# Love score calculator

print("Exercise 5")

name1 = input("What is your name? \n").lower()
name2 = input("WHat is their name? \n").lower()

name_together = name1 + name2
letter_t = name_together.count("t")
letter_r = name_together.count("r")
letter_u = name_together.count("u")
letter_e = name_together.count("e")
letter_l = name_together.count("l")
letter_o = name_together.count("o")
letter_v = name_together.count("v")

score_true = letter_t + letter_r + letter_u + letter_e
score_love = letter_l + letter_o + letter_v + letter_e

score = int(str(score_true) + str(score_love))

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif 40 < score < 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")

print("----------------------------------------------")
