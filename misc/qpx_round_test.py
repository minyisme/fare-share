import urllib2
import json
import os

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
      "adultCount": 1,
    },
    "slice": [
      {
        "kind": "qpxexpress#sliceInput",
        "origin": "SFO",
        "destination": "JFK",
        "date": "2016-06-11",
        "maxStops": 1,
      },
      {
        "kind": "qpxexpress#sliceInput",
        "origin": "JFK",
        "destination": "SFO",
        "date": "2016-06-21",
        "maxStops": 1,            
      }
    ],
    # Hard coding number of flight options
    # QPX API takes up to 500
    "solutions": 100,
    "maxPrice": "USD4000.00",
  }
}

# Turns parameters into JSON string
json_params = json.dumps(parameters, encoding = 'utf-8')
# Sends JSON string request to QPX and returns JSON 
flight_request = urllib2.Request(url, json_params, {'Content-Type': 'application/json'})

# Opens JSON results
results = urllib2.urlopen(flight_request)
# Read results and turn it into Python
python_results = results.read()
# Closes JSON results
results.close()

# Create flight_data dictionary
print (python_results)