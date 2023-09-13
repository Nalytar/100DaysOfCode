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
        self.high_score = self.read_high_score()
        self.goto(LABEL_POSITION)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}",
                   False,
                   ALIGNMENT,
                   (FONT_NAME, FONT_SIZE, FONT_TYPE))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_high_score(self.high_score)
        self.score = 0
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER",
                   False,
                   ALIGNMENT,
                   (FONT_NAME, FONT_SIZE, FONT_TYPE))

    def read_high_score(self):
        with open("data.txt") as file:
            high_score = file.read()
        return int(high_score)

    def write_high_score(self, new_high_score):
        with open("data.txt", "w") as file:
            file.write(str(new_high_score))
