import urllib2
import json
import os

API_KEY = os.environ['QPX_KEY']

url = "https://www.googleapis.com/qpxExpress/v1/trips/search?key=%s" %(API_KEY)

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

json_params = json.dumps(parameters, encoding = 'utf-8')
request = urllib2.Request(url, json_params, {'Content-Type': 'application/json'})

results = urllib2.urlopen(request)
json_results = results.read()
results.close()
print (json_results)