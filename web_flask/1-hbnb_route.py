#!/usr/bin/python3
"""
start Flask web app
"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_flask():
    """ listen on 0.0.0.0:5000 """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ display 'HBNB' """
    return "HBNB"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
