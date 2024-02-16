from flask import Flask, render_template
import requests

app = Flask(__name__)

URL_BLOG_CONTENT="https://api.npoint.io/c790b4d5cab58020d391"
response = requests.get(URL_BLOG_CONTENT)
blogs = response.json()


@app.route('/')
def home():
    print(blogs)
    return render_template("index.html", blogs=blogs)


@app.route('/post/<int:id>')
def show_post(id):
    return render_template("post.html", blog=blogs[id - 1])


if __name__ == "__main__":
    app.run(debug=True)
