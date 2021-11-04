import turtle

t = turtle.Turtle()
s = turtle.Screen()


def forwards():
    t.forward(25)


def backwards():
    t.backward(25)


def counter_clockwise():
    t.setheading(t.heading() + 10)


def clockwise():
    t.setheading(t.heading() - 10)


def clean():
    t.clear()
    t.penup()
    t.home()


s.listen()
s.onkey(forwards, "w")
s.onkey(backwards, "s")
s.onkey(clockwise, "d")
s.onkey(counter_clockwise, "a")
s.onkey(clean, "c")
s.exitonclick()
