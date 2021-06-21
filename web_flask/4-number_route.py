#!/usr/bin/python3
"""Script that starts a Flask web application"""

from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello():
    return 'Hello HBNB!'


@app.route('/hbnb')
def display():
    return 'HBNB'


@app.route('/c/<text>')
def cfile(text):
    return 'C {}'.format(text.replace("_", " "))


@app.route('/python/')
@app.route('/python/<text>')
def pyfile(text="is cool"):
    return 'Python {}'.format(text.replace("_", " "))


@app.route('/number/<int:n>')
def nmbfile(n):
    return '{} is a number'.format(n)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
