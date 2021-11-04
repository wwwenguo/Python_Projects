from turtle import Screen, Turtle
import time
from car import Car
from player import Player
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor('white')
screen.setup(width=600, height=600)
screen.title('Turtle Crossing Capstone')
screen.tracer(0)

cars = Car()
player = Player()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.go_up, 'Up')

is_game_on = True
while is_game_on:
    time.sleep(0.1)
    screen.update()

    cars.create_car()
    cars.move()

    for car in cars.cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            is_game_on = False

    if player.ycor() > 280:
        scoreboard.win()
        is_game_on = False

screen.exitonclick()
