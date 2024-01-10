# https://docs.python.org/3/library/turtle.html#turtle.colormode
import turtle
from turtle import Turtle, Screen
import random
timmy_turtle = Turtle()
timmy_turtle.pensize(5)
timmy_turtle.speed(5)
turtle.colormode(255)

def set_rgb_color():
    """Set color for turtle pen """
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


def draw_shape(num_side):
    """ draw shape for each number of side """
    angle = 360 / num_side
    for _ in range(num_side):
        timmy_turtle.forward(100)
        timmy_turtle.right(angle)


for shape_side_n in range(3, 11):
    timmy_turtle.color(set_rgb_color())
    draw_shape(shape_side_n)

screen=Screen()
screen.exitonclick()