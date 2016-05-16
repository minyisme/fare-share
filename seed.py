"""Utility file to seed travels db from ourairports.com/data/"""

from sqlalchemy import func
from model import Airport

from model import connect_to_db, db
from server import app

import csv

def load_airports():
    """Load airports from airports.csv into database"""

    print "Aiports"

    # Delete all rows in table, so if we need to
    # run this a second time, we won't be trying
    # to add duplicate users.
    Airport.query.delete()

    # Read airports.csv file and insert data
    counter = 0
    dictairports = {}

    with open('misc/airports_filtered.csv', 'rb') as allairports:
        airportsinfo = csv.reader(allairports)
        for row in airportsinfo:
            airport_code, airport_name, airport_city, airport_lat, airport_long = row[13], row[3], row[10], row[4], row[5]
            counter += 1

            airport = Airport(airport_code=airport_code,
                              airport_name=airport_name,
                              airport_city=airport_city,
                              airport_lat=airport_lat,
                              airport_long=airport_long)

            db.session.add(airport)

    db.session.commit()

if __name__ == "__main__":
    connect_to_db(app)

    db.create_all

    load_airports()

