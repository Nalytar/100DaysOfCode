from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self, color="blue", shape="circle", speed="fastest"):
        super().__init__(shape)
        self.color(color)
        self.penup()
        self.shapesize(0.75, 0.75)
        self.speed(speed)
        self.randomize_position()

    def randomize_position(self):
        x = random.randint(-14, 14) * 20
        y = random.randint(-14, 14) * 20
        self.goto(x, y)
