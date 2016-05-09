"""Travels and Stuffs"""

from jinja2 import StrictUndefined
from flask import Flask, render_template, redirect, request, flash, session
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

# Undefined variable in Jinja2 raises an error
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def index():
    """Homepage"""

    return render_template("homepage.html")

@app.route('/profile')
def profile():
    """User profile page"""

    return render_template("profile.html")

@app.route('/settings')
def settings():
    """User settings page"""

    return render_template("settings.html")

@app.route('/trip')
def trip_info():
    """Trip page"""

    return render_template("trip.html")

@app.route('/trip/search')
def trip_search():
    """Search flights"""

    return render_template("trip_search.html")

@app.route('/trip/results')
def trip_results():
    """Search flights results"""

    return render_template("trip_results.html")

@app.route('/trip/share')
def trip_share():
    """Share trip with other users"""

    return render_template("trip_share.html")

if __name__ == "__main__":
    # Debug to be turned off for production
    app.debug = True

    # Use DebugToolbar
    DebugToolbarExtension(app)

    # Runs app
    app.run()