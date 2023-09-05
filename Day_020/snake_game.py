from turtle import Screen
from snake_class import Snake
import time


def set_default_setting():
    screen = Screen()
    screen.bgcolor("black")
    screen.title("Snake-Game")
    screen.tracer(0)
    screen.screensize(600, 600, "black")
    return screen


def listen_for_input(screen, snake_func):
    screen.listen()
    screen.onkeypress(key="Up", fun=snake_func.up)
    screen.onkeypress(key="Down", fun=snake_func.down)
    screen.onkeypress(key="Left", fun=snake_func.left)
    screen.onkeypress(key="Right", fun=snake_func.right)


snake = Snake()
window = set_default_setting()
listen_for_input(window, snake)


game_is_on = True
while game_is_on:
    window.update()
    time.sleep(0.1)

    snake.move()

window.exitonclick()
