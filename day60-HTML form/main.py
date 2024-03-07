from flask import Flask
from flask import render_template, request
import requests

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route("/login", methods=["POST"])
def receive_data():
    # use the name attribute in <input ....> to get what the user type in
    name=request.form["name"]
    password=request.form["password"]
    return f"<h1> Name:{name} Password:{password}"

if __name__ == "__main__":
    app.run(debug=True)

