# udemy Course - 100 Days of Code - Python

# List Comprehension
# name_of_new_list = [(operation) for _ in list]


numbers = [1, 2, 3]
new_list = [n + 1 for n in numbers]

print(numbers)
print(new_list)

name = "Michael"
new_name = [letter for letter in name]

print(new_name)  # List with Elements of that String

double_range = [n * 2 for n in range(1, 5)]
print(double_range)

# Conditional List Comprehension
# name_of_new_list = [(operation) for _ in list if (condition)]

names = ["Axel", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
upper_names = [name.upper() for name in names if len(name) > 5]

print(short_names)
print(upper_names)

# Exercise 1
print("Exercise 1")

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [n * n for n in numbers]

print(squared_numbers)

print("----------------------------------------\n")

# Exercise 2
print("Exercise 2")

even_numbers = [n for n in numbers if n % 2 == 0]
print(even_numbers)

print("----------------------------------------\n")

# Exercise 3
print("Exercise 3")

with open("file1.txt") as file:
    file1 = file.readlines()

with open("file2.txt") as file:
    file2 = file.readlines()

result = [int(num) for num in file1 if num in file2]
print(result)

print("----------------------------------------\n")

# Dictionary Comprehension
# new_dict = {new_key:new_value for item in list}
# new_dict = {new_key:new_values for (key,values) in dict.items() if (condition)}

import random

random_scores = {name: random.randint(1, 100) for name in names}
print(random_scores)

passed_students = {key: value for (key, value) in random_scores.items() if value > 50}
print(passed_students)

# Exercise 4
print("Exercise 4")

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
words = sentence.split(" ")

result = {word: len(word) for word in words}
print(result)

print("----------------------------------------\n")

# Exercise 5
print("Exercise 5")

wheater_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24
}

wheater_f = {day: (temp * 9/5 + 32) for (day, temp) in wheater_c.items()}
print(wheater_f)

print("----------------------------------------\n")

import pandas
# loop through a dictionary

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    print(row.student)
