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
    num_travelers = (request.form.get("num_travelers"))
    flight_origin = request.form.get("flight_origin")
    flight_destination = request.form.get("flight_destination")
    departure_date = request.form.get("departure_date")
    max_price = request.form.get("max_price")
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
            "date": departure_date,
            "maxStops": 1,            
          }
        ],
        # Hard coding number of flight options
        # QPX API takes up to 500
        "solutions": 100,
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
    python_results = json.load(results)
    # Closes JSON results
    results.close()

    # Create flight_data dictionary
    flight_data = {}



    for x in range(len(python_results["trips"]["tripOption"])):
    # print "Round trip flight option %s" %(x)
    option_data = python_results["trips"]["tripOption"]
    option_id = flight_data[i]["id"]
    # print "ID: %s" %(flight_id)
    option_price = flight_data[i]["saleTotal"]
    # print "Price: %s" %(flight_price)
    # print "\n\n\n"
    flight_data[i] = [{"option_id": option_id},{"option_price": option_price}]



    slice_data = python_results["trips"]["tripOption"][x]["slice"]
    dep_ret = ["Departure", "Return"]

    # flight_data[i] = [{option id, option price},{}]
    flight_data[i].append({})

    for y in range(len(slice_data)):
        # print "%s Leg" %(dep_ret[y])
        flight_duration = slice_data[y]["duration"]
        # print "Flight Duration: %s" %(flight_duration)


        flight_data[i][y+1]["flight_duration"] = flight_duration
        

        segment_data = slice_data[y]["segment"]


        # flight_data[i] = [{option id, option price}, {flight duration, {}}]
        flight_data[i][y].append({})
        for z in range(len(segment_data)):
            # print "Leg %s" %(z)
            each_leg = segment_data[z]["leg"][0]
            leg_duration = each_leg["duration"]
            # print "Duration: %s" %(leg_duration)
            leg_origin = each_leg["origin"]
            # print "Origin: %s" %(leg_origin)
            leg_departure = each_leg["departureTime"]
            # print "Departure Time: " + leg_departure
            leg_destination = each_leg["destination"] 
            # print "Destination: %s" %(leg_destination)
            leg_arrival = each_leg["arrivalTime"]
            # print "Arrival Time: " + leg_arrival
            # print "\n\n\n"


            flight_data[i][y+1][z+1]["leg_duration"] = leg_duration
            flight_data[i][y+1][z+1]["leg_origin"] = leg_origin
            flight_data[i][y+1][z+1]["leg_departure"] = leg_departure
            flight_data[i][y+1][z+1]["leg_destination"] = leg_destination
            flight_data[i][y+1][z+1]["leg_arrival"] = leg_arrival


        for a in range(len(segment_data)-1):
            connection_duration = segment_data[a]["connectionDuration"]

            flight_data[i][y+1][z+1]["connection_duration"] = connection_duration
            # print "Connection Duration: %s" %(connection_duration)
            # print "\n\n\n"
    # print "\n\n\n"

    # Commented out to test return flights

    # # For each flight option, get id, duration, fare, tax, total fare
    # for i in range(len(python_results["trips"]["tripOption"])):
    #     flight_id = python_results["trips"]["tripOption"][i]["id"]
    #     flight_duration = python_results["trips"]["tripOption"][i]["slice"][0]["duration"]
    #     flight_fare = python_results["trips"]["tripOption"][i]["pricing"][0]["saleFareTotal"]
    #     flight_tax = python_results["trips"]["tripOption"][i]["pricing"][0]["saleTaxTotal"]
    #     flight_total = python_results["trips"]["tripOption"][i]["pricing"][0]["saleTotal"]

    #     # Wrap all flight data for one flight into one dictionary item
    #     flight_data[i] = [flight_id, flight_duration, flight_fare, flight_tax, flight_total]

    #     # Create segment_data variable to do less repetitive typing
    #     segment_data = python_results["trips"]["tripOption"][i]["slice"][0]["segment"]
    
    #     # For each segment inside each flight append all the legs and info to dict

    #     flight_data[i].append([])
    #     for x in range(len(segment_data)):
    #         leg_origin = segment_data[x]["leg"][0]["origin"]
    #         leg_departure = segment_data[x]["leg"][0]["departureTime"]
    #         leg_destination = segment_data[x]["leg"][0]["destination"]
    #         leg_arrival = segment_data[x]["leg"][0]["arrivalTime"]
    #         flight_data[i][5].append([leg_origin, leg_departure, leg_destination, leg_arrival])

    # Commented out to test return flights
    # return render_template("trip_results.html", results=flight_data)

    pprint(python_results)

    return render_template("trip.html", results=flight_data)

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