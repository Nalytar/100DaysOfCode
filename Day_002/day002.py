# udemy Course - 100 Days of Code - Python

# - Data Types -

# String
# "Hello"[0] = "H" - subscript
# can throw index out of range

# Integer, whole numbers
# 123

# Float, decimal numbers
# 15.4

# Boolean
# true or false

# Typecasting of Strings to float/int

# Exercise 1
# Insert a two-digit number and print the cross sum
two_digit_number = input("Type a two digit number: ")

number1 = int(two_digit_number[0])
number2 = int(two_digit_number[1])

print(f"{number1} + {number2} = {number1 + number2}")
print(number1 + number2)

print("----------------------------------------------")

# Exercise 2
# BMI-Calculator with Integer output

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
bmi = float(weight) / float(height)**2

print(int(bmi))

print("----------------------------------------------")

# Exercise 3
# Life week calculator until 90 years old

age = int(input("What is your current age? "))
days = (90 - age) * 365
weeks = (90 - age) * 52
months = (90 - age) * 12

print(f"Your have {days} days, {weeks} weeks, and {months} months left.")