import codecs
import csv

counter = 0
dictairports = {}

with open('airports.csv', 'rb') as allairports:
    airportsinfo = csv.reader(allairports)
    for row in airportsinfo:
        dictairports[counter] = [row[13], row[3], row[4], row[5]]
        counter += 1

print dictairports

self.airport_code, self.airport_name, self.airport_city, self.airport_lat, self.airport_long