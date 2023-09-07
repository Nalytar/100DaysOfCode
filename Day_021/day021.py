# udemy Course - 100 Days of Code - Python

# Day 020
# Step 1 Create Snake Body
# Step 2 Move the Snake
# Step 3 Control the Snake

# Day 021
# Step 4 detect food collision
# Step 5 Create Scoreboard
# Step 6 Detect collision with wall
# Step 7 Detect collision with wall

# class Inheritance and List slicing

# Class inheritance 

class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")


class Fish(Animal):
    def __init__(self):
        super().__init__()  # Call initializer from superclass

    def breathe(self):
        super().breathe()  # Calling the superclass breathe method
        print("doing this underwater")  # Adding own elements or full override this method

    def swim(self):
        print("moving in water.")


nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)

# List Slicing

# Example Piano keys
piano_keys = ["a", "b", "c", "d", "e", "f", "g"]
# get c, d, e
print(piano_keys[2:5])
# [Start index included : End index excluded : Increment(jump)]
# [2:] from index 2 until end of list
# [:5] from start of the list to index 4
# [2:5:2] from index to every second value of the list
# [::-1] from end of the list to the begging

# also works for tuples
