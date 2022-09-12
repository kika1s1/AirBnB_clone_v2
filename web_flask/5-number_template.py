#!/usr/bin/python3
"""
start Flask web app
"""
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_flask():
    """ listen on 0.0.0.0:5000 """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ display 'HBNB' """
    return "HBNB!"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """ display C <text> """
    return "C {}".format(text.replace('_', ' '))


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is cool"):
    """ displays Python <text> """
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>')
def is_number(n):
    """ display number "n" if int """
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>')
def number_template(n):
    """ display number inside <body> of HTML page """
    return render_template("5-number.html", n=n)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
