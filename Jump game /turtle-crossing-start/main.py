import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=1000, height=400)
screen.bgcolor("black")
screen.tracer(0)

player=Player(screen)
car_manager=CarManager()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")
screen.onkey(player.go_down, "Down")
game_is_on = True
while game_is_on:
    time.sleep(0.04)
    screen.update()
    player.go_down()
    car_manager.create_car()
    car_manager.mov_car()
    # detect collision of turtle with car
    for car in car_manager.cars:
        if car.distance(player) < 20:
            game_is_on=False
            scoreboard.game_over()
    # detect when player reach the other side
        if player.reach_other_side():
            player.reset_start_position()
            scoreboard.increase_level()
            car_manager.increase_speed()

screen.exitonclick()
