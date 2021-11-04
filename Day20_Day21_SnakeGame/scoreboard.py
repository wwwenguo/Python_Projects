from turtle import Turtle

POSITION = (230, 270)
ALIGN = "center"
FONT = ("Arial", 16, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(POSITION)
        self.score = 0
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}", move=False, align=ALIGN, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", move=False, align=ALIGN, font=FONT)
