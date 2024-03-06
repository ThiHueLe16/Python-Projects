from flask import Flask
from flask import render_template
import requests
app = Flask(__name__)
print(__name__)

posts= requests.get("https://api.npoint.io/674f5423f73deab1e9a7").json()
print(posts)
@app.route('/')
def home():
    return render_template('index.html', allpost=posts)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/post/<int:index>')
def show_post(index):
    requestesPost= None
    for blog in posts:
        if blog["id"]==index:
            requestesPost= blog

    return render_template('post.html', post=requestesPost )

if __name__ == "__main__":
    app.run(debug=True)
