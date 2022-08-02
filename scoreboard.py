from turtle import Turtle

FONT = ("Courier", 30, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()

    def gameover(self):
        self.color("red")
        self.setposition(0, 0)
        self.write("GAME OVER!", align="center", font=FONT)

    def score(self, score):
        self.color("black")
        self.setposition(-280, 250)
        self.write(score, font=FONT)

