import turtle, random
from turtle import Turtle, Screen
import colorgram

timmy = Turtle()
turtle.colormode(255)
# extract color from picture
colors = colorgram.extract("hirstpaint.jpg", 30)

# save color as list of tuple
rgb_color = []
for color in colors:
    rgb_color.append((color.rgb.r, color.rgb.g, color.rgb.b))

# make turtle invisible
# timmy.hideturtle()

timmy.setheading(225)
timmy.penup()
timmy.forward(300)
timmy.setheading(0)
number_of_dot=100


for dot_count in range(1, number_of_dot+1):
    print(f'timmy corordinate:({timmy.xcor(), timmy.ycor()}')
    timmy.dot(20, random.choice(rgb_color))
    timmy.forward(50)

    if dot_count%10==0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)

screen=Screen()
screen.exitonclick()