import turtle, random
from turtle import Turtle, Screen

timmy_turtle = Turtle()
turtle.colormode(255)
timmy_turtle.speed("fastest")


def set_rgb_color():
    """Set color for turtle pen """
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


def draw_spirograph(size_of_gap):
    """draw Sprirograph"""
    for _ in range(int(360 / size_of_gap)):
        timmy_turtle.color(set_rgb_color())
        timmy_turtle.circle(100)
        timmy_turtle.setheading(timmy_turtle.heading() + size_of_gap)


draw_spirograph(3)
screen = Screen()
screen.exitonclick()
