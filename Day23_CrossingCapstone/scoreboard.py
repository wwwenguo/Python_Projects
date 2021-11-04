from turtle import Turtle

POSITION = (0, 270)
ALIGN = "center"
FONT = ("Arial", 16, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(POSITION)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", move=False, align=ALIGN, font=FONT)

    def win(self):
        self.goto(0, 0)
        self.write(f"Win!", move=False, align=ALIGN, font=FONT)