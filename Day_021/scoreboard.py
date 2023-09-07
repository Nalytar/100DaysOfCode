from turtle import Turtle
FONT_SIZE = 16
FONT_NAME = "courier"
FONT_TYPE = "normal"
ALIGNMENT = "center"
LABEL_POSITION = (0, 280)


class Scoreboard(Turtle):

    def __init__(self, color="white"):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color(color)

        self.score = 0
        self.goto(LABEL_POSITION)
        self.write(f"Score: {self.score}",
                   False,
                   ALIGNMENT,
                   (FONT_NAME, FONT_SIZE, FONT_TYPE))

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}",
                   False,
                   ALIGNMENT,
                   (FONT_NAME, FONT_SIZE, FONT_TYPE))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER",
                   False,
                   ALIGNMENT,
                   (FONT_NAME, FONT_SIZE, FONT_TYPE))
