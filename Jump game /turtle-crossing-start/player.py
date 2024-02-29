import time
from turtle import Turtle

STARTING_POSITION = (0, -170)
Y_START_BORDER=-170
FINISH_LINE_Y = 180
MOVE_DISTANCE=70
GRAVITY=5
class Player(Turtle):
    def __init__(self,screen):
        super().__init__()
        # self.shapesize(stretch_wid=1.8, stretch_len=1.8, outline=1)
        self.color("white")
        self.shape("circle")
        self.penup()
        self.start_run(screen)
        self.setheading(90)


    def start_run(self, screen ):
        self.goto(-450,-180)
        while(self.xcor()<0):
            print(self.xcor())

            time.sleep(0.1)
            screen.update()
            self.goto(self.xcor()+MOVE_DISTANCE, self.ycor())

    def reset_start_position(self):
        self.goto(STARTING_POSITION)

    def go_up(self):
        print("im hier")

        new_y= self.ycor()+MOVE_DISTANCE
        self.goto(self.xcor(), new_y)


    def go_down(self):
        new_y = self.ycor() - GRAVITY
        if new_y>Y_START_BORDER:
            self.goto(self.xcor(), new_y)
        else:
            self.reset_start_position()


    def reach_other_side(self):
        if self.ycor()>FINISH_LINE_Y:
            return True
        return False


