from turtle import Turtle
ALIGNMENT = "center"
FONT = ("arial", 10, "italic")


class State(Turtle):
    def __init__(self, x, y, name):
        super().__init__()
        self.penup()
        self.color("black")
        self.hideturtle()

        self.goto(x, y)
        self.write(name,
                   True,
                   "center",
                   FONT)
        print("Turtle created")

