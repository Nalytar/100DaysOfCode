from turtle import Turtle
BOUNCE_SPEED_Y = 5
BOUNCE_SPEED_X = 10


class Ball(Turtle):
    def __init__(self, color="white"):
        super().__init__()

        self.x_value = BOUNCE_SPEED_X
        self.y_value = BOUNCE_SPEED_Y
        self.move_speed = 0.05

        self.penup()
        self.shape("circle")
        self.color(color)

    def move(self):
        new_x = self.xcor() + self.x_value
        new_y = self.ycor() + self.y_value
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_value *= -1
        self.move_speed *= 0.9

    def bounce_x(self):
        self.x_value *= -1

    def reset_ball(self):
        self.move_speed = 0.05
        self.x_value *= -1
        self.goto(0, 0)
