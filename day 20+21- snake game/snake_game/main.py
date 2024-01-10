from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

# set up screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
# turn the tracer of screen off and set screen.update() for image animation to refresh the screen
screen.tracer(0)
# initiate snake, food
snake = Snake()
food = Food()
scoreBoard=ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
# set up game
game_is_on = True

while game_is_on:
    screen.update()
    # use time sleep to see the udpate more clearly
    time.sleep(0.1)
    # move snake
    snake.move()

    # detect collision with food
    if snake.head.distance(food)<15:
        food.refresh()
        scoreBoard.increase_score()
        snake.extern()
    # detect collision with wall
    if snake.head.xcor()>280 or  snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        scoreBoard.reset()
        snake.reset()
    # detect collision with tail
    for body in snake.snake_body[1:]:
        if snake.head.distance(body)<10:
            scoreBoard.reset()
            snake.reset()

# for the screen doesnt disappear immediately
screen.exitonclick()
