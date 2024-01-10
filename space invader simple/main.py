# This is a sample Python script.

# This is a sample Python script.
import time
from tkinter import *
import random

GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 1600
SPACE_SIZE = 50
BODY_PARTS = 3
SPACEINVADER_COLOR = "yellow"
ENEMY_COLOR = "red"
BACKGROUND_COLOR = "black"


class Space_Invader:
    def __init__(self):
        self.live_number = 3
        self.coordinate = []  # position
        self.squares = []  # grapphic
        self.bullet_usage = []  # bullet already used
        self.coordinate.append(
            [(int(GAME_WIDTH / SPACE_SIZE) - 1) * SPACE_SIZE, (int(GAME_HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE])
        for x, y in self.coordinate:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SPACEINVADER_COLOR)
            self.squares.append(square)


class Enemy:
    def __init__(self):
        self.coordinate_ememies = []
        self.ovals = []
        for j in range(0, 3):
            for i in range(0, int(GAME_WIDTH / SPACE_SIZE)):
                self.coordinate_ememies.append([i, j])
        for x, y in self.coordinate_ememies:
            oval = canvas.create_oval(x * SPACE_SIZE, y * SPACE_SIZE, x * SPACE_SIZE + SPACE_SIZE,
                                      y * SPACE_SIZE + SPACE_SIZE, fill=ENEMY_COLOR)
            self.ovals.append(oval)


class Bullet:
    global spaceinvader
    global bullet_use_number

    def __init__(self, x, y):
        self.coordinate_bullet = []
        self.lines = []
        self.x = x
        self.y = y
        bullet_line = canvas.create_line(x + int(SPACE_SIZE / 2), y, x + int(SPACE_SIZE / 2),
                                         y - SPACE_SIZE, fill="white", width="10")

        self.coordinate_bullet.append([self.x, self.y])
        self.lines.append(bullet_line)
        spaceinvader.bullet_usage.append(self)


def next_turn(snake, food):
    global direction
    x, y = spaceinvader.coordinate[0]

    if direction == "left":
        if x != 0:
            x -= 1 * SPACE_SIZE
            direction = ""
    if direction == "right":
        if x != GAME_WIDTH - SPACE_SIZE:
            x += 1 * SPACE_SIZE
            direction = ""

    spaceinvader.coordinate.insert(0, [x, y])
    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SPACEINVADER_COLOR)
    spaceinvader.squares.insert(0, square)
    canvas.delete(spaceinvader.squares[-1])
    del spaceinvader.coordinate[-1]
    del spaceinvader.squares[-1]
    if spaceinvader.bullet_usage:
        for bullet_use in spaceinvader.bullet_usage:
            x = bullet_use.x
            y = bullet_use.y
            y -= SPACE_SIZE
            bullet_use.y = y
            bullet_line_new = canvas.create_line(x + int(SPACE_SIZE / 2), y, x + int(SPACE_SIZE / 2),
                                                 y - SPACE_SIZE , fill="white", width="10")
            bullet_use.coordinate_bullet.append([x, y])
            bullet_use.lines.insert(0, bullet_line_new)
            canvas.delete(bullet_use.lines[-1])
            del bullet_use.coordinate_bullet[-1]
            del bullet_use.lines[-1]



    if check_collision():
        game_over()
    window.after(SPEED, next_turn, snake, food)


def change_direction(new_direction):
    global direction
    global spaceinvader
    if new_direction == "left":
        direction = new_direction

    if new_direction == "right":
        direction = new_direction

    if new_direction == "up":
        direction = new_direction

    if new_direction == "down":
        direction = new_direction


def attack():
    global spaceinvader
    print("ATTACK!")
    x, y = spaceinvader.coordinate[0]
    new_bullet = Bullet(x, y)
    spaceinvader.bullet_usage.append(new_bullet)

a=0
def check_collision():
    global a
    global delete_enemy_index
    for bullet_use in spaceinvader.bullet_usage:
        for i in range(len(enemies.coordinate_ememies)):
            if i in delete_enemy_index:
                print("am hier")
                pass
            else:
                print(f"{i}      {a}")
                enemies.coordinate_ememies[i][1]
                if bullet_use.x == enemies.coordinate_ememies[i][0] * SPACE_SIZE and bullet_use.y == \
                        enemies.coordinate_ememies[i][1] * SPACE_SIZE:
                    print("i will delete "+str(i))
                    # delete enemy
                    delete_enemy_index.append(i)
                    canvas.delete(enemies.ovals[i])
                    enemies.ovals.remove(enemies.ovals[i])
                    enemies.coordinate_ememies.remove(enemies.coordinate_ememies[i])
                    # delete bullet
                    canvas.delete(bullet_use.lines)
                    del bullet_use.lines[0]
                    spaceinvader.bullet_usage.remove(bullet_use)
                    break
        a+=1

    return False


def game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height() / 2, text="GAME OVER", font=("consolas", 70),
                       fill="red", tag="game over")


window = Tk()
window.title("Space Invader game")
window.resizable(False, False)
score = 0
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
# listen to event outside and react
window.bind('<Left>', lambda event: change_direction("left"))
window.bind("<Right>", lambda event: change_direction("right"))
# window.bind("<Up>", lambda event: change_direction("up"))
# window.bind("<Down>", lambda event: change_direction("down"))
window.bind("<Down>", lambda event: attack())
window.bind("<Up>", lambda event: attack())

direction = ""
bullet_use_number = 0
spaceinvader = Space_Invader()
enemies = Enemy()
# bullets=Bullet()
delete_enemy_index = []
next_turn(spaceinvader, enemies)

window.mainloop()
