"""Travels and Stuffs"""

from jinja2 import StrictUndefined
from flask import Flask, render_template, redirect, request, flash, session
from flask_debugtoolbar import DebugToolbarExtension

import urllib2
import json
import os



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
    num_travelers = (request.form.get("num_travelers"))
    flight_origin = request.form.get("flight_origin")
    flight_destination = request.form.get("flight_destination")
    departure_date = request.form.get("departure_date")
    max_price = request.form.get("max_price")
    max_price = "USD" + max_price

    print num_travelers

    # Get key from environment
    API_KEY = os.environ['QPX_KEY']

    # Insert key into QPX API url
    url = "https://www.googleapis.com/qpxExpress/v1/trips/search?key=%s" %(API_KEY)

    # # Get search parameters from Flight Search Form
    # num_travelers = int(request.form.get("num_travelers"))
    # flight_origin = request.form.get("flight_origin")
    # flight_destination = request.form.get("flight_destination")
    # departure_date = request.form.get("departure_date")
    # max_price = request.form.get("max_price")
    # max_price = "USD" + max_price

    # Search parameters to QPX API
    # Variables from user: adultCount, origin, desination, date, maxPrice
    # All other variables static
    parameters = {
      "request": {
        "passengers": {
          "kind": "qpxexpress#passengerCounts",
          "adultCount": num_travelers,
        },
        "slice": [
          {
            "kind": "qpxexpress#sliceInput",
            "origin": flight_origin,
            "destination": flight_destination,
            "date": departure_date,
            "maxStops": 1,
          }
        ],
        "solutions": 2,
        "maxPrice": max_price,
      }
    }

    # Turns parameters into JSON string
    json_params = json.dumps(parameters, encoding = 'utf-8')
    # Sends JSON string request to QPX and returns JSON 
    flight_request = urllib2.Request(url, json_params, {'Content-Type': 'application/json'})

    # Opens JSON results
    results = urllib2.urlopen(flight_request)
    # Read results
    json_results = results.read()
    # Closes JSON results
    results.close()

    return render_template("trip_results.html", results=json_results)

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