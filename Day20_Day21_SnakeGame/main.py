from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

s = Screen()
s.setup(600, 600)
s.bgcolor("black")
s.title("Snake Game")
s.tracer(0)  # Turn off the tracer

# # create a snake body
# for index in range(0, 3):
#     t = Turtle(shape="square")
#     t.color("white")
#     t.penup()
#     t.goto(positions[index])
#     snakes.append(t)

# Call Snake class
snake = Snake()
food = Food()

s.listen()
s.onkey(snake.up, "Up")
s.onkey(snake.down, "Down")
s.onkey(snake.right, "Right")
s.onkey(snake.left, "Left")

# keys = pygame.key.get_pressed()  # keys pressed
# if keys[pygame.K_LEFT]:
#     print('left')
#     snake.left()
# if keys[pygame.K_RIGHT]:
#     print('right')
#     snake.right()
# if keys[pygame.K_UP]:
#     print('up')
#     snake.up()
# if keys[pygame.K_DOWN]:
#     print('down')
#     snake.down()


# score = 0
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    s.update()  # Show the current status of the screen
    time.sleep(0.1)  # Don't show the move motions below, want to update the screen after all three turtles moved.
    # for snake in snakes:
    #     snake.forward(20)
    # Let the second snake seg goes to the first snake seg's place
    # for idx in range(len(snakes) - 1, 0, -1):
    #     x = snakes[idx - 1].xcor()
    #     y = snakes[idx - 1].ycor()
    #     snakes[idx].goto(x, y)
    #
    # snakes[0].left(90)
    # snakes[0].forward(20)
    snake.move()
    if snake.head.distance(food) < 15:
        food.new_position()
        snake.extend()
        # score += 10
        scoreboard.increase_score()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        scoreboard.game_over()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

s.exitonclick()

# def go_forward(snakes_list):
#     for idx in range(len(snakes_list) - 1, 0, -1):
#         x = snakes_list[idx - 1].xcor()
#         y = snakes_list[idx - 1].ycor()
#         snakes_list[idx].goto(x, y)
#
#
# def turn_left(snakes_list):
#     for x in snakes_list:
#         x.setheading(270)
#         x.forward(10)
#
#
# def turn_right(snakes_list):
#     for x in snakes_list:
#         x.setheading(90)
#
#
# is_game_on = True
# while is_game_on:
#     s.update()
#     time.sleep(0.1)
#     go_forward(snakes)

