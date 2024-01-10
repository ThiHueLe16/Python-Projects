# This is a sample Python script.

from tkinter import *
from tkinter import ttk, messagebox

window = Tk()
window.title("To do list")
window.geometry("400x650")
window.resizable(False, False)

task_list = []


def openTaskFile():
    try:
        global task_list
        with open("tasklist.txt", "r") as taskFile:
            tasks = taskFile.readlines()
            for task in tasks:
                if task != "\n":
                    task_list.append(task)
                    listbox.insert(END, task)
    except:
        file = open("tasklist.txt", "w")
        file.close()


def addTask():
    task = task_entry.get()
    task_entry.delete(0, END)
    if task:
        with open("tasklist.txt", "a") as taskfile:
            taskfile.write(f"\n{task}")
            task_list.append(task)
            listbox.insert(END, task)


def delete_Task():
    global tasklist
    task = str(listbox.get(ANCHOR))  # ANCHOR MEANS THE SELECTED PART IN LISTBOX
    if task in task_list:
        task_list.remove(task)
        with open("tasklist.txt", "w") as taskfile:
            for task in task_list:
                taskfile.write(task + "\n")
        listbox.delete(ANCHOR)


# icon
Image_icon = PhotoImage(file="task.png")
window.iconphoto(False, Image_icon)

# top bar
# topImage=PhotoImage(file="topbar.png")
top_Image_Label = Label(window, bg="OliveDrab1", height=7)
top_Image_Label.pack(side=TOP, fill=X)

dockImage = PhotoImage(file="dock.png")
dock_Image_label = Label(window, image=dockImage, bg="black", fg="black")
dock_Image_label.place(x=30, y=138)

dockImage1 = PhotoImage(file="dock.png")
dock_Image_label = Label(window, image=dockImage, bg="black", fg="black")
dock_Image_label.place(x=90, y=138)

dockImage2 = PhotoImage(file="dock.png")
dock_Image_label = Label(window, image=dockImage, bg="black", fg="black")
dock_Image_label.place(x=150, y=138)

noteImage = PhotoImage(file="1382267-200.png")
noteImage_label = Label(window, image=noteImage, bg="OliveDrab1")
noteImage_label.place(x=240, y=25)

heading = Label(window, text="To-Do List ", fg="magenta3", font=" arial 30 bold underline ", bg="OliveDrab1")
heading.place(x=70, y=35)

# main
frame = Frame(window, width=400, height=60, bg="white")
frame.place(x=0, y=180)
task = StringVar()
task_entry = Entry(frame, width=25, font="arial 20", bd=0)
task_entry.place(x=10, y=15)
task_entry.focus()

button = Button(frame, text="ADD", font="arial 20 bold", width=6, background="OliveDrab1", fg="black", bd=0,
                command=addTask, activebackground="OliveDrab1")
button.place(x=315, y=15)

# Listbox
frame1 = Frame(window, bd=3, width=7, height=0, bg="#32405b")
frame1.pack(pady=(125, 0))
scrollbar = Scrollbar(frame1, orient='vertical')
scrollbar.pack(side=RIGHT, fill=Y)

listbox = Listbox(frame1, font=("arial", 15), width=80, height=20, bg="DarkOliveGreen1", fg="black", cursor="hand2",
                  selectbackground="black")
listbox.pack(side=LEFT, fill=BOTH, padx=2)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

# DELTE
delete_icon = PhotoImage(file="delete.png")
delete_button = Button(window, text="Delete Task", font="arial ", bd=0, command=delete_Task, bg="black")
delete_button.pack(side=BOTTOM, pady=10)

openTaskFile()

window.mainloop()
