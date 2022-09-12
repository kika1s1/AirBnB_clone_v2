#!/usr/bin/python3
'''flask for the website'''

from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def filters():
    """ display HTML page """
    state_stor = storage.all("State")
    amenity_stor = storage.all("Amenity")
    return render_template('10-hbnb_filters',
                           states=states, amenities=amenities)


@app.teardown_appcontext
def close_session(*args, **kwargs):
    """ remove SQLAlchemy session """
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
