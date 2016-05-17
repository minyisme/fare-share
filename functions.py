
"""Functions for project""" 
from pprint import pprint

import urllib2
import json    
import os

def flight_query(params):

    python_results = []

    for query in params:

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
              "adultCount": query["num_travelers"],
            },
            "slice": [
              {
                # "kind": "qpxexpress#sliceInput",
                "origin": query["flight_origin"],
                "destination": query["flight_destination"],
                "date": query["departure_date"],
                "maxStops": 1,
              },
              {
                "origin": query["flight_destination"],
                "destination": query["flight_origin"],
                "date": query["return_date"],
                "maxStops": 1,            
              }
            ],
            # Hard coding number of flight options
            # QPX API takes up to 500
            "solutions": 5,
            "maxPrice": query["max_price"],
          }
        }

        # Turns parameters into JSON string
        json_params = json.dumps(parameters, encoding = 'utf-8')
        # Sends JSON string request to QPX and returns JSON 
        flight_request = urllib2.Request(url, json_params, {'Content-Type': 'application/json'})

        # Opens JSON results
        results = urllib2.urlopen(flight_request)
        # Read results and turn it into Python
        python_result = json.load(results)
        python_results.append(python_result)
        # Closes JSON results
        results.close()

    return python_results


def flight_query_results(python_results):

    # Initialize empty list for all flight data to go into
    flight_data = []

    for w in range(len(python_results)):
        flight_data.append([])
        # For each of the flight options
        for x in range(len(python_results[w]["trips"]["tripOption"])):

            # Initialize empty dictionary to hold flight info
            flight_data[w].append({})

            # Basic flight data variable assignment
            option_data = python_results[w]["trips"]["tripOption"]
            option_id = option_data[x]["id"]
            option_price = option_data[x]["saleTotal"]

            # Add basic flight data to dictionary
            flight_data[w][x]["option_id"] = option_id
            flight_data[w][x]["option_price"] = option_price
            flight_data[w][x]["option_flight"] = []

            # Get to each to and return option
            slice_data = python_results[w]["trips"]["tripOption"][x]["slice"]
            dep_ret = ["Departure", "Return"]

            # For each to and return option
            for y in range(len(slice_data)):

                # Initialize empty list to hold to and return info
                flight_data[w][x]["option_flight"].append([])

                # Basic to and return option data variable assignment
                flight_duration = slice_data[y]["duration"]
                segment_data = slice_data[y]["segment"]

                # For each leg of a flight
                for z in range(len(segment_data)):

                    # Initialize empty dictionary to add leg info to
                    flight_data[w][x]["option_flight"][y].append({})

                    # Leg data variable assignment
                    each_leg = segment_data[z]["leg"][0]
                    leg_duration = each_leg["duration"]
                    leg_origin = each_leg["origin"]
                    leg_departure = each_leg["departureTime"]
                    leg_destination = each_leg["destination"] 
                    leg_arrival = each_leg["arrivalTime"]

                    # Add leg data to dictionary
                    flight_data[w][x]["option_flight"][y][z]["leg_duration"] = leg_duration
                    flight_data[w][x]["option_flight"][y][z]["leg_origin"] = leg_origin
                    flight_data[w][x]["option_flight"][y][z]["leg_departure"] = leg_departure
                    flight_data[w][x]["option_flight"][y][z]["leg_destination"] = leg_destination
                    flight_data[w][x]["option_flight"][y][z]["leg_arrival"] = leg_arrival

                # Get connection info
                for a in range(len(segment_data)-1):
                    connection_duration = segment_data[a]["connectionDuration"]

    # pprint(python_results)

    return flight_data