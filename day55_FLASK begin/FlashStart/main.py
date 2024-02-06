from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper_func():
        return f"<b>{function()}<b/>"
    return wrapper_func


def make_underline(function):
    def wrapper_func():
        return f"<u>{function()}<u/>"
    return wrapper_func


@app.route("/")
@make_bold
@make_underline
def hello_world():
    return "<p>Hello, World!</p>"





if __name__ == "__main__":
    app.run(debug=True)
