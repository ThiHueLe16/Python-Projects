from _ast import Lambda
from PILLOW import IMAGE

#Calculator tkinter

from tkinter import *

# lable=an area widget that hold text and or an image within a window
window = Tk()  # create instance of window
window.title("Calculator tkinter")
e = Entry(window, width=60, bg="white", fg="black", borderwidth=5 )
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def button_click1():
    current_number = e.get()
    e.delete(0, END)
    e.insert(0, str(current_number) + str(1))


def button_click2():
    current_number = e.get()
    e.delete(0, END)
    e.insert(0, str(current_number) + str(2))


def button_click3():
    current_number = e.get()
    e.delete(0, END)
    e.insert(0, str(current_number) + str(3))


def button_click4():
    current_number = e.get()
    e.delete(0, END)
    e.insert(0, str(current_number) + str(4))


def button_click5():
    current_number = e.get()
    e.delete(0, END)
    e.insert(0, str(current_number) + str(5))


def button_click6():
    current_number = e.get()
    e.delete(0, END)
    e.insert(0, str(current_number) + str(6))


def button_click7():
    current_number = e.get()
    e.delete(0, END)
    e.insert(0, str(current_number) + str(7))


def button_click8():
    current_number = e.get()
    e.delete(0, END)
    e.insert(0, str(current_number) + str(8))


def button_click9():
    current_number = e.get()
    e.delete(0, END)
    e.insert(0, str(current_number) + str(9))


def button_click0():
    current_number = e.get()
    e.delete(0, END)
    e.insert(0, str(current_number) + str(0))


def button_add():
    current_number = e.get()
    e.delete(0, END)
    e.insert(0, str(current_number) + "+")

def button_minus():
    current_number = e.get()
    e.delete(0, END)
    e.insert(0, str(current_number) + "-")
def button_mul():
    current_number = e.get()
    e.delete(0, END)
    e.insert(0, str(current_number) + "*")
def button_div():
    current_number = e.get()
    e.delete(0, END)
    e.insert(0, str(current_number) + "/")

def button_clear():
    current_number = e.get()
    current_number= current_number.rstrip(current_number[-1])
    e.delete(0, END)
    e.insert(0, str(current_number))


def button_equal():
    current_number = e.get()
    result = eval(current_number)
    e.delete(0, END)
    e.insert(0, str(result))



button_1 = Button(window, text="1", padx=70, pady=30, command=button_click1)
button_2 = Button(window, text="2", padx=70, pady=30, command=button_click2)
button_3 = Button(window, text="3", padx=70, pady=30, command=button_click3)
button_4 = Button(window, text="4", padx=70, pady=30, command=button_click4)
button_5 = Button(window, text="5", padx=70, pady=30, command=button_click5)
button_6 = Button(window, text="6", padx=70, pady=30, command=button_click6)
button_7 = Button(window, text="7", padx=70, pady=30, command=button_click7)
button_8 = Button(window, text="8", padx=70, pady=30, command=button_click8)
button_9 = Button(window, text="9", padx=70, pady=30, command=button_click9)
button_0 = Button(window, text="0", padx=70, pady=30, command=button_click0)

button_add = Button(window, text="+", padx=70, pady=30, command=button_add)
button_minus=Button(window, text="-", padx=70, pady=30, command=button_minus)
button_mul=Button(window, text="*", padx=70, pady=30, command=button_mul)
button_div=Button(window, text="/", padx=70, pady=30, command=button_div)

button_equal = Button(window, text="=", padx=260, pady=30, command=button_equal)
button_clear = Button(window, text="Clear", padx=60, pady=30, command=button_clear)
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_add.grid(row=4, column=1)
button_minus.grid(row=4,column=2)

button_clear.grid(row=5, column=0 )
button_mul.grid(row=5,column=1)
button_div.grid(row=5, column=2)

button_equal.grid(row=6, column=0, columnspan=3)

window.mainloop()  # place window on screen +listen to events
