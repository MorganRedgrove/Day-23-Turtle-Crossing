from turtle import Turtle
from random import randint
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager(Turtle):
    def __init__(self):
        self.car_list = []

    def gen_car(self):
        random_chance = randint(1,6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.penup()
            new_car.hideturtle()
            new_car.color(COLORS[randint(0, 5)])
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.setposition(300, (-200 + (25* (randint(1, 18)))))
            new_car.showturtle()
            self.car_list.append(new_car)

    def move_car(self):
        for car in self.car_list:
            car.backward(STARTING_MOVE_DISTANCE)


