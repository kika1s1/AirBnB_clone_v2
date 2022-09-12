#!/usr/bin/python3
"""
start Flask web app
"""

from flask import Flask, render_template
from models import storage, State, City


app = Flask(__name__)


@app.route('/states/', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states_list(id=None):
    """ display HTML page """
    return render_template('9-states.html',
                           states=storage.all("State"), id=id)


@app.teardown_appcontext
def close_session(exceptions):
    """ remove SQLAlchemy session """
    storage.close()

if __name__ == "__main__":
    app.run('0.0.0.0', port=5000)
