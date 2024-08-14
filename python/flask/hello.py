#!/usr/bin/python3

from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def home_page():
    return f"<h1>This is the home page</h1>"

@app.route('/about')
def about():
    return f"<h2>This is the about page</h2>"

@app.route('/<name>')
def user_page(name):
    return f"This is {escape(name)}'s page"

if __name__ == "__main__":
    app.run(debug=True)
