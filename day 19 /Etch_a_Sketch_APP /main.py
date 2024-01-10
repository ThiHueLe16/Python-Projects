from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def turn_right():
    tim.setheading(tim.heading() - 10)


def turn_left():
    tim.setheading(tim.heading() + 10)


def turn_left_forward():
    tim.setheading(tim.heading() + 10)
    tim.forward(10)


def turn_right_backward():
    tim.setheading(tim.heading() - 10)
    tim.backward(10)

def pen_up():
    tim.penup()

def pen_down():
    tim.pendown()

screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(turn_left_forward, "l")
screen.onkey(turn_right_backward, "r")
screen.onkey(pen_up, "u")
screen.onkey(pen_down, "k")
screen.exitonclick()
