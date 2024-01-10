START_POSIYION = [(0,0), (-20,0), (-40, 0)]
MOVE_DISTANCE = 20
UP, DOWN, LEFT, RIGHT = 90, 270, 180, 0
from turtle import Turtle


class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_body()
        self.head = self.snake_body[0]

    def create_body(self):
        for pos in START_POSIYION:
            self.add_body(pos)

    def add_body(self, position):
        b = Turtle(shape="square")
        b.color("white")
        b.penup()
        b.goto(position)
        self.snake_body.append(b)

    def extern(self):
        self.add_body(self.snake_body[-1].position())

    # move snake
    def move(self):
        for body_num in range(len(self.snake_body)-1, 0, -1):
            next_pos = (self.snake_body[body_num - 1].xcor(), self.snake_body[body_num - 1].ycor())
            self.snake_body[body_num].goto(next_pos)
        self.snake_body[0].forward(MOVE_DISTANCE)

    # change snake direction
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset(self):
        for body in self.snake_body:
            body.goto(1000,1000)
        self.snake_body.clear()
        self.create_body()
        self.head=self.snake_body[0]