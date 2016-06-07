# Fare Share

Fare Share is an app built for friends living in different cities who want to travel together. It allows each user to create trips for a group of users. All users of that trip can then one-click-search flights for everyone in the group. The app uses the Google Flights API to find the cheapest dates/destinations for everyone on the trip. All search results in a trip are then viewable by all users of that trip, and all users can then vote for their preferred option for that trip. With easy-to-view Google Maps of flight paths and Chart.js summaries of the flight prices, Fare Share makes it easier for friends living all over to plan travel together.

## Tech Stack

##### Backend

Python, Flask, SQLAlchemy, PostgreSQL

##### Frontend

JavaScript, jQuery, AJAX, Jinja2, HTML, CSS, jQuery UI, Chart.js

##### APIs

Google Flights API
Google Maps API

## Features

##### Landing Page

![alt text](https://github.com/minyisme/fare-share/blob/master/static/images/landing_page.png)

##### User Sign Up

- User specifies a home airport during sign up

![alt text](https://github.com/minyisme/fare-share/blob/master/static/images/sign_up.png)

##### Profile Page

![alt text](https://github.com/minyisme/fare-share/blob/master/static/images/profile.png)

- Display tiles of all trips belonging to user
- User can click on "trash" glyphicons to delete trips
- User can create a trip, specifying other users on the trip

![alt text](https://github.com/minyisme/fare-share/blob/master/static/images/add_trip.png)

##### Trip Page

![alt text](https://github.com/minyisme/fare-share/blob/master/static/images/trip.png)

- Displays trip details with links to:
    - modal window of travelers for this trip
    - modal window to vote for a flight option for the trip
    - search for new flight options for the trip
- Displays visuals:
    - Google Map of flight paths for all options
    - Chart.js chart of all options by price
![alt text](https://github.com/minyisme/fare-share/blob/master/static/images/options_prices.png)
    - Chart.js chart of all options by user votes
![alt text](https://github.com/minyisme/fare-share/blob/master/static/images/options_votes.png)

## Data Model

![alt text](https://github.com/minyisme/fare-share/blob/master/static/images/data_model.png)


<!-- [![Coverage Status](https://coveralls.io/repos/github/minyisme/totally-named-project-yo/badge.svg?branch=master)](https://coveralls.io/github/minyisme/totally-named-project-yo?branch=master) -->
