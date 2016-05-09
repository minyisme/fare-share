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
        "origin": "ORD",
        "destination": "LHR",
        "date": "2016-06-11",
        "maxStops": 1,
      }
    ],
    "solutions": 20,
    "maxPrice": "USD2000.00",
  }
}

# Turns parameters into JSON string
json_params = json.dumps(parameters, encoding = 'utf-8')
# Sends JSON string request to QPX and returns JSON 
request = urllib2.Request(url, json_params, {'Content-Type': 'application/json'})

# Opens JSON results
results = urllib2.urlopen(request)
# Read results
json_results = results.read()
# Closes JSON results
results.close()
# Prints resulting JSON string
print (json_results)