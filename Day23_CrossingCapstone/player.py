from turtle import Turtle

MOVE_DISTANCE = 5


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.goto(0, -280)
        self.setheading(90)

    def go_up(self):
        self.forward(MOVE_DISTANCE)
