
"""Functions for project""" 
from pprint import pprint

import pdb

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
            "solutions": 2,
            "maxPrice": query["max_price"],
          }
        }

        # Turns parameters into JSON string
        json_params = json.dumps(parameters, encoding = 'utf-8')
        # Sends JSON string request to QPX and returns JSON 
        flight_request = urllib2.Request(url, json_params, {'Content-Type': 'application/json'})

        # Opens JSON results
        results = urllib2.urlopen(flight_request)

        # pprint(results)
        # Read results and turn it into Python
        python_result = json.load(results)
        python_results.append(python_result)
        # Closes JSON results
        results.close()

    return python_results