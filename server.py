"""Server for project"""

from jinja2 import StrictUndefined
from flask import Flask, render_template, redirect, request, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from flask_sqlalchemy import SQLAlchemy

from model import connect_to_db, db, User, Trip, UserTrip, Option, Flight, Leg, Airport

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

    # print session["user_id"]

    # Get all trips for this user to display on profile page
    user = User.query.filter_by(user_id=session["user_id"]).first()

    usertrip_list = UserTrip.query.filter_by(user_id = user.user_id).all()
    # print usertrip_list

    trip_list = []

    for usertrip in usertrip_list:
        trip_list.append(Trip.query.filter_by(trip_id=usertrip.trip_id).first())

    # print trip_list

    return render_template("profile.html", trip_list=trip_list)



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

    # Check User db for email and password match
    # If match, add to session to indicate logged in user
    # Else, prompt to try again
    if User.query.filter_by(email=user_email, password=user_password).first():
        flash("Yay you're back!!!!!")
        logged_in_user = User.query.filter_by(email=user_email, password=user_password).first()
        session["user_id"] = logged_in_user.user_id
        return redirect('/profile')
    else:
        flash("Forgot your password you idiot! Try again.")
        return redirect('/')



@app.route('/logout')
def user_logout():
    """Logs out user"""

    # Deletes user_id from session when logging out
    del session["user_id"]

    flash("Don't leave meeeee!!!! :( ")

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

    # Get email and password from user reg form
    user_email = request.form.get('email')
    user_password = request.form.get('password')
    user_name = request.form.get('username')
    user_origin_airport_code = request.form.get('origin_airport_code')

    # Checks if user email is already registered
    if User.query.filter_by(email=user_email).first():
        flash("This email is already taken; please log in.")
    else:
        user = User(email=user_email, 
                    password=user_password,
                    user_name=user_name,
                    origin_airport_code=user_origin_airport_code)

        db.session.add(user)

        db.session.commit()

        flash("Thank you for registering; please log in.")

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

    # Get trip name from form and add trip to db
    trip_name = request.form.get("trip_name")

    trip = Trip(trip_name=trip_name)

    db.session.add(trip)

    db.session.commit()

    # Adding usertrip for user who's logged in to the db
    user_id = session["user_id"]

    usertrip = UserTrip(user_id=user_id, trip_id=trip.trip_id)

    db.session.add(usertrip)

    db.session.commit()
    # For user emails entered in form, add usertrip to db if user email valid
    # Else for email, flash email not in db
    for x in range(5):
        if request.form.get("trip_user%s" %(x)):
            user_email = request.form.get("trip_user%s" %(x))
            if User.query.filter_by(email=user_email).first():
                user = User.query.filter_by(email=user_email).first()
                usertrip = UserTrip(user_id=user.user_id,
                                    trip_id=trip.trip_id)

                db.session.add(usertrip)

                db.session.commit()

            else:
                flash("User not in db: " + user_email)

    return redirect("/profile")



################################################################################

## trip details, search/result, and share routes ##

################################################################################



@app.route('/trip/<int:trip_id>')
def trip_detail(trip_id):
    """Display trip details page"""

    trip = Trip.query.get(trip_id)
    
    return render_template("trip_detail.html", trip=trip)


@app.route('/trip/<int:trip_id>/search')
def trip_search(trip_id):
    """Search flights"""

    trip = Trip.query.get(trip_id)

    return render_template("trip_search.html", trip=trip)



@app.route('/trip/<int:trip_id>/results', methods=["POST"])
def trip_results(trip_id):
    """Search flights results"""

    # Get trip
    trip = Trip.query.get(trip_id)

    # Get all origin airport codes to search from users attached to trip
    origin_airport_codes = []
    for usertrip in trip.usertrips:
        origin_airport_codes.append(usertrip.user.origin_airport_code)

    print origin_airport_codes

    # Get destination, departure_date, return_date from form
    destination = request.form.get("destination")
    departure_date = request.form.get("departure_date")
    return_date = request.form.get("departure_date")

    # Add search option to database
    option = Option(trip_id=trip_id, destination_airport_code=destination, 
                    depart_date=departure_date, return_date=return_date)

    db.session.add(option)

    db.session.commit()

    # Add search parameters to search params to send to search QPX function
    params = []
    count = 0
    for origin_airport_code in origin_airport_codes:
        params.append({})
        params[count]["num_travelers"] = 1
        params[count]["flight_origin"] = origin_airport_code
        params[count]["flight_destination"] = destination
        params[count]["departure_date"] = departure_date
        params[count]["return_date"] = return_date
        params[count]["max_price"] = "USD10000"
        count += 1

    print params

    # Make call to QPX with flight searches
    python_results = functions.flight_query(params)
    print python_results

    # Parse results to display on results page
    flight_results_data = functions.flight_query_results(python_results)
    print flight_results_data

    # Trip results page with all the data necessary for tables
    return render_template("trip_search_results.html", results=flight_results_data)



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
