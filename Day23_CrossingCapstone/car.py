from turtle import Turtle
import random

COLORS = ['red', 'blue', 'green', 'orange', 'yellow', 'purple', 'black']
MOVE_DISTANCE = 5


class Car:
    def __init__(self):
        self.cars = []

    def create_car(self):
        random_choice = random.randint(1, 5)
        if random_choice == 1:
            car = Turtle()
            car.penup()
            car.shape('square')
            car.shapesize(stretch_len=2, stretch_wid=1)
            car.color(random.choice(COLORS))
            y = random.randint(-250, 250)
            car.goto(300, y)
            self.cars.append(car)

    def move(self):
        for car in self.cars:
            car.backward(MOVE_DISTANCE)