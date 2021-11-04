from turtle import Turtle

MOVE_DISTANCE = 20


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        # self.paddle = Turtle()  # No need of this line
        self.shape('square')  # Hit 'ctrl + R' to replace paddle to self
        self.color('white')
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), new_y)
