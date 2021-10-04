from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home_page():
    return render_template('home.html')

# Dynamic Routing


@app.route("/about/<username>")
def about_page(username):
    return f'<h1>this is the about page of {username}</h1>'
