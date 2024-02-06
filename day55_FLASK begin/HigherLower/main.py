from flask import Flask
import random

app = Flask(__name__)


@app.route("/")
def guess_number():
    return "<h1> Guess a number between 0 and 9</h1><img " \
           "src='https://media.giphy.com/media/v1" \
           ".Y2lkPTc5MGI3NjExMzBqandoemMwdXZ5eGN3ZW9oZDh4Zm0xcm9pajh4aHFkc3lubTdrcCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/sJNKngRsekXnLlcJDT/giphy.gif'> "


guess_number = random.randint(0, 9)


@app.route("/<int:number>")
def check_number(number):
    if number < guess_number:
        return "<h1 style='color: purple'> Number is too low </h1><img " \
               "src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/> "
    elif number > guess_number:
        return "<h1 style='color: red'> Number is too high. Try again </h1><img " \
               "src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/> "
    else:
        return "<h1 style='color: green'> You are right </h1> <img " \
               "src='https://media.giphy.com/media/v1" \
               ".Y2lkPTc5MGI3NjExcHFtZTZjOWVldml4djJ6cGQ1MXpsZDFpM3Z5N2RzNGVtM2I0Nmc0bCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/IzXiddo2twMmdmU8Lv/giphy.gif'/> "


if __name__ == "__main__":
    app.run(debug=True)
