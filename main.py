import time
from turtle import Screen

import car_manager
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
scoreboard=Scoreboard()

player = Player()
cars = CarManager()
screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.move()
    if player.ycor() == 270:
        scoreboard.levelup()
        scoreboard.update()
        player.reset()
        cars.movefaster()
    for i in cars.all_cars:
        if player.distance(i.xcor(), i.ycor()) < 20 and (player.ycor() >= i.ycor()-10 or player.ycor() <= i.ycor()+10):
            scoreboard.game_over()
            game_is_on = False



screen.exitonclick()

