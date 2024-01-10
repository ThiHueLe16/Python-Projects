# This is a sample Python script.

from tkinter import *
from tkinter import ttk, messagebox

import googletrans
from googletrans import Translator
import textblob  # for translate

window = Tk()
window.title("Translator")
window.geometry("1080x400")
window.resizable(False, False)
window.configure(bg="white")


def label_change():
    c1 = combo1.get()
    c2 = combo2.get()
    label1.configure(text=c1)
    label2.configure(text=c2)
    window.after(10, label_change)  # need this line to change the text in text box


def translate_func():
    text2.delete(1.0, END)
    try:
        text = text1.get(1.0, END)
        # need to get the key(not the value of dictionary language in conbobox to use the translate function)
        # grab the key from 2 combobox
        for key, value in googletrans.LANGUAGES.items():
            if value == combo1.get():
                from_language_key = key
                print(str(from_language_key))
        for key, value in googletrans.LANGUAGES.items():
            if value == combo2.get():
                to_language_key = key
                print(str(to_language_key))
        # turn original text into textblob
        print(str(text1.get(1.0,END)))
        word = textblob.TextBlob(text1.get(1.0, END))
        # translate text
        words = word.translate( to=to_language_key, from_lang=from_language_key)
        # output
        text2.insert(1.0, words)
    except Exception as e:
        messagebox.showerror("Translator", e)


# icom
image_icon = PhotoImage(file="Google_Translate_logo.svg.png")
window.iconphoto(False, image_icon)

language = googletrans.LANGUAGES
languageV = list(language.values())
# langl=languageV.

combo1 = ttk.Combobox(window, values=languageV, font="Roboto 14", state="r", postcommand=label_change)
combo1.place(x=110, y=20)
combo1.set("ENGLISH")

label1 = Label(window, text="English", font="arial 30 bold", bg="white", width=18, bd=5, fg="black", relief=GROOVE)
label1.place(x=10, y=50)

combo2 = ttk.Combobox(window, values=languageV, font="Roboto 14", state="r", postcommand=label_change)
combo2.place(x=730, y=20)
combo2.set("SELECT")

label2 = Label(window, text="", font="arial 30 bold", bg="white", width=18, bd=5, fg="black", relief=GROOVE)
label2.place(x=620, y=50)

# 1. frame
f = Frame(window, bg="black", bd=5)
f.place(x=10, y=118, width=440, height=210)

text1 = Text(f, font="Roboto 20", bg="white", fg="black", relief=GROOVE, wrap=WORD)
text1.place(x=0, y=0, width=430, height=200)
scrollbar1 = Scrollbar(f)
scrollbar1.pack(side="right", fill="y")
scrollbar1.configure(command=text1.yview())
text1.configure(yscrollcommand=scrollbar1.set)
# 2. frame
f2 = Frame(window, bg="black", bd=5)
f2.place(x=620, y=118, width=440, height=210)

text2 = Text(f2, font="Roboto 20", bg="white", fg="black", relief=GROOVE, wrap=WORD)
text2.place(x=0, y=0, width=430, height=200)
scrollbar2 = Scrollbar(f2)
scrollbar2.pack(side="right", fill="y")
scrollbar1.configure(command=text2.yview())
text1.configure(yscrollcommand=scrollbar2.set)

# 3. translate button
translate_button = Button(window, text="TRANSLATE", font=("arial", 15), activebackground="white", cursor="hand2", bd=1,
                          width=10, height=2, bg="black", fg="black", command=translate_func)
translate_button.place(x=476, y=250)

label_change()

window.mainloop()
