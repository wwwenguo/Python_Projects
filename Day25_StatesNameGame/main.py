import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
answer_list = []

is_game_on = True
while is_game_on:
    answer_state = screen.textinput(title=f"Guess the State, {len(answer_list)}/50",
                                    prompt="What's another state's name?").title()
    state = data[data.state == answer_state]
    if not state.empty:
        cor = (int(state['x']), int(state['y']))
        label = turtle.Turtle()
        label.color('black')
        label.hideturtle()
        label.penup()
        label.goto(cor)
        label.write(f"{answer_state}", move=False, align='center', font=('Arial', 16, 'normal'))
        answer_list.append(answer_state)

    if len(answer_list) == 50:
        is_game_on = False

screen.exitonclick()
