#!/usr/bin/python3
"""
start Flask web app
"""

from flask import Flask, render_template
from models import storage, State, City


app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def list_states_and_cities():
    """ display HTML page """
    return render_template('8-cities_by_states.html',
                           state_stor=storage.all(State))


@app.teardown_appcontext
def close_session(exceptions):
    """ remove SQLAlchemy session """
    storage.close()

if __name__ == "__main__":
    app.run('0.0.0.0', port=5000)
