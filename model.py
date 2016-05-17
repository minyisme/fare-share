"""Models and database functions for project"""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

#################################################
# Model definitions

# User who logs in to the site
class User(db.Model):
    """User in project"""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String(100), nullable=False) # add unique constraint
    password = db.Column(db.String(40), nullable=False)
    user_name = db.Column(db.String(20), nullable=False) # add unique constraint
    origin_airport_code = db.Column(db.String(3), db.ForeignKey('airports.airport_code'), nullable=False)

    # Define relationship to airport
    origin_airport = db.relationship('Airport', backref='users')

    # # Secondary backref to Trips
    # trips = db.relationship('Trip', secondary="usertrips", backref=db.backref('usertrips'))

    def __repr__(self):
        """Provide helpful representation when printed."""

        return ("<User user_id=%s email=%s password=%s user_name=%s origin_aiport_code=%s>"
                % (self.user_id, self.email, self.password, self.user_name, self.origin_airport_code))



# Trips that can be taken by multiple users and planned among users
class Trip(db.Model):
    """Trip in project"""

    __tablename__ = "trips"

    trip_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    trip_name = db.Column(db.String(40), nullable=False)

    def __repr__(self):
        """Provide helpful representation when printed."""

        return ("<Trip trip_id=%s trip_name=%s>" 
                % (self.trip_id, self.trip_name))



# Middle table of users to trips where users can vote for an option per trip
class UserTrip(db.Model): 
    """User to Trip association"""

    __tablename__ = "userstrips"

    usertrip_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    trip_id = db.Column(db.Integer, db.ForeignKey('trips.trip_id'), nullable=False)
    option_vote = db.Column(db.Integer, db.ForeignKey('options.option_id'), nullable=True)

    # Define relationship to user, trip, and option
    user = db.relationship('User', backref='usertrips')
    trip = db.relationship('Trip', backref='usertrips')
    option = db.relationship('Option', backref='votes')

    def __repr__(self):
        """Provide helpful representation when printed."""

        return ("<User_Trip user_trip_id=%s user_id=%s trip_id=%s user_trip_vote=%s>" 
                % (self.usertrip_id, self.user_id, self.trip_id, self.option_vote))



# Different options belonging to each trip the users can choose
class Option(db.Model):
    """Option in a Trip"""

    __tablename__ = "options"

    option_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    trip_id = db.Column(db.Integer, db.ForeignKey('trips.trip_id'), nullable=False)
    destination_airport_code = db.Column(db.String(3), db.ForeignKey('airports.airport_code'), nullable=False)
    depart_date = db.Column(db.Date, nullable=False)
    return_date = db.Column(db.Date, nullable=False)

    # Define relationship to trip and airport
    trip = db.relationship('Trip', backref='options')
    destination_airport = db.relationship('Airport', backref='options')

    def __repr__(self):
        """Provide helpful representation when printed."""

        return ("<Option option_id=%s trip_id=%s destination_airport_code=%s departure_date=%s return_date=%s>"
                % (self.option_id, self.trip_id, self.destination_airport_code, self.depart_date, self.return_date))    



# Flight options from QPX API belonging to each option
class Flight(db.Model):
    """Flight in an Option"""

    __tablename__ = "flights"

    flight_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    option_id = db.Column(db.Integer, db.ForeignKey('options.option_id'), nullable=False)
    flight_price = db.Column(db.String(12), nullable=False)
    has_layover = db.Column(db.Boolean, nullable=False)
    layover_duration = db.Column(db.Integer, nullable=True)

    # Define relationship to option
    option = db.relationship('Option', backref='flights')

    def __repr__(self):
        """Provide helpful representation when printed."""

        return ("<Flight flight_id=%s option_id=%s flight_price=%s has_layover=%s layover_time=%s>"
                % (self.flight_id, self.option_id, self.flight_price, self.has_layover, self.layover_duration))



# Legs constituting a flight from QPX API
class Leg(db.Model):
    """Leg in a flight"""

    __tablename__ = "legs"

    leg_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    flight_id = db.Column(db.Integer, db.ForeignKey('flights.flight_id'), nullable=False)
    direction = db.Column(db.String(6), nullable=False) # only allowed to put two things here
    origin_airport_code = db.Column(db.String(3), db.ForeignKey('airports.airport_code'), nullable=False)
    departure_datetime = db.Column(db.DateTime, nullable=False)
    destination_airport_code = db.Column(db.String(3), db.ForeignKey('airports.airport_code'), nullable=False)
    arrival_datetime = db.Column(db.DateTime, nullable=False)
    leg_airline = db.Column(db.String(2), nullable=False)
    leg_flight_code = db.Column(db.String(4), nullable=False) # think about storing it as an integer if leading 0 is unimportant
    leg_duration = db.Column(db.Integer, nullable=False)

    # Define relationship to flight, airport, and airport
    flight = db.relationship('Flight', backref='legs')
    origin_airport = db.relationship('Airport', foreign_keys=[origin_airport_code])
    destination_airport = db.relationship('Airport', foreign_keys=[destination_airport_code])

    def __repr__(self):
        """Provide helpful representation when printed."""

        return ("<Leg leg_id=%s flight_id=%s direction=%s origin_airport=%sdeparture_datetime=%s" + 
                "destination_airport=%s arrival_datetime=%s leg_airline=%s leg_flight_code=%s leg_duration=%s>"
                % (self.leg_id, self.flight_id, self.direction, self.origin_airport, self.departure_datetime, 
                   self.destination_airport, self.arrival_datetime, self.leg_airline, self.leg_flight_code, 
                   self.leg_duration))



# Airports by airport code that can be origins and destination IDs
class Airport(db.Model):
    """Airport by airport code"""

    __tablename__ = "airports"

    airport_code = db.Column(db.String(3), primary_key=True)
    airport_name = db.Column(db.String(500), nullable=False)
    airport_city = db.Column(db.String(200), nullable=True)
    airport_lat = db.Column(db.Float, nullable=False)
    airport_long = db.Column(db.Float, nullable=False)

    def __repr__(self):
        """Provide helpful representation when printed."""

        return ("<Airport airport_code=%s airport_name=%s airport_city=%s airport_lat=%s airport_long=%s>"
                % (self.airport_code, self.airport_name, self.airport_city, self.airport_lat, self.airport_long))

#################################################
# Helper functions

def connect_to_db(app):
    """Connect the database to our Flask app"""

    # Configure to use our PostgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://maggieyang:hackbright@localhost:5432/travels'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)

if __name__ == "__main__":
    # Allows interaction directly with db from
    # server when running interactively

    from server import app
    connect_to_db(app)
    db.create_all()
    print "Connected to DB."