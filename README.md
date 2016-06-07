<dl id="fare-share"></dl>
# Fare Share

Fare Share is an app built for friends living in different cities who want to travel together. It allows each user to create trips for a group of users. All users of that trip can then one-click-search flights for everyone in the group. The app uses the Google Flights API to find the cheapest dates/destinations for everyone on the trip. All search results in a trip are then viewable by all users of that trip, and all users can then vote for their preferred option for that trip. With easy-to-view Google Maps of flight paths and Chart.js summaries of the flight prices, Fare Share makes it easier for friends living all over to plan travel together.

## Table of Contents
- [Tech Stack](#tech-stack)
- [Features](#features)
    - [Landing Page](#landing-page)
    - [Profile Page](#profile-page)
    - [Trip Page](#trip-page)
    - [Search Page](#search-page)
- [Data Model](#data-model)

<dl id="tech-stack"></dl>
## Tech Stack                   


##### Backend

Python, Flask, SQLAlchemy, PostgreSQL

##### Frontend

JavaScript, jQuery, AJAX, Jinja2, HTML, CSS, jQuery UI, Chart.js

##### APIs

Google Flights API
Google Maps API

<p align="right">[Back to Top](#fare-share)</p>
<dl id="features"></dl>
## Features                     [Back to Top](#fare-share)

<dl id="landing-page"></dl>
##### Landing Page              [Back to Top](#fare-share)

![alt text](https://github.com/minyisme/fare-share/blob/master/static/images/landing_page.png)

- User specifies a home airport during sign up
![alt text](https://github.com/minyisme/fare-share/blob/master/static/images/sign_up.png)

<dl id="profile-page"></dl>
##### Profile Page              [Back to Top](#fare-share)

![alt text](https://github.com/minyisme/fare-share/blob/master/static/images/profile.png)

- Display tiles of all trips belonging to user
- User can click on "trash" glyphicons to delete trips
- User can add a new trip, specifying other users on the trip

![alt text](https://github.com/minyisme/fare-share/blob/master/static/images/add_trip.png)

<dl id="trip-page"></dl>
##### Trip Page                 [Back to Top](#fare-share)

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
- Displays flight details for all travelers for each flight option with:
    - Glyphicon to delete option
    - Glyphicon to update option results
![alt text](https://github.com/minyisme/fare-share/blob/master/static/images/option_details.png)

<dl id="search-page"></dl>
##### Search Page               [Back to Top](#fare-share)

![alt text](https://github.com/minyisme/fare-share/blob/master/static/images/search.png)

- Allows user to flight search with:
    - autocomplete feature on airport
![alt text](https://github.com/minyisme/fare-share/blob/master/static/images/autocomplete.png)
    - datepicker feature on dates
![alt text](https://github.com/minyisme/fare-share/blob/master/static/images/datepicker.png)
- Shows results from Google Flights API 
![alt text](https://github.com/minyisme/fare-share/blob/master/static/images/results.png)

<dl id="data-model"></dl>
## Data Model                   [Back to Top](#fare-share)

![alt text](https://github.com/minyisme/fare-share/blob/master/static/images/data_model.png)


<!-- [![Coverage Status](https://coveralls.io/repos/github/minyisme/totally-named-project-yo/badge.svg?branch=master)](https://coveralls.io/github/minyisme/totally-named-project-yo?branch=master) -->
