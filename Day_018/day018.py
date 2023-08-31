# udemy Course - 100 Days of Code - Python
import turtle
from turtle import Turtle, Screen
import random

# timmy_the_turtle = Turtle()
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("red")
#
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# screen = Screen()
# screen.exitonclick()

timmy = Turtle()

# Exercise 1
# Draw a Square

# turtle.shape("turtle")
# turtle.color("orange")
#
# for _ in range(1, 5):
#     turtle.forward(100)
#     turtle.right(90)


# Exercise 2
# Draw a dashed line

# for _ in range(1, 30):
#     if _ % 2 == 0:
#         turtle.penup()
#     else:
#         turtle.pendown()
#     turtle.forward(10)


# Exercise 3
# Draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon, and decagon

# for number in range(0, 8):
#     colors = ["red", "green", "blue", "yellow", "orange", "brown", "black", "gray", "pink"]
#     turtle.color(colors[number])
#     for _ in range(0, 3+number):
#         turtle.right((360/(3+number)))
#         turtle.forward(100)


# Exercise 4
# Generate a random Walk


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    tuple = (r, g, b)  # Tuple is an immutable type
    return tuple


# turtle.colormode(255)
# moves = [timmy.right,
#          timmy.left,
#          timmy.forward]
# timmy.speed(7)
# timmy.pensize(5)
#
# for _ in range(0, 1000):
#     timmy.color(random_color())
#     move = random.choice(moves)
#     if move in moves[0:2]:
#         move(90)
#     else:
#         move(20)

# Exercise 5
# Make a Spirograph

# turtle.colormode(255)
# timmy.speed("fastest")
# for _ in range(0, 360):
#     timmy.color(random_color())
#     timmy.circle(125)
#     timmy.left(1)

screen = Screen()
screen.exitonclick()
