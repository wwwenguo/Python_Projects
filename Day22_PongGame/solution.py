from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Pong')
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
# continue move when pressing the keyboard
screen.onkeypress(r_paddle.go_up, 'Up')
screen.onkeypress(r_paddle.go_down, 'Down')
screen.onkeypress(l_paddle.go_up, 'w')
screen.onkeypress(l_paddle.go_down, 's')

is_game_on = True
while is_game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.bounce_y()
    if ball.distance(r_paddle) < 30 and ball.xcor() > 320:
        ball.bounce_x()
        scoreboard.r_increase_score()
    if ball.distance(l_paddle) < 30 and ball.xcor() < -320:
        ball.bounce_x()
        scoreboard.l_increase_score()
    if ball.xcor() > 380:
        ball.reset()
        scoreboard.l_increase_score()
    if ball.xcor() < -380:
        ball.reset()
        scoreboard.r_increase_score()
screen.exitonclick()
