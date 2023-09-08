from turtle import Screen
from Scoreboard import Scoreboard
from Paddle import Paddle
from Ball import Ball
import time


BG_COLOR = "black"

game_screen = Screen()

game_screen.bgcolor(BG_COLOR)
game_screen.setup(800, 600)
game_screen.title("Pong")
game_screen.tracer(0)

score_board = Scoreboard()
paddle_left = Paddle("left")
paddle_right = Paddle("right")
ball = Ball()

game_screen.listen()
game_screen.onkeypress(fun=paddle_left.up, key="w")
game_screen.onkeypress(fun=paddle_left.down, key="s")
game_screen.onkeypress(fun=paddle_right.up, key="Up")
game_screen.onkeypress(fun=paddle_right.down, key="Down")

game_is_on = True
while game_is_on:
    game_screen.update()
    time.sleep(ball.move_speed)

    ball.move()

    # Detect Top, Bottom wall collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect scoring point
    if ball.xcor() > 380:
        score_board.update_score(1)
        ball.reset_ball()

    if ball.xcor() < -380:
        score_board.update_score(2)
        ball.reset_ball()

    # Detect Collision with Paddle
    if ball.distance(paddle_right) < 50 and ball.xcor() > 330:
        ball.bounce_x()
    if ball.distance(paddle_left) < 50 and ball.xcor() < -330:
        ball.bounce_x()

    if score_board.check_for_winner():
        game_is_on = False

game_screen.exitonclick()
