# udemy Course - 100 Days of Code - Python

# Debugging
# 1. Describe the Problem
# 2. Reproduce the Bug
# 3. Play Computer
# 4. Fix the Error
# 5. Print is your Friend
# 6. Use debugger
# 7. Take a break
# 8. Ask a friend
# 9. Run often
# 10. Tackle Bugs one at time
# 11. Ask StackOverflow

# Everyone gets bugs

# ###########DEBUGGING#####################

# def my_function():
#   for i in range(1, 21):  # Fixed range to reach 20
#     if i == 20:
#       print("You got it")
# my_function()

# Reproduce the Bug
# from random import randint
# dice_img = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(0, 5)  # Fixed randint to 0, 5 for right indexing
# print(dice_img[dice_num])

# Play Computer
# year = int(input("What's your year of birth?"))
# if 1980 < year < 1994:
#     print("You are a millennial.")
# elif year > 1994:
#     print("You are a Gen Z.")
# else:
#     print("You are freaking old")  # Added an else statement for years < 1980

# # Fix the Errors
# age = input("How old are you?")
# if age > 18:
#     print ("You can drive at age {age}.") # Fixed the indentation error

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: ")) # Fixed operator to be an assigment and not an equal check
# total_words = pages * word_per_page
# print(total_words)

# #Use a Debugger
# def mutate(a_list):
#     b_list = []
#     for item in a_list:
#         new_item = item * 2
#         b_list.append(new_item)  # Fixed indentation error
#     print(b_list)
#
#
# mutate([1, 2, 3, 5, 8, 13])

# Exercise 1
# Debugging odd or even

print("Exercise 1")

number = int(input("Which number do you want to check?"))

if number % 2 == 0:  # Fixed = to ==
    print("This is an even number.")
else:
    print("This is an odd number.")

print("----------------------------------------------")

print("Exercise 2")

year = int(input("Which year do you want to check?"))  # Fixed to typecast into int()

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")

print("----------------------------------------------")

print("Exercise 3")

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:  # Fixed logical operator to and from or
        print("FizzBuzz")
    elif number % 3 == 0:  # Fixed to elif from if
        print("Fizz")
    elif number % 5 == 0:  # Fixed to elif from if
        print("Buzz")
    else:
        print(number)  # Fixed print, removed '[]'

print("----------------------------------------------")
