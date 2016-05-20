"""Server for project"""

from jinja2 import StrictUndefined
from flask import Flask, render_template, redirect, request, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from flask_sqlalchemy import SQLAlchemy
from pprint import pprint

# File that holds my db classes and tables
from model import connect_to_db, db, User, Trip, UserTrip, Option, Flight, Leg, Airport

# File that holds my functionalities
import functions




app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

# Undefined variable in Jinja2 raises an error
app.jinja_env.undefined = StrictUndefined


################################################################################

## default pages routes ##

################################################################################



@app.route('/')
def index():
    """Homepage"""

    return render_template("homepage.html")



@app.route('/profile')
def profile():
    """User profile page"""

    # Get logged in user
    user = User.query.get(session['user_id'])
    # Get list of trips for user
    trips = functions.trips_by_user(user)

    return render_template("profile.html", user=user, trips=trips)



@app.route('/settings')
def settings():
    """User settings page"""

    return render_template("settings.html")



################################################################################

## login/logout routes ##

################################################################################



@app.route('/login', methods=["POST"])
def user_login():
    """Checks if email and password match in db
       and logs in user if match"""

    # Get email and password from the user login
    user_email = request.form.get('email')
    user_password = request.form.get('password')

    # Validate user_email and login and redirects depending on validity
    if functions.is_valid_login(user_email, user_password):
        return redirect('/profile')
    else:
        return redirect('/')



@app.route('/logout')
def user_logout():
    """Logs out user"""

    # Logs out user
    functions.logout()

    return redirect('/')



################################################################################

## user registration routes ##

################################################################################



@app.route('/user-reg-form')
def user_reg_form():
    """Takes user to user registration form"""

    # Takes user directly to user registration page without any checks
    return render_template('user_registration.html')



@app.route('/user-registration', methods=["POST"])
def user_registration():
    """Check if user in db, if not, add"""

    # Initialize empty dictionary for user info
    user_info = {}

    # Get inputs from user registration form
    user_info["user_email"] = request.form.get('email')
    user_info["user_password"] = request.form.get('password')
    user_info["user_name"] = request.form.get('username')
    user_info["user_origin_airport_code"] = request.form.get('origin_airport_code')

    # Checks if email is in the db already
    if functions.is_registered_email(user_info["user_email"]) == False:
        # Add user in db if email is not already in db
        functions.add_user_to_db(user_info)

    return redirect('/')



################################################################################

## trip adding routes ##

################################################################################



@app.route('/trip/add')
def trip_info():
    """Trip page"""

    return render_template("trip_add.html")



@app.route('/trip/create_new', methods=["POST"])
def trip_add():
    """Trip details page"""

    # Initialize empty dictionary to add trip info to
    trip_info = {}
    # Get trip name from form and add trip to db
    trip_info["trip_name"] = request.form.get("trip_name")
    # Add trip object to db and assign trip to variable
    trip = functions.add_trip_to_db(trip_info)

    # Initialize empty dictionary to add usertrip info to
    usertrip_info = {}
    # Get user_id from session
    usertrip_info["user_id"] = session["user_id"]
    # Get trip_id from trip
    usertrip_info["trip_id"] = trip.trip_id
    # Add usertrip object to db
    functions.add_usertrip_to_db(usertrip_info)

    # Initialize empty list for user emails
    emails = []
    # Add user emails from form to user_emails list
    for x in range(5):
        if request.form.get("trip_user%s" %(x)):
            emails.append(request.form.get("trip_user%s" %(x)))

    # For all emails entered in input
    for email in emails:
        # Validates if email in db
        if functions.is_registered_email(email):
            # Get user from registered email
            user = User.query.filter_by(email=email).first()
            # Get usertrip_info
            usertrip_info = {"user_id":user.user_id, "trip_id":trip.trip_id}
            # Add usertrip to db
            functions.add_usertrip_to_db(usertrip_info)
        # Else flash user not in db
        else:
            flash("User not in db: " + email)

    return redirect("/profile")



################################################################################

## trip details, search/result, and share routes ##

################################################################################



@app.route('/trip/<int:trip_id>')
def trip_detail(trip_id):
    """Display trip details page"""

    # Get trip from trip_id
    trip = Trip.query.get(trip_id)
    # Get all options for a trip
    options = trip.options
    
    return render_template("trip_detail.html", trip=trip, options=options)



@app.route('/trip/<int:trip_id>/search')
def trip_search(trip_id):
    """Search flights"""

    trip = Trip.query.get(trip_id)

    return render_template("trip_search.html", trip=trip)



@app.route('/trip/<int:trip_id>/results', methods=["POST"])
def trip_results(trip_id):
    """Search flights results"""

    # Get trip from trip_id
    trip = Trip.query.get(trip_id)

    # Initializes empty dictionary to add option info to
    option_info = {}
    # Get destination, departure_date, return_date from form and add to option_info
    option_info["destination"] = request.form.get("destination")
    option_info["departure_date"] = request.form.get("departure_date")
    option_info["return_date"] = request.form.get("departure_date")
    # Add trip_id to option_info
    option_info["trip_id"] = trip_id

    # Add option to db and return option object
    option = functions.add_option_to_db(option_info)

    # Get origin airport codes for trip
    origin_airport_codes = functions.origin_airport_codes_by_trip(trip)

    # Get parameter variables for QPX search from input option and origin_airport_codes
    params = functions.get_params(origin_airport_codes, option_info)

    # Initialize empty results list to add QPX query restuls to
    python_results = []
    # For each set of parameter variables in params
    for query in params:
        # Get the parameter string from the parameter variables
        parameter = functions.parameter_by_params(query)
        # Make request to QPX
        flight_request = functions.query_QPX(parameter)
        # Read results from QPX into python
        python_result = functions.QPX_results(flight_request)
        #add python_result to python_results
        python_results.append(python_result)

    # Parse python results to add flights and legs to db and to get data to render on 
    # results page
    flights = functions.parse_results(python_results, option)

    # Trip results page with all the data necessary for tables
    return render_template("trip_search_results.html", option=option, flights=flights, trip=trip)



@app.route('/trip/share')
def trip_share():
    """Share trip with other users"""

    return render_template("trip_share.html")



################################################################################

## End routes ##

################################################################################



if __name__ == "__main__":
    # Debug to be turned off for production
    app.debug = True

    connect_to_db(app)

    # Use DebugToolbar
    DebugToolbarExtension(app)

    # Runs app
    app.run()
