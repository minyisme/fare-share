"""Functions for project""" 
from pprint import pprint

from flask import Flask, render_template, redirect, request, flash, session
from flask_sqlalchemy import SQLAlchemy
import urllib2
import json    
import os

from model import connect_to_db, db, User, Trip, UserTrip, Option, Flight, Leg, Airport



################################################################################

## validating ##

################################################################################



def is_valid_login(user_email, user_password):
    """Validates input email and password against users in db and returns true 
    if match and false if not match"""

    # Check User db for email and password match
    if User.query.filter_by(email=user_email, password=user_password).first():
        # If match, add to session to indicate logged in user
        logged_in_user = User.query.filter_by(email=user_email, password=user_password).first()
        session["user_id"] = logged_in_user.user_id
        return True
    # Else, prompt to try again
    else:
        flash("Forgot your password you idiot! Try again.")
        return False



def is_registered_email(user_email):
    """Validates input user_email against emails in db"""

    # Checks if user email is already registered
    if User.query.filter_by(email=user_email).first():
        # Flash message if email is already used by a registered user
        flash("This email is already taken; please log in.")
        return True
    else:
        return False



################################################################################

## add records to db ##

################################################################################



def add_user_to_db(user_info):
    """Takes dictionary of user information and adds them to user attributes. Then 
    add new user to db"""

    # Instantiates user object with info from input user_info 
    user = User(email=user_info["user_email"], 
                password=user_info["user_password"],
                user_name=user_info["user_name"],
                origin_airport_code=user_info["user_origin_airport_code"])

    # Add user to session
    db.session.add(user)
    # Commit session to db
    db.session.commit()

    # Flash message to confirm registration
    flash("Thank you for registering; please log in.")

    return user



def add_trip_to_db(trip_info):
    """Takes dictionary of trip information and adds them to trip attributes. Then 
    add new trip to db"""

    # Instantiates trip object with info from input user_info
    trip = Trip(trip_name=trip_info["trip_name"])

    # Add user to session
    db.session.add(trip)
    # Commit session to db
    db.session.commit()

    return trip



def add_usertrip_to_db(usertrip_info):
    """Takes dictionary of usertrip information and adds them to usertrip attributes.
    Then add new usertrip to db"""

    # Instantiates usertrip object with info from input usertrip_info
    usertrip = UserTrip(user_id=usertrip_info["user_id"], trip_id=usertrip_info["trip_id"])

    # Add usertrip to session
    db.session.add(usertrip)
    # Commit session to db
    db.session.commit()

    return usertrip



def add_option_to_db(option_info):
    """Takes dictionary of option information and adds them to option attributes. 
    Then add new option to db"""

    # Instantiates option object with info from input option_info
    option = Option(trip_id=option_info["trip_id"], 
                    destination_airport_code=option_info["destination"], 
                    depart_date=option_info["depart_date"], 
                    return_date=option_info["return_date"])

    # Add option to session
    db.session.add(option)
    # Commit session to db
    db.session.commit()

    return option



def add_flight_to_db(option, flight_info):
    """Takes a option object and dictionary of flight information and adds them to flight 
    attributes. Then add new flight to db"""

    # Instantiates flight object with info from inputs option object and flight_info
    flight = Flight(option_id=option.option_id, flight_price=flight_info["flight_price"])

    # Add flight to session
    db.session.add(flight)
    # Commit session to db
    db.session.commit()

    return flight



def add_leg_to_db(flight, leg_info):
    """Takes a flight object and dictionary of leg information and adds them to leg 
    attributes. Then add new leg to db"""

    # Instantiates leg object with info from inputs flight object and leg_info
    leg = Leg(flight_id=flight.flight_id, 
              origin_airport_code=leg_info["origin_airport_code"],
              departure_datetime=leg_info["departure_datetime"], 
              destination_airport_code=leg_info["destination_airport_code"], 
              arrival_datetime=leg_info["arrival_datetime"], 
              leg_airline=leg_info["airline_code"], 
              leg_flight_code=leg_info["flight_code"],
              leg_duration=leg_info["leg_duration"])

    # Add leg to session
    db.session.add(leg)
    # Commit session to db
    db.session.commit()

    return leg



################################################################################

## query from db ##

################################################################################



def trips_by_user(user):
    """Takes input user object, and returns all trip objects associated with user"""

    # Get all usertrips associated with user
    usertrips = UserTrip.query.filter_by(user_id=user.user_id).all()

    # Initialize empty trips
    trips = []

    # Get every trip for the usertrips in usertrip_list
    for usertrip in usertrips:
        trips.append(Trip.query.get(usertrip.trip_id))

    return trips



def origin_airport_codes_by_trip(trip):
    """Takes input trip object, and returns all origin_airport_codes of users on 
    this trip"""

    # Instantiates empty list to put in origin airport codes
    origin_airport_codes = []
    # Iterates over usertrip for input trip and adds user's origin airport codes to list
    for usertrip in trip.usertrips:
        origin_airport_codes.append(usertrip.user.origin_airport_code)

    origin_airport_codes = str(origin_airport_codes)
    origin_airport_codes = origin_airport_codes.replace("u'", '"')
    origin_airport_codes = origin_airport_codes.replace("'", '"')

    return origin_airport_codes



def userstrips_by_trip(trip):
    """Takes input trip object, and returns all usertrip objects associated with
    that trip"""

    userstrips = UserTrip.query.filter_by(trip_id = trip.trip_id).all()

    return userstrips



def travelers_by_userstrips(userstrips):

    travelers = {}
    for usertrip in userstrips:
        travelers[usertrip.user.user_name] = usertrip.user.origin_airport_code

    return travelers



def options_by_trip(trip):
    """Takes input trip object, and returns all option objects associated with
    that trip"""

    options = Option.query.filter_by(trip_id = trip.trip_id).all()

    return options



def flights_by_option(option):
    """Takes input option object, and returns all flight objects associated with
    that option"""

    flights = Flight.query.filter_by(option_id = option.option_id).all()

    return flights



def legs_by_flight(flight):
    """Takes input flight object, and returns all legs objects associated with
    that flight"""

    legs = Leg.query.filter_by(flight_id = flight.flight_id).all()

    return legs



def make_airports_autocomplete():
    """Takes no input, and returns list of strings of all airports "Airport Code 
    - Airport Name, Airport City"""

    airports = Airport.query.all()

    airports_autocomplete_list = []
    for airport in airports:
        #  Get all airport info from db if airport_city exists
        if airport.airport_city:
            airport_autocomplete = ["%s: %s, %s" %(airport.airport_code, airport.airport_name, airport.airport_city)]
            airport_autocomplete.append((airport.airport_lat, airport.airport_long))
        # Get all airport info from db if no airport_city
        else:
            airport_autocomplete = ["%s: %s" %(airport.airport_code, airport.airport_name)]
            airport_autocomplete.append((airport.airport_lat, airport.airport_long))
        airports_autocomplete_list.append(airport_autocomplete)

    return airports_autocomplete_list



################################################################################

## delete from db ##

################################################################################


# After Career day, refactor to this!!!!
# def delete_things(things):
#     for thing in things:
#         db.session.delete(thing)
#         db.session.commit()


def delete_legs(legs):
    """Takes input list of leg objects and deletes all leg records from db"""

    # Iterate over legs_list and delete all legs from db
    for leg in legs:
        db.session.delete(leg)
        db.session.commit()


def delete_flights(flights):
    """Takes input list of flights objects and deletes all flight records from db"""

    # Iterate over flights and delete all flights from db
    for flight in flights:
        db.session.delete(flight)
        db.session.commit()


def delete_options(options):
    """Takes input list of options objects and deletes all option records from db"""

    # Iterate over options and delete all options from db
    for option in options:
        db.session.delete(option)
        db.session.commit()

def delete_userstrips(userstrips):
    """Takes input list of usertrip objects and deletes all usertrip records from
    db"""

    # Iterate over userstrips and delete all options from db
    for usertrip in userstrips:
        db.session.delete(usertrip)
        db.session.commit

################################################################################

## QPX query ##

################################################################################



def get_params(origin_airport_code, option_info):
    """Gets parameter variables for a QPX search from user origin_airport_codes 
    and option"""

    # Initializes empty params list
    params = {}
    # Adds a dictionary to params of parameters for every origin airport code
    params["num_travelers"] = 1
    params["flight_origin"] = origin_airport_code
    params["flight_destination"] = option_info["destination"]
    params["depart_date"] = option_info["depart_date"]
    params["return_date"] = option_info["return_date"]
    params["max_price"] = "USD10000"

    return params



def parameter_by_params(query):
    """Get parameter dictionary from params"""

    # Get inputs from params into parameters
    parameter = {
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
            "date": query["depart_date"],
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
        "solutions": 1,
        "maxPrice": query["max_price"],
      }
    }

    return parameter



def query_QPX(parameter):
    """Send query with parameter and url to QPX"""

    # Get key from environment
    API_KEY = os.environ['QPX_KEY']

    # Insert key into QPX API url
    url = "https://www.googleapis.com/qpxExpress/v1/trips/search?key=%s" %(API_KEY)

    # Turns parameters into JSON string
    json_param = json.dumps(parameter, encoding = 'utf-8')

    # Sends JSON string request to QPX and returns JSON 
    flight_request = urllib2.Request(url, json_param, {'Content-Type': 'application/json'})

    return flight_request



################################################################################

## QPX results ##

################################################################################



def QPX_results(flight_request):
    """Read results from query to QPX into python and add to list"""

    # Opens JSON results
    results = urllib2.urlopen(flight_request)

    # Read results and turn it into Python
    python_result = json.load(results)
    # Closes JSON results
    results.close()

    return python_result



def parse_results(python_result, option):
    """Takes inputs python_results and option object and parses the python_results
    to be ready to display on search results page."""

    # Gets option_id from option object
    option_id = option.option_id

    # # Initiates empty flights dictionary
    flights = []
    # Parsing QPX results to add to flights table
    # for i in range(len(python_results)):
    # use enumerate to make this more readable!!!!!
    for j in range(len(python_result["trips"]["tripOption"])):
        flight_info = {"flight_price":python_result["trips"]["tripOption"][j]["saleTotal"]}
        # Calls function to add flight to db
        flight = add_flight_to_db(option, flight_info)
        flight_dict = flight.to_dict()
        # Adds a new list value at flight object key in flights dictionary
        flights.append(flight_dict)
        flights.append([])
        # Parsing QPX results to add to legs table
        for flight_slice in python_result["trips"]["tripOption"][j]["slice"]:
            for flight_segment in flight_slice["segment"]:
                leg_info = {}
                leg_info["airline_code"] = flight_segment["flight"]["carrier"]
                leg_info["flight_code"] = flight_segment["flight"]["number"]
                leg_info["origin_airport_code"] = flight_segment["leg"][0]["origin"]
                leg_info["destination_airport_code"] = flight_segment["leg"][0]["destination"]
                leg_info["departure_datetime"] = flight_segment["leg"][0]["departureTime"]
                leg_info["arrival_datetime"] = flight_segment["leg"][0]["arrivalTime"]
                leg_info["leg_duration"] = flight_segment["leg"][0]["duration"]
                # Calls function to add leg to db
                leg = add_leg_to_db(flight, leg_info)
                leg_dict = leg.to_dict()
                # Adds each leg to the list value at flight key
                flights[1].append(leg_dict)

    return flights



################################################################################

## other ##

################################################################################



def logout():
    """Logsout user by deleting user_id from session and flash confirmation message"""

    # Deletes user_id from session
    del session["user_id"]

    return
