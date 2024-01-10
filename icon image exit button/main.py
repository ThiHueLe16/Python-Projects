# This is a sample Python script.

from tkinter import *
from PILLOW import ImageTK, Image
window = Tk()
window.title("huele")
myimage= ImageTK.PhotoImage(Image.open(""))
button_quit= Button(window, text="exit programm", command= window.quit)
button_quit.pack()
window.mainloop()
