import json

from pprint import pprint

with open('airports_sample.json') as airports_file:
    airports = json.load(airports_file)

pprint(airports)