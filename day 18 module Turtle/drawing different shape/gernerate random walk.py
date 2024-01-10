# https://docs.python.org/3/library/turtle.html#turtle.colormode
import turtle
from turtle import Turtle, Screen
import random

timmy_turtle = Turtle()
turtle.colormode(255)
direction = [0, 90, 180, 270]
timmy_turtle.pensize(10)
timmy_turtle.speed("fast")


def set_rgb_color():
    """Set color for turtle pen """
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


for _ in range(200):
    timmy_turtle.color(set_rgb_color())
    timmy_turtle.forward(30)
    timmy_turtle.setheading(random.choice(direction))
