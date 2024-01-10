from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    # use pyperclip to auto the save the generator password and we can use cmd+v to pass new password in any space
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_input = website_entry.get()
    username_input = email_username_entry.get()
    pass_input = password_entry.get()
    if not website_input or not username_input or not pass_input:
        messagebox.showinfo(message="Please dont let any of the information field empty")
    else:
        answer = messagebox.askyesno(title=website_input,
                                     message=f"There are the detailed enter for website {website_input}: \n Email:{username_input}\n Password: {pass_input}\n")
        if answer:
            new_data = {
                website_input: {
                    "email": username_input,
                    "password": pass_input
                }
            }
            try:
                with open("data.json", "r") as data_file:
                    # Reading old data
                    # have to handle the following error incase the file is exist but empty
                    try:
                        data = json.load(data_file)
                    except json.JSONDecodeError:
                        data=dict()
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                # Updating old data with new data
                data.update(new_data)

                with open("data.json", "w") as data_file:
                    # Saving updated data
                    json.dump(data, data_file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- SEARCH WEBSITE ------------------------------- #
def search_website():
    searchwebsite = website_entry.get()
    try:
        with open("data.json") as data_file:
            # have to handle the following error incase the file is exist but empty
            try:
                data = json.load(data_file)
            except json.JSONDecodeError:
                data=dict()
    except FileNotFoundError:
        messagebox.showinfo("There is no infomation for given website")
    else:

        if searchwebsite in data:
            web_username = data[searchwebsite]["email"]
            web_password = data[searchwebsite]["password"]
            messagebox.showinfo(title=searchwebsite, message=f"Email:{web_username}\nPassword: {web_password} ")
        else:
            messagebox.showinfo("There is no infomation for given website")


# use dialog textbox , messagebox increase interaction with user
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=20, pady=20, bg="white")
canvas = Canvas(height=200, width=200, bg="white", highlightthickness=0)
photoImage = PhotoImage(file="logo.png", width=200, height=200)
canvas.create_image(100, 100, image=photoImage)
canvas.grid(row=0, column=1)
website = Label(text="Website:", bg="white", fg="black")
website_entry = Entry(width=21, bg="white", highlightthickness=0, fg="black")
website.grid(row=1, column=0)
website_entry.focus()
website_entry.grid(row=1, column=1)

search_button = Button(text="Search", bg="white", fg="black", highlightthickness=0, width=13, command=search_website)
search_button.grid( row=1, column=2)
email_username = Label(text="Email/Username:", bg="white", fg="black")
email_username_entry = Entry(width=35, bg="white", highlightthickness=0, fg="black")
email_username_entry.insert(0, "huethangnhat@gmail.com")
email_username.grid(row=2, column=0)
email_username_entry.grid(row=2, column=1, columnspan=2)
password_label = Label(text="Password:", bg="white", fg="black")
password_label.grid(row=3, column=0)
password_entry = Entry(width=18, bg="white", highlightthickness=0, fg="black")
password_entry.grid(row=3, column=1)
generatePassword = Button(text="Generate Password", bg="white", highlightthickness=0, width=13,
                          command=generate_password)
generatePassword.grid(row=3, column=2)
addButton = Button(text="add", bg="white", highlightthickness=0, width=34, command=save)
addButton.grid(row=4, column=1, columnspan=2)

window.mainloop()
