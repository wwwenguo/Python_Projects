from turtle import Turtle

POSITIONS = [(20, 0), (0, 0), (-20, 0)]
MOVE_DISTANCE = 20
LEFT = 180
RIGHT = 0
UP = 90
DOWN = 270


class Snake:
    # define the objects being created when this class is called and initialized
    def __init__(self):
        self.segments = []
        self.create_snake()  # When the Snake class is called, generated three snake segments
        self.head = self.segments[0]

    def create_snake(self):
        for position in POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        t = Turtle(shape="square")
        t.color("white")
        t.penup()
        t.speed("fastest")
        t.goto(position)
        self.segments.append(t)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):  # This is a move method for the Snake class
        for idx in range(len(self.segments) - 1, 0, -1):
            x = self.segments[idx - 1].xcor()
            y = self.segments[idx - 1].ycor()
            self.segments[idx].goto(x, y)

        self.segments[0].forward(MOVE_DISTANCE)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
            # self.move()

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
            # self.move()

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
            # self.move()

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
            # self.move()
