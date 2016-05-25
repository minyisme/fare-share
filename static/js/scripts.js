function tableResults(flights) {
    $("#flightResults").append("<p>Flight ID: " + flights[0]["flight_id"] + 
                               "</p><p>Flight Price: " + flights[0]["flight_price"] + "</p>");
    var results_table = "<table><thead><th>" + 
                "<td>Origin Airport</td>" + 
                "<td>Departure Datetime</td>" + 
                "<td>Destination Airport</td>" + 
                "<td>Arrival Time</td>" + 
                "<td>Flight ID</td>" + 
                "<td>Flight Duration</td>" + 
                "</th></thead><tbody>";
    for (i=0; i<flights[1].length; i++) {
        var origin_airport_code = flights[1][i]["origin_airport_code"];
        var departure_datetime = flights[1][i]["departure_datetime"];
        var destination_airport_code = flights[1][i]["destination_airport_code"];
        var arrival_datetime = flights[1][i]["arrival_datetime"];
        var leg_airline = flights[1][i]["leg_airline"];
        var leg_flight_code = flights[1][i]["leg_flight_code"];
        var leg_duration = flights[1][i]["leg_duration"];
        results_table += ("<tr><td>" + origin_airport_code + 
                     "</td><td>" + departure_datetime +
                     "</td><td>" + destination_airport_code + 
                     "</td><td>" + arrival_datetime + 
                     "</td><td>" + leg_airline + leg_flight_code + 
                     "</td><td>" + leg_duration + 
                     "</td></tr>");
    }
    results_table += "</tbody></table>";
    $("#flightResults").append(results_table);
}

function showFlightResults(result) {
    var flights = result["flights"];
    // debugger;
    tableResults(flights);
}

function searchQPX(evt) {

    var optionAttributes = {
        "destination" : $("#destination-airport-code").val(),
        "depart-date" : $("#depart-date").val(),
        "return-date" : $("#return-date").val(),
    };

    $.ajax({type: "POST",
        url: "/trip/" + tripId + "/search.json",
        data: optionAttributes,
        success: function (result) {
            debugger;
                 alert("option added");

                 for (var i=0; i<$("#qpx-query").data("origins").length; i++) {

                      // var originAirports = $(this).data("origins").split(",")
                        // debugger;
                      var queryInputs = {
                          "destination" : $("#destination-airport-code").val(),
                          "depart-date" : $("#depart-date").val(),
                          "return-date" : $("#return-date").val(),
                          "origin-airport-code" : $("#qpx-query").data("origins")[i],
                          "option-id" : result["option_id"],
                      };

                      $.ajax({type: "POST",
                          url: "/trip/" + tripId + "/results.json",
                          data: queryInputs,
                          success: showFlightResults,
                       });
                    }
        }
    });
}

$("#qpx-query").click(searchQPX);

function updateSearchQPX(evt) {
  for (var i=0; i<$("#qpx-reQuery").data("origins").length; i++) {

                      // var originAirports = $(this).data("origins").split(",")
                        // debugger;
                      var queryInputs = {
                          "destination" : $("#destination-airport-code-reQ").val(),
                          "depart-date" : $("#depart-date-reQ").val(),
                          "return-date" : $("#return-date-reQ").val(),
                          "origin-airport-code" : $("#qpx-reQuery").data("origins")[i],
                          "option-id" : $("#qpx-reQuery").data("option"),
                      };

                      $.ajax({type: "POST",
                          url: "/trip/" + reQTripId + "/results.json",
                          data: queryInputs,
                          success: showFlightResults,
                       });
                    }

}

$("#qpx-reQuery").click(updateSearchQPX);



////////////////////////////////////////////////////////////////////////////////

//Modal Window Actions

////////////////////////////////////////////////////////////////////////////////



// When the user clicks on the button, open the modal 
btn.onclick = function() {
    modal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
    modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}



////////////////////////////////////////////////////////////////////////////////

//Next Function

////////////////////////////////////////////////////////////////////////////////



function showConfirmation(result) {
    $("#myModal").hide();
    $("#votedForOption").val(voted_option_id)
}

function voteOption(evt, voted_option_id) {
    evt.preventDefault();     

    $("#votedForOption").text("You voted for option: " + voted_option_id)
    // debugger;
    $.ajax({type: "POST",
            url: "/trip/" + voteTripId + "/option-vote.json",
            data: {"voted-option-id": voted_option_id}, 
            showConfirmation
          });
}

$("#option-vote").on("submit", voteOption(voted_option_id));



////////////////////////////////////////////////////////////////////////////////

//Next Function

////////////////////////////////////////////////////////////////////////////////



function showAddedTrip(result) {
    $("#myModal").hide();
    $("#addTripConf").val("Trip Added")
}

function addTrip(evt) {
    evt.preventDefault();

    $.ajax({type: "POST",
      url: "/trip/create-new",
      data: {"trip_name": trip_name,
             "trip_user1": trip_user1,
             "trip_user2": trip_user2,
             "trip_user3": trip_user3,
             "trip_user4": trip_user4,},
      showAddedTrip
    });
}

$("#trip-add").on("submit", addTrip);


