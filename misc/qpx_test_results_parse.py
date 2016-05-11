import json
from pprint import pprint

with open('qpx_test_results.json') as results_file:
    data = json.load(results_file)

#prints data tabbed
# pprint(data)

#dictionary
print type(data)

for i in range(len(data["trips"]["tripOption"])):
    flight_id = data["trips"]["tripOption"][i]["id"]
    flight_duration = data["trips"]["tripOption"][i]["slice"][0]["duration"]
    flight_fare = data["trips"]["tripOption"][i]["pricing"][0]["saleFareTotal"]
    flight_tax = data["trips"]["tripOption"][i]["pricing"][0]["saleTaxTotal"]
    flight_total = data["trips"]["tripOption"][i]["pricing"][0]["saleTotal"]

    print (flight_id, flight_duration, flight_fare, flight_tax, flight_total)

    segment_data = data["trips"]["tripOption"][i]["slice"][0]["segment"]
    
    for x in range(len(segment_data)):
        leg_origin = segment_data[x]["leg"][0]["origin"]
        leg_departure = segment_data[x]["leg"][0]["departureTime"]
        leg_destination = segment_data[x]["leg"][0]["destination"]
        leg_arrival = segment_data[x]["leg"][0]["arrivalTime"]
        print (leg_origin, leg_departure, leg_destination, leg_arrival)


# "flight_id:%s\nflight_duration%i\nflight_fare%s\nflight_tax%s\nflight_total" %

    # for x in range(len(data["trips"]["tripOption"][i]["slice"][0]["segment"][0]["leg"])):
    #     print data["trips"]["tripOption"][i]["slice"][0]["segment"][0]["leg"][x]["origin"], data["trips"]["tripOption"][i]["slice"][0]["segment"][0]["leg"][x]["departureTime"], data["trips"]["tripOption"][i]["slice"][0]["segment"][0]["leg"][x]["destination"], data["trips"]["tripOption"][i]["slice"][0]["segment"][0]["leg"][x]["arrivalTime"]