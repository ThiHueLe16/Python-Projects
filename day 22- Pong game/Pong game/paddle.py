from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position, color):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle_color=color
        self.color(color)
        self.penup()
        self.goto(position)

    def go_up(self):
        if self.ycor()<250:
            new_y=self.ycor()+10
            self.goto(self.xcor(), new_y)

    def go_down(self):
        if self.ycor()>-250:
            new_y = self.ycor() - 10
            self.goto(self.xcor(), new_y)
