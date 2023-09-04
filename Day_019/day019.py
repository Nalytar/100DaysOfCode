# udemy Course - 100 Days of Code - Python

# Turtle Event Listener
import turtle as t


def move_forward():
    timmy.forward(1)


def move_backwards():
    timmy.back(1)


def move_right():
    timmy.right(1)


def move_left():
    timmy.left(1)


def reset_game():
    timmy.clear()
    timmy.reset()


timmy = t.Turtle()
screen = t.Screen()

screen.listen()
screen.onkeypress(move_forward, "w")
screen.onkeypress(move_left, "a")
screen.onkeypress(move_backwards, "s")
screen.onkeypress(move_right, "d")
screen.onkey(reset_game, "c")

screen.exitonclick()
