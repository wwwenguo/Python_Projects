from turtle import Turtle, Screen
from pong import Pong
import time

s = Screen()
s.setup(800, 600)
s.bgcolor("black")
s.title("Pong Game")

s.tracer(0)

pong = Pong()

s.listen()
s.onkey(pong.up, "Up")
s.onkey(pong.down, "Down")

is_game_on = True
while is_game_on:
    s.update()
    time.sleep(0.1)

s.exitonclick()
