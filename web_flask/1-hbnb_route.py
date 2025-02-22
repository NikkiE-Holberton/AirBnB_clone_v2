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

if __name__ == "__main__":
    app.run(host="0.0.0.0")
