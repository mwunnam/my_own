#!/usr/bin/python3
from flask import Flask, render_template


app = Flask(__name__)


posts = [
    {
        'author': 'corey Schafer',
        'title': 'Love at first site',
        'content': 'First post content',
        'date_posted': 'March 20, 2024'
    },
    {   'author': 'Micheal Wunnam',
        'title': 'Keep going',
        'content': 'Second post content',
        'date_posted': 'April 20, 2024'
    }
]

aside = [
    {
        'author': 'corey Schafer',
        'title': 'Love at first site',
        'content': 'First post content',
        'date_posted': 'March 20, 2024'
    },
    {   'author': 'Micheal Wunnam',
        'title': 'Keep going',
        'content': 'Second post content',
        'date_posted': 'April 20, 2024'
    }
]



@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/aside')
def aside():
    return render_template('aside.html', posts=posts)


if __name__ == "__main__":
    app.run(debug=True)
