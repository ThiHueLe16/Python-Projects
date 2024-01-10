from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.leftscore=0
        self.rightscore=0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(f"{self.leftscore}",align="Center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(f"{self.rightscore}", align="Center", font=("Courier", 80, "normal"))

    def update_leftscore(self):
        self.leftscore+=1
        self.update_score()

    def update_rightscore(self):
        self.rightscore+=1
        self.update_score()
