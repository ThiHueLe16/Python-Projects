from turtle import Turtle, Screen
import random
is_race_on=False
screen = Screen()
screen.setup(width=600, height=600)
color = ["red", "orange","pink", "green", "blue", "purple"]
user_guess=""
while user_guess not in color :
    user_guess = screen.textinput(title="Make your guess:", prompt="Which turtle(red,orange,pink, green, blue, purple) "
                                                               "is going to win?")
turtles = []

ycor = [-70, -40, -10, 20, 50, 80]
# initiate the turtles
for i in range(6):
    turtle = Turtle(shape="turtle")
    turtle.color(color[i])
    turtle.penup()
    turtle.goto(x=-230,y=ycor[i] )
    turtles.append(turtle)

# make the turtle to start moving randomly
if user_guess:
    is_race_on=True

while is_race_on:
    for turtle in turtles:

        if turtle.xcor()>230:
            is_race_on=False
            for t in turtles:
                t.hideturtle()
            if turtle.pencolor()== user_guess:
                turtle.write(arg="You Win",align="center", font=("Cooper Black", 25, "italic"))
            else:
                turtle.write(arg="You Loose",align="center", font=("Cooper Black", 25, "italic"))
        turtle.forward(random.randint(0, 10))


screen.exitonclick()
