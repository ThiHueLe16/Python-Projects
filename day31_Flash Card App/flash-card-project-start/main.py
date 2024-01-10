from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
to_learn = {}
try:
    data = pandas.read_csv("./data/to_learn_words.csv")
except FileNotFoundError:
    original = pandas.read_csv("./data/french_words.csv")
    to_learn = original.to_dict(orient="records")
# turn each row into a dict with 2 key word french english
else:
    to_learn = data.to_dict(orient="records")
    print(to_learn)
cur_card = {}


# ---------------------------- read French_words file  ------------------------------- #
def next_card():
    global cur_card, flip_timer
    window.after_cancel(flip_timer)
    canvas_card.itemconfig(language_title, text="French", fill="black")
    cur_card = random.choice(to_learn)
    canvas_card.itemconfig(word, text=cur_card["French"], fill="black")
    canvas_card.itemconfig(photo_image, image=photo_card_front)
    flip_timer = window.after(3000, func=flip_card)


# ---------------------------- FLIP CARDS  ------------------------------- #
def flip_card():
    canvas_card.itemconfig(photo_image, image=photo_card_back)
    canvas_card.itemconfig(language_title, text="English", fill="white")
    canvas_card.itemconfig(word, text=cur_card["English"], fill="white")


# ---------------------------- UPDATE TO_LEARN_WORDS   ------------------------------- #
def known_card():
    to_learn.remove(cur_card)
    data = pandas.DataFrame(to_learn)
    # used index=0 to get rid of the small bug with index, remove index before each row of csv file
    data.to_csv("./data/to_learn_words.csv", index=0)
    next_card()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

canvas_card = Canvas(width=800, height=526)
photo_card_front = PhotoImage(file="./images/card_front.png")
photo_card_back = PhotoImage(file="./images/card_back.png")
photo_image = canvas_card.create_image(400, 263, image=photo_card_front)

language_title = canvas_card.create_text(400, 150, text="", fill="black", font=("Ariel", 40, "bold"))
word = canvas_card.create_text(400, 253, text="", fill="black", font=("Ariel", 40, "bold"))
canvas_card.grid(column=0, row=0, columnspan=2)
canvas_card.config(bg=BACKGROUND_COLOR, highlightthickness=0)
unknown_image = PhotoImage(file="./images/wrong.png")
unknown_button = Button(image=unknown_image, highlightthickness=0, command=next_card)
known_image = PhotoImage(file="./images/right.png")
known_button = Button(image=known_image, highlightthickness=0, command=known_card)
unknown_button.grid(column=0, row=1)
unknown_button.config(highlightthickness=0)
known_button.grid(column=1, row=1)


next_card()

window.mainloop()
