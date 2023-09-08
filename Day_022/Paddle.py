from turtle import Turtle
BOUNDS_POSITIVE = 240
BOUNDS_NEGATIVE = -240
UP = 90
DOWN = 270
DISTANCE = 20


class Paddle(Turtle):
    def __init__(self, site):
        super().__init__()
        self.create_paddle(site)

    def create_paddle(self, site):
        if site == "left":
            x_cor = -350
        else:
            x_cor = 350
        self.penup()
        self.setheading(UP)

        self.shape("square")
        self.shapesize(1, 5)
        self.color("white")

        self.setpos(x_cor, 0.0)

    def up(self):
        if self.ycor() < BOUNDS_POSITIVE:
            self.setheading(UP)
            self.forward(DISTANCE)

    def down(self):
        if self.ycor() > BOUNDS_NEGATIVE:
            self.setheading(DOWN)
            self.forward(DISTANCE)
