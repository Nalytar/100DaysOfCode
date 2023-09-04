from turtle import Turtle, Screen
import random as rng

colors = ["red", "orange", "green", "blue", "purple", "yellow"]
race_turtles = []


def create_turtles():
    for color in colors:
        race_turtles.append(Turtle("turtle"))
        race_turtles[-1].color(color)
        race_turtles[-1].penup()


def place_turtles():
    x = -220.0
    y = -125.0

    for r_turtle in race_turtles:
        r_turtle.goto(x, y)
        y += 50


def get_bet():
    bet_color = screen.textinput("Bet!",
                                 "On which turtle do you want to bet?\nred, blue, green, orange, yellow")
    while bet_color not in colors:
        bet_color = screen.textinput("Bet!",
                                     "On which turtle do you want to bet?\nred, blue, green, orange, yellow")
    return bet_color


def start_race():
    racing = True
    while racing:
        for r_turtle in race_turtles:
            r_turtle.forward(rng.randint(0, 10))
            if r_turtle.xcor() > 220:
                racing = False
                return r_turtle.pencolor()


screen = Screen()
screen.setup(width=500, height=400)

create_turtles()
place_turtles()
color_bet = get_bet()
winner = start_race()
if color_bet == winner:
    print("You won your bet!")
else:
    print(f"Your Turtle didn't won, the winner is {winner}.")

screen.exitonclick()
