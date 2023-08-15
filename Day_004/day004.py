# udemy Course - 100 Days of Code - Python

import random
# Get a random decimal between 0 and 5

# random_float = random.random() + random.randint(0,4)
# print(random_float)

# Lists in Python using the square brackets
# list = ["item1", "item2"]
# counting starts at 0 so to print item1 we need to address list[0]
# addressing list with -1 like list[-1] will return the last item and so on
# list.append("newItem") will this item to the end of the list


print("----------------------------------------------")

# Exercise 1
# Heads or Tails

print("Exercise 1")

if random.randint(0,1) == 1:
    print("Heads")
else:
    print("Tails")

print("----------------------------------------------")

# Exercise 2
# Banker Roulette
# usage of random.choice is forbidden
# str.split(", ") splits the string @ the given delimiter and return a list with the separated items

print("Exercise 2")

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
number = random.randint(0,len(names)-1)

print(f"{names[number]} is going to buy the meal today!")

print("----------------------------------------------")

# Exercise 3
# Treasure Map
# Ignoring that false input could occur

print("Exercise 3")

row1 = [" ", " ", " "]
row2 = [" ", " ", " "]
row3 = [" ", " ", " "]
treasure_map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to puh the treasure? ")

x = int(position[0])-1
y = int(position[1])-1
treasure_map[y][x] = "X"

print(f"{row1}\n{row2}\n{row3}")

print("----------------------------------------------")
