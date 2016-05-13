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
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(40), nullable=False)
    user_name = db.Column(db.String(20), nullable=False)
    origin_airport = db.Column(db.String(3), db.ForeignKey('airports.airport_code'), nullable=False)

    # Define relationship to airport
    airport = db.relationship('Airport', backref='users')

    def __repr__(self):
        """Provide helpful representation when printed."""

        return ("<User user_id=%s email=%s password=%s user_name=%s origin_aiport=%s>"
                % (self.user_id, self.email, self.password, self.user_name, self.origin_airport))



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
                % (self.user_trip_id, self.user_id, self.trip_id, self.option_vote))



# Different options belonging to each trip the users can choose
class Option(db.Model):
    """Option in a Trip"""

    __tablename__ = "options"

    option_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    trip_id = db.Column(db.Integer, db.ForeignKey('trips.trip_id'), nullable=False)
    destination_airport = db.Column(db.String(3), db.ForeignKey('airports.airport_code'), nullable=False)
    depart_date = db.Column(db.Date, nullable=False)
    return_date = db.Column(db.Date, nullable=False)

    # Define relationship to trip and airport
    trip = db.relationship('Trip', backref='options')
    airport = db.relationship('Airport', backref='options')

    def __repr__(self):
        """Provide helpful representation when printed."""

        return ("<Option option_id=%s trip_id=%s destination_airport=%s departure_date=%s return_date=%s>"
                % (self.option_id, self.trip_id, self.destination_airport, self.depart_date, self.return_date))    



# Flight options from QPX API belonging to each option
class Flight(db.Model):
    """Flight in an Option"""

    __tablename__ = "flights"

    flight_id = db.Column(db.String(25), primary_key=True)
    option_id = db.Column(db.Integer, db.ForeignKey('options.option_id'), nullable=False)
    flight_price = db.Column(db.String(12), nullable=False)
    connection = db.Column(db.Boolean, nullable=False)
    connection_time = db.Column(db.Integer, nullable=True)

    # Define relationship to option
    option = db.relationship('Option', backref='flights')

    def __repr__(self):
        """Provide helpful representation when printed."""

        return ("<Flight flight_id=%s option_id=%s flight_price=%s connection=%s connection_time=%s>"
                % (self.flight_id, self.option_id, self.flight_price, self.connection, self.connection_time))



# Legs constituting a flight from QPX API
class Leg(db.Model):
    """Leg in a flight"""

    __tablename__ = "legs"

    leg_id = db.Column(db.String(16), primary_key=True)
    flight_id = db.Column(db.ForeignKey('flights.flight_id'), nullable=False)
    direction = db.Column(db.String(6), nullable=False)
    origin_airport = db.Column(db.ForeignKey('airports.airport_code'), nullable=False)
    departure_date = db.Column(db.DateTime, nullable=False)
    destination_airport = db.Column(db.ForeignKey('airports.airport_code'), nullable=False)
    leg_airline = db.Column(db.String(2), nullable=False)
    leg_code = db.Column(db.String(4), nullable=False)
    leg_time = db.Column(db.Integer, nullable=False)

    # Define relationship to flight, airport, and airport
    flight = db.relationship('Flight', backref='legs')
    airport = db.relationship('Airport', backref='origins') #help queue these two relationships
    airport = db.relationship('Airport', backref='destinations')

    def __repr__(self):
        """Provide helpful representation when printed."""

        return ("<Leg leg_id=%s flight_id=%s direction=%s origin_airport=%s" + 
                "departure_date=%s destination_airport=%s arrival_date=%s" + 
                "leg_airline=%s leg_code=%s leg_time=%s>"
                % (self.leg_id, self.flight_id, self.direction, self.origin_airport, 
                   self.departure_date, self.destination_airport, self.arrival_date, 
                   self.leg_airline, self.leg_code, self.leg_time))



# Airports by airport code that can be origins and destination IDs
class Airport(db.Model):
    """Airport by airport code"""

    __tablename__ = "airports"

    airport_code = db.Column(db.String(3), primary_key=True)
    airport_name = db.Column(db.String(500), nullable=False)
    airport_city = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        """Provide helpful representation when printed."""

        return ("<Airport airport_code=%s airport_name=%s airport_city=%s>"
                % (self.airport_code, self.airport_name, self.airport_city))

#################################################
# Helper functions

def connect_to_db(app):
    """Connect the database to our Flask app"""

    # Configure to use our PostgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://maggieyang:hackbright@localhost:5432/travels'
    db.app = app
    db.init_app(app)

if __name__ == "__main__":
    # Allows interaction directly with db from
    # server when running interactively

    from server import app
    connect_to_db(app)
    db.create_all()
    print "Connected to DB."