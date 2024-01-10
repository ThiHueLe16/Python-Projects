from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level=0
        self.goto(x=-240, y=260)
        self.update_level()

    def update_level(self):
        self.clear()
        self.write(f"Level:{self.level}", align="Center", font=FONT)

    def increase_level(self):
        self.level+=1
        self.update_level()

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align="Center", font=FONT)