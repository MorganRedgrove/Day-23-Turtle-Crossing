from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("black")
        self.shape("turtle")
        self.setposition(0, -280)
        self.setheading(90)
        self.showturtle()

    def move(self):
        self.forward(10)

    def score(self):
        if self.ycor() > 280:
            self.hideturtle()
            self.setposition(0, -280)
            self.showturtle()
            return 1
        else:
            return 0


