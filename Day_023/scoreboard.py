from turtle import Turtle
FONT = ("Courier", 24, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.current_lvl = 1

        self.penup()
        self.hideturtle()
        self.goto(-200, 240)
        self.write_lvl()

    def write_lvl(self):
        self.clear()
        self.write(f"Level: {self.current_lvl}",
                   False,
                   ALIGNMENT,
                   FONT)

    def update_lvl(self):
        self.current_lvl += 1
        self.write_lvl()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER",
                   False,
                   ALIGNMENT,
                   FONT)
