import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Create and configure Screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Create game elements
car_manager = CarManager()
score_board = Scoreboard()
player = Player()

# Event listener for input
screen.listen()
screen.onkeypress(key="w", fun=player.move)

# Game loop
game_is_on = True
while game_is_on:
    time.sleep(0.01)
    screen.update()

    car_manager.cars_start()

    # Reaching end of line for new lvl
    if player.ycor() >= 280:
        player.next_level()
        score_board.update_lvl()
        car_manager.increase_speed()

    car_manager.replace_cars()

    if car_manager.detect_collision(player):
        game_is_on = False
        score_board.game_over()

# Exit Program
screen.exitonclick()
