<dl id="fare-share"></dl>
# Fare Share

Fare Share is an app built for friends living in different cities who want to travel together. It allows each user to create trips for groups of users. All users of that trip can then one-click-search flights for everyone in the group. The app then aggregates all the origin airports of users to query the Google Flights API, and finds the cheapest dates/destinations for everyone on the trip. All search results in a trip are then viewable by all users of that trip, and all users can then vote for their preferred option for that trip. With easy-to-view Google Maps of flight paths and Chart.js summaries of the flight prices and vote tallies, Fare Share makes it easy for friends living all over the wold to plan travel together.

## Table of Contents
- [Tech Stack](#tech-stack)
- [Features](#features)
    - [Landing Page](#landing-page)
    - [Profile Page](#profile-page)
    - [Trip Page](#trip-page)
    - [Search Page](#search-page)
- [Data Model](#data-model)
- [Get Fare Share](#set-up)
- [Fare Share 2.0](#future)

<dl id="tech-stack"></dl>
## Tech Stack                   


##### Backend

[Python](https://www.python.org/), [Flask](http://flask.pocoo.org/), [SQLAlchemy](http://www.sqlalchemy.org/), [PostgreSQL](https://www.postgresql.org/)

##### Frontend

JavaScript, [jQuery](https://jquery.com/), AJAX, [Jinja2](http://jinja.pocoo.org/docs/dev/), HTML, CSS, [jQuery UI](https://jqueryui.com/), [Chart.js](http://www.chartjs.org/)

##### APIs

[Google Flights API](https://developers.google.com/qpx-express/), [Google Maps API](https://developers.google.com/maps/)

[Back to Top](#fare-share)
<dl id="features"></dl>
## Features

<dl id="landing-page"></dl>
##### Landing Page

![alt text](https://github.com/minyisme/fare-share/blob/master/static/images/landing_page.png)

- User specifies a home airport during sign up
![alt text](https://github.com/minyisme/fare-share/blob/master/static/images/sign_up1.png)

[Back to Top](#fare-share)
<dl id="profile-page"></dl>
##### Profile Page

![alt text](https://github.com/minyisme/fare-share/blob/master/static/images/profile1.png)

- Display tiles of all trips belonging to user
- User can click on "trash" glyphicons to delete trips
- User can add a new trip, specifying other users on the trip

![alt text](https://github.com/minyisme/fare-share/blob/master/static/images/add_trip.png)

[Back to Top](#fare-share)
<dl id="trip-page"></dl>
##### Trip Page

![alt text](https://github.com/minyisme/fare-share/blob/master/static/images/trip1.png)

- Displays trip details with links to:
    - modal window of travelers for this trip
    - modal window to vote for a flight option for the trip
    - search for new flight options for the trip
- Displays visuals:
    - Google Map of flight paths for all options
    - Chart.js chart of all options by price
![alt text](https://github.com/minyisme/fare-share/blob/master/static/images/options_prices1.png)
    - Chart.js chart of all options by user votes
![alt text](https://github.com/minyisme/fare-share/blob/master/static/images/options_votes1.png)
- Displays flight details for all travelers for each flight option with:
    - Glyphicon to delete option
    - Glyphicon to update option results
![alt text](https://github.com/minyisme/fare-share/blob/master/static/images/option_details1.png)

[Back to Top](#fare-share)
<dl id="search-page"></dl>
##### Search Page

![alt text](https://github.com/minyisme/fare-share/blob/master/static/images/search1.png)

- Allows user to flight search with:
    - autocomplete feature on airport
![alt text](https://github.com/minyisme/fare-share/blob/master/static/images/autocomplete.png)
    - datepicker feature on dates
![alt text](https://github.com/minyisme/fare-share/blob/master/static/images/datepicker.png)
- Displays results from Google Flights API through individual AJAX calls 
![alt text](https://github.com/minyisme/fare-share/blob/master/static/images/results.png)

[Back to Top](#fare-share)
<dl id="data-model"></dl>
## Data Model

![alt text](https://github.com/minyisme/fare-share/blob/master/static/images/data_model.png)

[Back to Top](#fare-share)
<dl id="set-up"></dl>
## Get Fare Share

Clone or fork this repo:

```
https://github.com/minyisme/fare-share
```

Create and activate a virtual environment inside your project directory:

```
virtualenv env
source env/bin/activate
```

Install the requirements:

```
pip install -r requirements.txt
```

Grab your own secret key for Google Flights API and save it to secrets.sh:

```
QPX_KEY
```

Set up your database and seed airport data:

```
python model.py
python seed.py
```

Start running your server:

```
python server.py
```

Navigate to 'localhost:5000/' and have fun trip planning!

[Back to Top](#fare-share)
<dl id="future"></dl>
## For Version 2.0

- **Search by region:** Allow users to search destinations by region, country, or continent
- **Interactive map and charts:** Map markers and chart columns to be interactive
- **Password hashing:** Passwords will be hashed before being saved in DB
- **Trip images:** Allow users to upload images for each trip tile
- **Deployment:** Deployment coming soon!

[Back to Top](#fare-share)
<!-- [![Coverage Status](https://coveralls.io/repos/github/minyisme/totally-named-project-yo/badge.svg?branch=master)](https://coveralls.io/github/minyisme/totally-named-project-yo?branch=master) -->
