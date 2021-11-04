from turtle import Turtle

RIGHT_POSITIONS = [(350, 40), (350, 20), (350, 0), (350, -20), (350, -40)]
LEFT_POSITIONS = [(-350, 40), (-350, 20), (-350, 0), (-350, -20), (-350, -40)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270


class Pong:
    def __init__(self):
        self.segments = []
        self.create_pong(RIGHT_POSITIONS)
        # self.create_pong(LEFT_POSITIONS)
        self.seg = self.segments

    def create_pong(self, positions):
        for position in positions:
            self.add_segment(position)

    def add_segment(self, position):
        t = Turtle(shape="square")
        t.color("white")
        t.penup()
        t.speed("fastest")
        t.goto(position)
        self.segments.append(t)

    def move(self, direction):
        if direction == 'down':
            self.seg = self.segments[::-1]
            self.seg[0].setheading(DOWN)
        elif direction == 'up':
            self.seg = self.segments
            self.seg[0].setheading(UP)
        for idx in range(len(self.seg) - 1, 0, -1):
            x = self.seg[idx - 1].xcor()
            y = self.seg[idx - 1].ycor()
            self.seg[idx].goto(x, y)

        self.seg[0].forward(MOVE_DISTANCE)

    def up(self):
        self.move('up')

    def down(self):
        self.move('down')

