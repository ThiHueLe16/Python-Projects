# This is a sample Python script.
import tkinter
from _ast import Lambda
from tkinter import *
from tkinter import filedialog
from tkinter import font

window = Tk()
window.title("Text editor")
window.geometry("1200x600")
# Set name for open file
global open_status_name
open_status_name = False
global selected
selected=False
# create main Frame
myframe = Frame(window)
myframe.pack(pady=5)
# create sidescroll
text_scroll = Scrollbar(myframe, orient="vertical")
text_scroll.pack(side=RIGHT, fill='y')
# create text box
mytext = Text(myframe, width=97, height=25, font="arial, 20", selectbackground="yellow", selectforeground="black",
              undo=True, yscrollcommand=text_scroll.set)
mytext.pack()
# config our scrollbar
text_scroll.config(command=mytext.yview())


# create new file
def new_file():
    mytext.delete("1.0", END)  # delete from the first line to the end line
    window.title("new file! ")
    status_bar.config(text="new file.........")


def open_file():
    mytext.delete("1.0", END)
    # grab file name
    text_file = filedialog.askopenfilename(initialdir="", title="Open file", filetypes=(
        ("Text file", "*.txt"), ("HTML FILE", "*.html"), ("Python file", "*.py"), ("all file", "*.*")))
    if text_file:
        global open_status_name
        open_status_name = text_file
    name = text_file
    status_bar.config(text=name)
    window.title(f"{name}- TextPad")
    # open the file
    text_file = open(text_file, "r")
    stuff = text_file.read()
    mytext.insert(END, stuff)
    # close the open file
    text_file.close()


def saveas_file():
    text_file = filedialog.asksaveasfile(defaultextension=".*", initialdir="/Users/thihuele", title="Save File", filetypes=(
        ("Text file", "*.txt"), ("HTML FILE", "*.html"), ("Python file", "*.py"), ("all file", "*.*")))
    if text_file:
        name = text_file
        status_bar.config(text=f"saved {name}")
        # Update status bar
        status_bar.config(text=name)
        window.title(f"Saved {name}- TextPad")
        # save the file
        print(type(text_file))
        #to fix the problem with text io wrapper when open file, using f" " to modify text file name in string
        text_file = open(f"{text_file}", 'w')
        text_file.write(mytext.get(1.0, END))
        text_file.close()


def save_file():
    global open_status_name
    if open_status_name:
        text_file = open(open_status_name, "w")
        text_file.write(mytext.get(1.0, END))
        text_file.close()
        status_bar.config(text=f"saved {open_status_name}")
    else:
        saveas_file()
def cut_text(e):
    global selected
    if mytext.selection_get():
        selected = mytext.selection_get()
        mytext.delete(tkinter.SEL_FIRST, tkinter.SEL_LAST)
def copy_text(e):
    global selected
    if mytext.selection_get():
        selected = mytext.selection_get()
def paste_text(e):
    global selected
    if selected:
        position= mytext.index((INSERT))
        mytext.insert(position, selected)
# create menu bar
menu = Menu(window)
window.config(menu=menu)

file_menu = Menu(menu, tearoff=False)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Save As", command=saveas_file)
file_menu.add_command(label="Exit", command=window.quit)

edit_menu = Menu(menu, tearoff=False)
menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command= lambda:cut_text(FALSE))
edit_menu.add_command(label="Copy", command=lambda: copy_text(FALSE))
edit_menu.add_command(label="Paste ", command=lambda: paste_text(FALSE))

# create status bar
status_bar = Label(myframe, text="Ready............", fg="black", font="ARIAL, 20", anchor=E, bg="white")
status_bar.pack(side=BOTTOM, fill="x", ipady=5)

window.mainloop()
