import turtle as t
import random
import colorgram

# tim = t.Turtle()

# # Or defined a function to call it
# n = 3
# while n < 11:
#     x = 0
#     y = 360 / n
#     while x < n:
#         tim.forward(50)
#         tim.right(y)
#         x += 1
#     n += 1

# # create random color
# # set the color mode
# t.colormode(255)
# tim.pensize(5)
# # random color function
#
#
# def random_color():
#     r = random.choice(range(256))
#     g = random.choice(range(256))
#     b = random.choice(range(256))
#     color = (r, g, b)
#     return color
#
# # create Spirograph
#
#
# def draw_spiro(size):
#     for _ in range(int(360 / size)):
#         tim.color(random_color())
#         tim.circle(100)
#         tim.setheading(tim.heading() + size)
#
#
# tim.speed("fastest")
# draw_spiro(5)
#
# colors = colorgram.extract('hirst.jpg', 30)
# color_list = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     color_list.append((r, g, b))
# print(color_list)

color_list = [(222, 163, 66), (19, 45, 86), (136, 61, 84), (176, 61, 44), (126, 40, 61), (22, 86, 60), (59, 48, 37),
              (249, 194, 43), (14, 117, 146), (58, 145, 72), (229, 86, 36), (230, 173, 190), (194, 128, 151),
              (57, 71, 39), (31, 67, 58), (196, 103, 134), (156, 191, 185), (166, 204, 202), (60, 27, 45),
              (145, 165, 181), (7, 79, 111), (36, 45, 98), (170, 202, 204), (73, 152, 86), (114, 43, 36),
              (223, 178, 169)]

paint = t.Turtle()
t.colormode(255)


def draw_dots(size, space, times):
    for _ in range(times):
        paint.dot(size, random.choice(color_list))
        paint.forward(space)


def new_line(times, space):
    paint.backward(times * space)
    paint.left(90)
    paint.forward(space)
    paint.right(90)


n = 5
paint.speed("fastest")
paint.penup()
paint.hideturtle()
paint.setx(- n * 50 / 2)
paint.sety(- n * 50 / 2)
for _ in range(n):
    draw_dots(20, 50, n)
    new_line(n, 50)


screen = t.Screen()
screen.exitonclick()

