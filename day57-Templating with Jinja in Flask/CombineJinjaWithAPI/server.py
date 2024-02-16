from flask import Flask, render_template
from markupsafe import escape
import requests

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html" )

@app.route('/guess/<name>')
def guess(name):
    gender_response=requests.get(f"https://api.genderize.io?name={name}")
    gender_response.raise_for_status()
    gender_data=gender_response.json()
    gender=gender_data["gender"]
    print(gender_data)
    age_response=requests.get(f"https://api.agify.io?name={name}")
    age_response.raise_for_status()
    age_data=age_response.json()
    print(age_data)
    age=age_data["age"]
    return render_template("guess.html", person_name=name, gender=gender, age=age  )
app.run(debug=True)