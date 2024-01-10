import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

turn = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global turn
    global timer
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    check_marks.config(text="")
    turn = 0
    title_label.config(text="Timer")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global turn
    turn += 1
    work_in_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if turn % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="lONG BREAK", fg=PINK)
    elif turn % 2 == 1:
        count_down(work_in_sec)
        title_label.config(text="WORK", fg=GREEN)

    else:
        count_down(short_break_sec)
        title_label.config(text="SHORT BREAK", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global turn
    global timer
    minusleft = count // 60
    secondleft = count - minusleft * 60
    # dynamic typing
    if secondleft < 10:
        secondleft = f'0{secondleft}'

    canvas.itemconfig(timer_text, text=f'{minusleft}:{secondleft}')
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_section = math.floor(turn / 2)
        for _ in range(work_section):
            mark += "☑️"
        check_marks.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=200, pady=50, bg=YELLOW)
title_label = Label(text="TIMER", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
title_label.grid(row=0, column=1)
canvas = Canvas(width=200, height=233, bg=YELLOW, highlightthickness=0)

photoimage = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=photoimage)

timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)


start_button = Button(text="Start", font=(FONT_NAME, 14), highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)
reset_button = Button(text="Reset", font=(FONT_NAME, 14), highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)
check_marks = Label(text="", fg=GREEN, bg=YELLOW)
check_marks.grid(row=2, column=1)
window.mainloop()
