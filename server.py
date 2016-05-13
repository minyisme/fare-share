"""Server for project"""

from jinja2 import StrictUndefined
from flask import Flask, render_template, redirect, request, flash, session
from flask_debugtoolbar import DebugToolbarExtension

from model import connect_to_db, db, User, Trip, UserTrip, Option, Flight, Leg, Airport

import functions



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



@app.route('/trip/results', methods=["POST"])
def trip_results():
    """Search flights results"""

    # Get search parameters from Flight Search Form
    num_origins = int(request.form.get("num_origins"))

    params = []
    for num in range(0, num_origins):
        params.append({})
        num_travelers = request.form.get("num_travelers%s" %num)
        params[num]["num_travelers"] = num_travelers
        flight_origin = request.form.get("flight_origin%s" %num)
        params[num]["flight_origin"] = flight_origin
        flight_destination = request.form.get("flight_destination%s" %num)
        params[num]["flight_destination"] = flight_destination
        departure_date = request.form.get("departure_date%s" %num)
        params[num]["departure_date"] = departure_date
        return_date = request.form.get("return_date%s" %num)
        params[num]["return_date"] = return_date
        max_price = request.form.get("max_price%s" %num)
        max_price = "USD" + max_price
        params[num]["max_price"] = max_price

    flight_results_data = functions.flight_query(params)

    # Trip results page with all the data necessary for tables
    return render_template("trip_results.html", results=flight_results_data)



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