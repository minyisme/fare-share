import json
from pprint import pprint


def parse():
    with open('misc/airports_sample.json') as airports_file:
        airports = json.load(airports_file)

    return airports

pprint(parse())