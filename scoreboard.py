from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-280, 250)
        self.level = 0
        self.write(f"Level: {self.level}", font=FONT)

    def game_over(self):
        self.goto(-100,0)
        self.write("game Over", font=FONT)

    def levelup(self):
        self.level += 1

    def update(self):
        self.clear()
        self.goto(-280, 250)
        self.write(f"Level: {self.level}", font=FONT)

