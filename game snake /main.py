# This is a sample Python script.

from tkinter import *
import random

GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 150
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "yellow"
FOOD_COLOR = "red"
BACKGROUND_COLOR = "black"


class Snake:
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinate = []  # position
        self.squares = []  # grapphic

        for i in range(0, BODY_PARTS):
            self.coordinate.append([0, 0])
        for x, y in self.coordinate:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)
            self.squares.append(square)


class Food:
    def __init__(self):
        x = random.randint(0, (GAME_WIDTH / SPACE_SIZE) - 1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE
        print(f"food coordinate: x= {x} and y= {y}")
        self.coordinate = [x, y]
        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")


def next_turn(snake, food):
    x, y = snake.coordinate[0]
    if direction == "up":
        y -= SPACE_SIZE
    if direction == "down":
        y += SPACE_SIZE
    if direction == "right":
        x += SPACE_SIZE
    if direction == "left":
        x -= SPACE_SIZE
    snake.coordinate.insert(0, (x, y))
    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)
    snake.squares.insert(0, square)
    if x == food.coordinate[0] and y == food.coordinate[1]:
        global score
        print("EAT. Iam happy")
        score += 1
        label.config(text="Score:{}".format(score))
        canvas.delete("food")
        food = Food()
    else:
        del snake.coordinate[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]
    if check_collision():
        game_over()
    window.after(SPEED, next_turn, snake, food)


def change_direction(new_direction):
    global direction
    if new_direction == "left":
        if direction != "right":
            direction = new_direction
    if new_direction == "right":
        if direction != "left":
            direction = new_direction
    if new_direction == "up":
        if direction != "down":
            direction = new_direction
    if new_direction == "down":
        if direction != "up":
            direction = new_direction


def check_collision():
    x,y=snake.coordinate[0]
    if x<0 or x>GAME_WIDTH:
        print("GAME OVER")
        return True
    elif y<0 or y>GAME_HEIGHT:
        print("GAME OVER")
        return True
    for body_part in snake.coordinate[1:]:
        if x == body_part[0] and y== body_part[1]:
            print("GAME OVER")
            return True
    return False
def game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2, text="GAME OVER",font=("consolas",70) ,fill="red",tag="game over")


window = Tk()
window.title("Snake game")
window.resizable(False, False)
score = 0
direction = "down"

label = Label(window, text="Score:{}".format(score), font=("arial", 40))

label.pack()
canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

# change whenever the window appear it will be in the middle of the screen
window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))
window.geometry(f"{window_width}x{window_height}+{x}+{y}")
#listen to event outside and react
window.bind('<Left>', lambda event: change_direction("left"))
window.bind("<Right>", lambda event: change_direction("right"))
window.bind("<Up>", lambda event: change_direction("up"))
window.bind("<Down>", lambda event: change_direction("down"))
snake = Snake()
food = Food()

next_turn(snake, food)

window.mainloop()
