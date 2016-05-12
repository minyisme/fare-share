"""Travels and Stuffs"""

from jinja2 import StrictUndefined
from flask import Flask, render_template, redirect, request, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from pprint import pprint

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
    num_origins = int(request.form.get("num_origins"))

    python_results = []

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





    # Get key from environment
        API_KEY = os.environ['QPX_KEY']

        # Insert key into QPX API url
        url = "https://www.googleapis.com/qpxExpress/v1/trips/search?key=%s" %(API_KEY)

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
                # "kind": "qpxexpress#sliceInput",
                "origin": flight_origin,
                "destination": flight_destination,
                "date": departure_date,
                "maxStops": 1,
              },
              {
                "origin": flight_destination,
                "destination": flight_origin,
                "date": return_date,
                "maxStops": 1,            
              }
            ],
            # Hard coding number of flight options
            # QPX API takes up to 500
            "solutions": 5,
            "maxPrice": max_price,
          }
        }

        # Turns parameters into JSON string
        json_params = json.dumps(parameters, encoding = 'utf-8')
        # Sends JSON string request to QPX and returns JSON 
        flight_request = urllib2.Request(url, json_params, {'Content-Type': 'application/json'})

        # Opens JSON results
        results = urllib2.urlopen(flight_request)
        # Read results and turn it into Python
        python_results.append(json.load(results))
        # Closes JSON results
        results.close()

    # Initialize empty list for all flight data to go into
    # flight_data = []

    # # For each of the flight options
    # for x in range(len(python_results["trips"]["tripOption"])):

    #     # Initialize empty dictionary to hold flight info
    #     flight_data.append({})

    #     # Basic flight data variable assignment
    #     option_data = python_results["trips"]["tripOption"]
    #     option_id = option_data[x]["id"]
    #     option_price = option_data[x]["saleTotal"]

    #     # Add basic flight data to dictionary
    #     flight_data[x]["option_id"] = option_id
    #     flight_data[x]["option_price"] = option_price
    #     flight_data[x]["option_flight"] = []

    #     # Get to each to and return option
    #     slice_data = python_results["trips"]["tripOption"][x]["slice"]
    #     dep_ret = ["Departure", "Return"]

    #     # For each to and return option
    #     for y in range(len(slice_data)):

    #         # Initialize empty list to hold to and return info
    #         flight_data[x]["option_flight"].append([])

    #         # Basic to and return option data variable assignment
    #         flight_duration = slice_data[y]["duration"]
    #         segment_data = slice_data[y]["segment"]

    #         # For each leg of a flight
    #         for z in range(len(segment_data)):

    #             # Initialize empty dictionary to add leg info to
    #             flight_data[x]["option_flight"][y].append({})

    #             # Leg data variable assignment
    #             each_leg = segment_data[z]["leg"][0]
    #             leg_duration = each_leg["duration"]
    #             leg_origin = each_leg["origin"]
    #             leg_departure = each_leg["departureTime"]
    #             leg_destination = each_leg["destination"] 
    #             leg_arrival = each_leg["arrivalTime"]

    #             # Add leg data to dictionary
    #             flight_data[x]["option_flight"][y][z]["leg_duration"] = leg_duration
    #             flight_data[x]["option_flight"][y][z]["leg_origin"] = leg_origin
    #             flight_data[x]["option_flight"][y][z]["leg_departure"] = leg_departure
    #             flight_data[x]["option_flight"][y][z]["leg_destination"] = leg_destination
    #             flight_data[x]["option_flight"][y][z]["leg_arrival"] = leg_arrival

    #         # Get connection info
    #         for a in range(len(segment_data)-1):
    #             connection_duration = segment_data[a]["connectionDuration"]

    pprint(python_results)

    # Trip results page with all the data necessary for tables
    return render_template("trip.html", results=results)

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