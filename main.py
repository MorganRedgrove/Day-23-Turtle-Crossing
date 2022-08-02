from random import randint
from threading import Thread
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

def coll_check():
    for car in car_manager.car_list:
        if car.distance(player.position()) < 30:
            scoreboard.gameover()
            return True
        else:
            return False

screen = Screen()
screen.setup(width=600, height=600)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

score = 0

screen.listen()
screen.onkeypress(fun=player.move, key="w")

game_over = False
while not game_over == True:
    time.sleep(0.1 - (score/50))
    screen.update()
    car_manager.gen_car()
    car_manager.move_car()
    game_over = coll_check()
    new_score = score + player.score()
    score = new_score
    scoreboard.score(score)




screen.exitonclick()
