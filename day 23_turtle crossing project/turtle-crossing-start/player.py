from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape("turtle")
        self.penup()
        self.reset_start_position()
        self.setheading(90)

    def reset_start_position(self):
        self.goto(STARTING_POSITION)

    def go_up(self):
        new_y= self.ycor()+MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def reach_other_side(self):
        if self.ycor()>FINISH_LINE_Y:
            return True
        return False
