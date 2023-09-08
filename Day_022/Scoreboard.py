from turtle import Turtle
X_POSITION = 0
Y_POSITION = 240
ALIGNMENT = "center"
FONT_TYPE = "bold"
FONT_SIZE = 30
FONT_NAME = "courier"


class Scoreboard(Turtle):
    def __init__(self, color="white"):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score_player_1 = 0
        self.score_player_2 = 0

        self.color(color)
        self.goto(X_POSITION, Y_POSITION)
        self.write(f"{self.score_player_1} | {self.score_player_2}",
                   False,
                   ALIGNMENT,
                   (FONT_NAME, FONT_SIZE, FONT_TYPE))

    def update_score(self, player):
        if player == 1:
            self.score_player_1 += 1
        else:
            self.score_player_2 += 1

        self.clear()
        self.write(f"{self.score_player_1} | {self.score_player_2}",
                   False,
                   ALIGNMENT,
                   (FONT_NAME, FONT_SIZE, FONT_TYPE))

    def check_for_winner(self):
        got_a_winner = False
        winner = ""
        if self.score_player_1 == 5:
            winner = "Player 1 won!"
            got_a_winner = True
        elif self.score_player_2 == 5:
            winner = "Player 2 won!"
            got_a_winner = True

        if got_a_winner:
            self.goto(0, 0)
            self.write(winner,
                       False,
                       ALIGNMENT,
                       (FONT_NAME, FONT_SIZE, FONT_TYPE))
        return got_a_winner
