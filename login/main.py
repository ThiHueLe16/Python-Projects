# This is a sample Python script.
from tkinter import *
from tkinter import messagebox
window = Tk()
window.title("Login")
label = Label(window, text="Login")
label.place(x=40, y=10)
username= Label(window, text= "Username:")
password=Label(window, text= "Password: ")
username.place(x=40, y=40)
password.place(x=40, y=70)
entry_username = Entry(window)
entry_password= Entry(window)
entry_username.place(x=150, y=40)
entry_password.place(x=150,y=70)

def login():
    if entry_username.get()=="" and entry_password.get() == "":
        messagebox.showinfo("", "No blank is acceptable! ")
    elif str(entry_username.get()) =="huele" and entry_password.get() == "16011999":
        messagebox.showinfo("", "Login success!")
    else:
        messagebox.showinfo("","Login Failed!")


login_button= Button(window, text="Login", command=login, bd =5)
login_button.place(x=70,y=100)
window.mainloop()
