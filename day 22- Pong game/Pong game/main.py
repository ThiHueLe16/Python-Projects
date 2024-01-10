from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("DarkSalmon")
screen.setup(width=800, height=600)
screen.title("Pong")

screen.listen()
# draw middle line
draw=Turtle()
draw.color("white")
draw.hideturtle()
draw.shapesize(10)
draw.goto(0,-300)
draw.goto(0, 300)
screen.tracer(0)
# set up paddle and move paddle
r_paddle = Paddle((350, 0), "DarkGreen")
l_paddle =Paddle((-350, 0),"DeepPink")

screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

ball= Ball()
scoreboard=Scoreboard()
game_is_on=True

while game_is_on:
    time.sleep(ball.speed)
    screen.update()
    ball.move()
    # detect ball collision with wall
    if ball.ycor()>280 or ball.ycor() < -280:
        ball.bounce_y()
    # detect ball collision with paddle
    if ball.xcor()>320 and r_paddle.distance(ball)<50:
        ball.bounce_x()
        ball.reset_color(r_paddle.paddle_color)
    if ball.xcor()<-320 and l_paddle.distance(ball)<50:
        ball.bounce_x()
        ball.reset_color(l_paddle.paddle_color)
    # detect when ball goes out of bound, increase speed of ball whenever a player loose
    # right player loose
    if ball.xcor()>380:
        ball.reset_position()
        ball.reset_color(r_paddle.paddle_color)
        ball.increase_speed()
        scoreboard.update_leftscore()
    # left player loose
    if ball.xcor()<-380:
        ball.reset_position()
        ball.reset_color(l_paddle.paddle_color)
        ball.increase_speed()
        scoreboard.update_rightscore()


screen.exitonclick()
