# udemy Course - 100 Days of Code - Python

# for loop
# for item in list:
# - for list or other iterable datatypes

# for loop with range
# for number in range(1,100):
# - range(start, end *exclusive*, increase)

# Exercise 1
# Get the average height in cm without using sum(), and len() outside of for loop, use for loop

print("Exercise 1")

counter = 0
sums = 0

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
    print(student_heights[n])
    sums += student_heights[n]
    counter += 1

print(round(sums / counter))

print("----------------------------------------------")

# Exercise 2
# Get the highest score of a list, you are not allowed to use the min() or max() function

print("Exercise 2")

student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

highest_score = 0
for score in student_scores:
    if highest_score < score:
        highest_score = score

print(highest_score)

print("----------------------------------------------")

# Exercise 3
# adding even numbers between 1 to 100 including both

print("Exercise 3")

even_sum = 0
for number in range(0, 101, 2):
    even_sum += number

print(even_sum)

print("----------------------------------------------")

# Exercise 4
# Fizz Buzz, number dividable by 15: FizzBuzz, by 3: Fizz, by 5: Buzz

print("Exercise 4")

for number in range(1,101):
    if number % 15 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

print("----------------------------------------------")
