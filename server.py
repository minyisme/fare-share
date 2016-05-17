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

@app.route('/')
def index():
    """Homepage"""

    return render_template("homepage.html")



@app.route('/profile')
def profile():
    """User profile page"""

    print session["user_id"]

    user = User.query.filter_by(user_id=session["user_id"]).first()

    trip_list = UserTrip.query.filter_by(user_id = user.user_id).all()
    print trip_list

    return render_template("profile.html")



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



@app.route('/settings')
def settings():
    """User settings page"""

    return render_template("settings.html")



@app.route('/trip/add')
def trip_info():
    """Trip page"""

    return render_template("trip_add.html")



@app.route('/trip/create_new', methods=["POST"])
def trip_details():
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



@app.route('/trip/trip_id')
def trip():
    pass



@app.route('/trip/search')
def trip_search():
    """Search flights"""

    return render_template("trip_search.html")



@app.route('/trip/results', methods=["POST"])
def trip_results():
    """Search flights results"""

    # Get search parameters from Flight Search Form
    num_origins = int(request.form.get("num_origins"))

    params = []
    for num in range(0, num_origins):
        params.append({})
        num_travelers = request.form.get("num_travelers%s" %num)
        params[num]["num_travelers"] = num_travelers
        flight_origin = request.form.get("flight_origin%s" %num)
        params[num]["flight_origin"] = flight_origin
        flight_destination = request.form.get("flight_destination%s" %num)
        params[num]["flight_destination"] = flight_destination
        departure_date = request.form.get("departure_date%s" %num)
        params[num]["departure_date"] = departure_date
        return_date = request.form.get("return_date%s" %num)
        params[num]["return_date"] = return_date
        max_price = request.form.get("max_price%s" %num)
        max_price = "USD" + max_price
        params[num]["max_price"] = max_price

    flight_results_data = functions.flight_query(params)

    # Trip results page with all the data necessary for tables
    return render_template("trip_search_results.html", results=flight_results_data)



@app.route('/trip/share')
def trip_share():
    """Share trip with other users"""

    return render_template("trip_share.html")



if __name__ == "__main__":
    # Debug to be turned off for production
    app.debug = True

    connect_to_db(app)

    # Use DebugToolbar
    DebugToolbarExtension(app)

    # Runs app
    app.run()
