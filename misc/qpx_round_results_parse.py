import json

with open('qpx_round_results.json') as results:
    python_results=json.load(results)

# # For each flight option, get id, duration, fare, tax, total fare
# # for i in range(len(python_results["trips"]["tripOption"])):
# #     flight_id = python_results["trips"]["tripOption"][i]["id"]
# #     flight_duration = python_results["trips"]["tripOption"][i]["slice"][0]["duration"]
# #     flight_fare = python_results["trips"]["tripOption"][i]["pricing"][0]["saleFareTotal"]
# #     flight_tax = python_results["trips"]["tripOption"][i]["pricing"][0]["saleTaxTotal"]
# #     flight_total = python_results["trips"]["tripOption"][i]["pricing"][0]["saleTotal"]

# #     # Wrap all flight data for one flight into one dictionary item
# #     flight_data[i] = [flight_id, flight_duration, flight_fare, flight_tax, flight_total]

# #     # Create segment_data variable to do less repetitive typing
# #     segment_data = python_results["trips"]["tripOption"][i]["slice"][0]["segment"]

# #     # For each segment inside each flight append all the legs and info to dict

# #     for x in range(len(segment_data)):
# #         flight_data[i].append([])
# #         for y in range(len(segment_data["leg"])):
# #             leg_origin = segment_data[x]["leg"][y]["origin"]
# #             leg_departure = segment_data[x]["leg"][y]["departureTime"]
# #             leg_destination = segment_data[x]["leg"][y]["destination"]
# #             leg_arrival = segment_data[x]["leg"][y]["arrivalTime"]
# #             flight_data[i][5].append([leg_origin, leg_departure, leg_destination, leg_arrival])

# # print flight_data

# # Commented out to test return flights
# # return render_template("trip_results.html", results=flight_data)

# for i in range(len(python_results["trips"]["tripOption"])):
#     print python_results["trips"]["tripOption"][i]
#     print "\n\n\n"

# {   u'saleTotal': u'USD393.20', 
#     u'kind': u'qpxexpress#tripOption', 
#     u'slice': [{u'duration': 329, 
#                 u'kind': u'qpxexpress#sliceInfo', 
#                 u'segment': [{  u'kind': u'qpxexpress#segmentInfo', 
#                                 u'bookingCodeCount': 1, 
#                                 u'flight': {u'carrier': u'VX', 
#                                             u'number': u'26'}, 
#                                 u'leg': [{  u'origin': u'SFO', 
#                                             u'originTerminal': u'2', 
#                                             u'departureTime': u'2016-06-11T15:15-07:00', 
#                                             u'destinationTerminal': u'4', 
#                                             u'secure': True, 
#                                             u'destination': u'JFK', 
#                                             u'kind': u'qpxexpress#legInfo', 
#                                             u'aircraft': u'320', 
#                                             u'onTimePerformance': 69, 
#                                             u'arrivalTime': u'2016-06-11T23:44-04:00', 
#                                             u'duration': 329, 
#                                             u'id': u'LRtjxsr0YG0VaplO', 
#                                             u'mileage': 2579}], 
#                                 u'bookingCode': u'L', 
#                                 u'duration': 329, 
#                                 u'id': u'GVqHJREx7hDNjzhX', 
#                                 u'cabin': u'COACH', 
#                                 u'marriedSegmentGroup': u'0'
#                             }]
#                 }, 
#                 {u'duration': 375, 
#                 u'kind': u'qpxexpress#sliceInfo', 
#                 u'segment': [{  u'kind': u'qpxexpress#segmentInfo', 
#                                 u'bookingCodeCount': 5, 
#                                 u'flight': {u'carrier': u'VX', 
#                                             u'number': u'11'}, 
#                                 u'leg': [{  u'origin': u'JFK', 
#                                             u'originTerminal': u'4', 
#                                             u'departureTime': u'2016-06-21T07:30-04:00', 
#                                             u'destinationTerminal': u'2', 
#                                             u'secure': True, 
#                                             u'destination': u'SFO', 
#                                             u'kind': u'qpxexpress#legInfo', 
#                                             u'aircraft': u'320', 
#                                             u'onTimePerformance': 94, 
#                                             u'arrivalTime': u'2016-06-21T10:45-07:00', 
#                                             u'duration': 375, 
#                                             u'id': u'LYc8ZeGkZz19Ua2l', 
#                                             u'mileage': 2579}], 
#                                 u'bookingCode': u'S', 
#                                 u'duration': 375, 
#                                 u'id': u'GmK69GxW5bAq09iv', 
#                                 u'cabin': u'COACH', 
#                                 u'marriedSegmentGroup': u'1'
#                             }]
#                 }], 
#     u'id': u'C1TDtZ534dKQihoVN4pVNS001', 
#     u'pricing': [{u'fare': [{   u'origin': u'SFO', 
#                                 u'basisCode': u'L21NR', 
#                                 u'kind': u'qpxexpress#fareInfo', 
#                                 u'destination': u'NYC', 
#                                 u'carrier': u'VX', 
#                                 u'id': u'AvP2wPPE7knId2h/jPZGX9mZ6Uo5TmsGm8S/Jy6FBwZQ'
#                             }, 
#                             {   u'origin': u'NYC', 
#                                 u'basisCode': u'S21SP', 
#                                 u'kind': u'qpxexpress#fareInfo', 
#                                 u'destination': u'SFO', 
#                                 u'carrier': u'VX', 
#                                 u'id': u'A/m4jpdhCIIYekyyGR+sEbx1VDNtIfE4pfwpYHitiwxo'
#                             }], 
#                 u'saleTotal': u'USD393.20', 
#                 u'kind': u'qpxexpress#pricingInfo', 
#                 u'segmentPricing': [{   u'kind': u'qpxexpress#segmentPricing', 
#                                         u'fareId': u'A/m4jpdhCIIYekyyGR+sEbx1VDNtIfE4pfwpYHitiwxo', 
#                                         u'segmentId': u'GmK69GxW5bAq09iv'
#                                     }, 
#                                     {   u'kind': u'qpxexpress#segmentPricing', 
#                                         u'fareId': u'AvP2wPPE7knId2h/jPZGX9mZ6Uo5TmsGm8S/Jy6FBwZQ', 
#                                         u'segmentId': u'GVqHJREx7hDNjzhX'
#                                     }], 
#                 u'passengers': {u'kind': u'qpxexpress#passengerCounts', 
#                                 u'adultCount': 1}, 
#                 u'ptc': u'ADT', 
#                 u'tax': [{  u'kind': u'qpxexpress#taxInfo', 
#                             u'code': u'US', 
#                             u'country': u'US', 
#                             u'salePrice': u'USD25.46', 
#                             u'chargeType': u'GOVERNMENT', 
#                             u'id': u'US_001'
#                         }, 
#                         {   u'kind': u'qpxexpress#taxInfo', 
#                             u'code': u'AY', 
#                             u'country': u'US', 
#                             u'salePrice': u'USD11.20', 
#                             u'chargeType': u'GOVERNMENT', 
#                             u'id': u'AY_001'
#                         }, 
#                         {   u'kind': u'qpxexpress#taxInfo', 
#                             u'code': u'XF', 
#                             u'country': u'US', 
#                             u'salePrice': u'USD9.00', 
#                             u'chargeType': u'GOVERNMENT', 
#                             u'id': u'XF'
#                         }, 
#                         {   u'kind': u'qpxexpress#taxInfo', 
#                             u'code': u'ZP', u'country': u'US', 
#                             u'salePrice': u'USD8.00', 
#                             u'chargeType': u'GOVERNMENT', 
#                             u'id': u'ZP'
#                         }], 
#                 u'fareCalculation': u'SFO VX NYC 181.40L21NR VX SFO 158.14S21SP USD 339.54 END ZP SFO JFK XT 25.46US 8.00ZP 11.20AY 9.00XF SFO4.50 JFK4.50', 
#                 u'saleFareTotal': u'USD339.54', 
#                 u'baseFareTotal': u'USD339.54', 
#                 u'saleTaxTotal': u'USD53.66', 
#                 u'latestTicketingTime': u'2016-05-12T23:59-04:00'
#                 }]
# }


# for i in range(len(python_results["trips"]["tripOption"])):
#     print "Round trip flight option %s" %(i)
#     flight_data = python_results["trips"]["tripOption"]
#     flight_id = flight_data[i]["id"]
#     flight_price = flight_data[i]["saleTotal"]
#     slice_data = python_results["trips"]["tripOption"][i]["slice"]
#     print "\n\n\n"


# # Round trip flight option 0
# [{  u'duration': 329, 
#     u'kind': u'qpxexpress#sliceInfo', 
#     u'segment': 
#         [{  u'kind': u'qpxexpress#segmentInfo', 
#             u'bookingCodeCount': 1, 
#             u'flight': {u'carrier': u'VX', 
#                         u'number': u'26'}, 
#             u'leg': [{  u'origin': u'SFO', 
#                         u'originTerminal': u'2', 
#                         u'departureTime': u'2016-06-11T15:15-07:00', 
#                         u'destinationTerminal': u'4', 
#                         u'secure': True, 
#                         u'destination': u'JFK', 
#                         u'kind': u'qpxexpress#legInfo', 
#                         u'aircraft': u'320', 
#                         u'onTimePerformance': 69, 
#                         u'arrivalTime': u'2016-06-11T23:44-04:00', 
#                         u'duration': 329, 
#                         u'id': u'LRtjxsr0YG0VaplO', 
#                         u'mileage': 2579}], 
#             u'bookingCode': u'L', 
#             u'duration': 329, 
#             u'id': u'GVqHJREx7hDNjzhX', 
#             u'cabin': u'COACH', 
#             u'marriedSegmentGroup': u'0'
#         }]
# },
# {   u'duration': 375, 
#     u'kind': u'qpxexpress#sliceInfo', 
#     u'segment': 
#         [{  u'kind': u'qpxexpress#segmentInfo', 
#             u'bookingCodeCount': 5, 
#             u'flight': {u'carrier': u'VX', 
#                         u'number': u'11'}, 
#             u'leg': [{  u'origin': u'JFK', 
#                         u'originTerminal': u'4', 
#                         u'departureTime': u'2016-06-21T07:30-04:00', 
#                         u'destinationTerminal': u'2', 
#                         u'secure': True, 
#                         u'destination': u'SFO', 
#                         u'kind': u'qpxexpress#legInfo', 
#                         u'aircraft': u'320', 
#                         u'onTimePerformance': 94, 
#                         u'arrivalTime': u'2016-06-21T10:45-07:00', 
#                         u'duration': 375, 
#                         u'id': u'LYc8ZeGkZz19Ua2l', 
#                         u'mileage': 2579}], 
#             u'bookingCode': u'S', 
#             u'duration': 375, 
#             u'id': u'GmK69GxW5bAq09iv', 
#             u'cabin': u'COACH', 
#             u'marriedSegmentGroup': u'1'
#         }]
# }]


# for x in range(len(python_results["trips"]["tripOption"])):
#     print "Round trip flight option %s" %(x)
#     flight_data = python_results["trips"]["tripOption"]
#     flight_id = flight_data[i]["id"]
#     flight_price = flight_data[i]["saleTotal"]
#     slice_data = python_results["trips"]["tripOption"][x]["slice"]
#     dep_ret = ["Departure", "Return"]
#     for y in range(len(slice_data)):
#         print "%s Flight" %(dep_ret[y])
#         flight_duration = slice_data[y]["duration"]
#         print slice_data[y]["segment"]
#         print "\n\n\n\n"
#     print "\n\n\n"


# [{  u'kind': u'qpxexpress#segmentInfo', 
#     u'bookingCodeCount': 7, 
#     u'flight': {u'carrier': u'VX', 
#                 u'number': u'924'}, 
#     u'leg': [{  u'origin': u'SFO', 
#                 u'originTerminal': u'2', 
#                 u'departureTime': u'2016-06-11T11:55-07:00', 
#                 u'destinationTerminal': u'3', 
#                 u'secure': True, 
#                 u'destination': u'LAX', 
#                 u'kind': u'qpxexpress#legInfo', 
#                 u'aircraft': u'320', 
#                 u'onTimePerformance': 100, 
#                 u'arrivalTime': u'2016-06-11T13:15-07:00', 
#                 u'duration': 80, 
#                 u'id': u'Ly+pZSObzaxJ6Q2q', 
#                 u'mileage': 337}], 
#     u'connectionDuration': 135, 
#     u'bookingCode': u'L', 
#     u'duration': 80, 
#     u'id': u'Gg+cCS6D7qMO-ju6', 
#     u'cabin': u'COACH', 
#     u'marriedSegmentGroup': u'0'
# }, 
# {   u'kind': u'qpxexpress#segmentInfo', 
#     u'bookingCodeCount': 7, 
#     u'flight': {u'carrier': u'VX', u'number': u'416'}, 
#     u'leg': [{  u'origin': u'LAX', 
#                 u'originTerminal': u'3', 
#                 u'departureTime': u'2016-06-11T15:30-07:00', 
#                 u'destinationTerminal': u'4', 
#                 u'secure': True, 
#                 u'destination': u'JFK', 
#                 u'kind': u'qpxexpress#legInfo', 
#                 u'aircraft': u'320', 
#                 u'onTimePerformance': 70, 
#                 u'arrivalTime': u'2016-06-11T23:59-04:00', 
#                 u'duration': 329, 
#                 u'id': u'LB+vZOwvREq7tbs9', 
#                 u'mileage': 2468}], 
#     u'bookingCode': u'L', 
#     u'duration': 329, 
#     u'id': u'G3hlPibIfauEPKnJ', 
#     u'cabin': u'COACH', 
#     u'marriedSegmentGroup': u'1'
# }]
            

# for x in range(len(python_results["trips"]["tripOption"])):
#     print "Round trip flight option %s" %(x)
#     flight_data = python_results["trips"]["tripOption"]
#     flight_id = flight_data[i]["id"]
#     flight_price = flight_data[i]["saleTotal"]
#     slice_data = python_results["trips"]["tripOption"][x]["slice"]
#     dep_ret = ["Departure", "Return"]
#     for y in range(len(slice_data)):
#         print "%s Flight" %(dep_ret[y])
#         flight_duration = slice_data[y]["duration"]
#         segment_data = slice_data[y]["segment"]
#         for z in range(len(segment_data)):
#             print "Leg %s" %(z)
#             print segment_data[z]["leg"]
#             print "\n\n\n"
#     print "\n\n\n"

# # Leg 1
# [{  u'origin': u'YVR', 
#     u'originTerminal': u'M', 
#     u'departureTime': u'2016-06-11T22:50-07:00', 
#     u'destinationTerminal': u'7', 
#     u'secure': True, 
#     u'destination': u'JFK', 
#     u'kind': u'qpxexpress#legInfo', 
#     u'meal': u'Dinner', 
#     u'aircraft': u'77W', 
#     u'mileage': 2441, 
#     u'arrivalTime': u'2016-06-12T07:00-04:00', 
#     u'duration': 310, 
#     u'id': u'LFi2v3UOH11vqKOh'
# }]

# # Working code to get all info from results string and parse it to print
# flight_data = []

# for x in range(len(python_results["trips"]["tripOption"])):
#     print "Round trip flight option %s" %(x)
#     option_data = python_results["trips"]["tripOption"]
#     option_id = option_data[x]["id"]
#     print "ID: %s" %(option_id)
#     option_price = option_data[x]["saleTotal"]
#     print "Price: %s" %(option_price)
#     print "\n\n\n"
#     slice_data = python_results["trips"]["tripOption"][x]["slice"]
#     dep_ret = ["Departure", "Return"]
#     for y in range(len(slice_data)):
#         print "%s Leg" %(dep_ret[y])
#         flight_duration = slice_data[y]["duration"]
#         print "Flight Duration: %s" %(flight_duration)
#         segment_data = slice_data[y]["segment"]
#         for z in range(len(segment_data)):
#             print "Leg %s" %(z)
#             each_leg = segment_data[z]["leg"][0]
#             leg_duration = each_leg["duration"]
#             print "Duration: %s" %(leg_duration)
#             leg_origin = each_leg["origin"]
#             print "Origin: %s" %(leg_origin)
#             leg_departure = each_leg["departureTime"]
#             print "Departure Time: " + leg_departure
#             leg_destination = each_leg["destination"] 
#             print "Destination: %s" %(leg_destination)
#             leg_arrival = each_leg["arrivalTime"]
#             print "Arrival Time: " + leg_arrival
#             print "\n\n\n"
#         for a in range(len(segment_data)-1):
#             connection_duration = segment_data[a]["connectionDuration"]
#             print "Connection Duration: %s" %(connection_duration)
#             print "\n\n\n"
#     print "\n\n\n"

"""Mess of code to parse results data - doesn't work, start over"""
# flight_data = {}

# for x in range(len(python_results["trips"]["tripOption"])):
#     # print "Round trip flight option %s" %(x)
#     option_data = python_results["trips"]["tripOption"]
#     option_id = option_data[x]["id"]
#     # print "ID: %s" %(flight_id)
#     option_price = option_data[x]["saleTotal"]
#     # print "Price: %s" %(flight_price)
#     # print "\n\n\n"
#     flight_data[x] = [{"option_id": option_id,"option_price": option_price}]



#     slice_data = python_results["trips"]["tripOption"][x]["slice"]
#     dep_ret = ["Departure", "Return"]

#     # flight_data[x] = [{option id, option price},{}]
#     flight_data[x].append({})

#     for y in range(len(slice_data)):
#         # print "%s Leg" %(dep_ret[y])
#         flight_duration = slice_data[y]["duration"]
#         # print "Flight Duration: %s" %(flight_duration)


#         flight_data[x][-1]["flight_duration"] = []
#         flight_data[x][-1]["flight_duration"].append(flight_duration)

#         segment_data = slice_data[y]["segment"]


#         # flight_data[i] = [{option id, option price}, {flight duration [leg data]}]
#         # flight_data[x][-1]["leg_data"] = []
#         for z in range(len(segment_data)):
#             # print "Leg %s" %(z)
#             each_leg = segment_data[z]["leg"][0]
#             leg_duration = each_leg["duration"]
#             # print "Duration: %s" %(leg_duration)
#             leg_origin = each_leg["origin"]
#             # print "Origin: %s" %(leg_origin)
#             leg_departure = each_leg["departureTime"]
#             # print "Departure Time: " + leg_departure
#             leg_destination = each_leg["destination"] 
#             # print "Destination: %s" %(leg_destination)
#             leg_arrival = each_leg["arrivalTime"]
#             # print "Arrival Time: " + leg_arrival
#             # print "\n\n\n"

#             # flight_data[x][-1]["leg_data"].append({})
#             # flight_data[x][-1]["leg_data"][-1]["leg_duration"] = leg_duration
#             # flight_data[x][-1]["leg_data"][-1]["leg_origin"] = leg_origin
#             # flight_data[x][-1]["leg_data"][-1]["leg_departure"] = leg_departure
#             # flight_data[x][-1]["leg_data"][-1]["leg_destination"] = leg_destination
#             # flight_data[x][-1]["leg_data"][-1]["leg_arrival"] = leg_arrival


#         for a in range(len(segment_data)-1):
#             connection_duration = segment_data[a]["connectionDuration"]

#             # flight_data[x][y+1]["leg_data"].append([])
#             # flight_data[x][y+1]["leg_data"][-1] = connectionDuration

# print flight_data

# 99: [{  'option_id': u'C1TDtZ534dKQihoVN4pVNS00g', 
#         'option_price': u'USD3256.36'
#     }, 
#     {   'flight_duration': 715, 
#         'leg_data': [{  'leg_oridin': u'JFK', 
#                         'leg_arrival': u'2016-06-21T10:33-07:00', 
#                         'leg_departure': u'2016-06-21T07:15-04:00', 
#                         'leg_destination': u'SEA', 
#                         'leg_duration': 378
#                     }, 
#                     {   'leg_oridin': u'SEA', 
#                         'leg_arrival': u'2016-06-21T16:10-07:00', 
#                         'leg_departure': u'2016-06-21T13:55-07:00', 
#                         'leg_destination': u'SFO', 
#                         'leg_duration': 135
#                     }]
#     }]

flight_data = []

for x in range(len(python_results["trips"]["tripOption"])):

    flight_data.append({})

    # print "Round trip flight option %s" %(x)
    option_data = python_results["trips"]["tripOption"]
    option_id = option_data[x]["id"]
    # print "ID: %s" %(option_id)
    option_price = option_data[x]["saleTotal"]
    # print "Price: %s" %(option_price)

    flight_data[x]["option_id"] = option_id
    flight_data[x]["option_price"] = option_price
    flight_data[x]["option_flight"] = []
    flight_data[x]["option_break"] = "\n\n\n\n\n\n"

    # print flight_data[x]
    # print "\n\n\n"
    slice_data = python_results["trips"]["tripOption"][x]["slice"]
    dep_ret = ["Departure", "Return"]
    for y in range(len(slice_data)):

        flight_data[x]["option_flight"].append([])

        # print "%s Leg" %(dep_ret[y])
        flight_duration = slice_data[y]["duration"]
        # print "Flight Duration: %s" %(flight_duration)
        segment_data = slice_data[y]["segment"]
        for z in range(len(segment_data)):

            flight_data[x]["option_flight"][y].append({})

            # print "Leg %s" %(z)
            each_leg = segment_data[z]["leg"][0]
            leg_duration = each_leg["duration"]
            # print "Duration: %s" %(leg_duration)
            leg_origin = each_leg["origin"]
            # print "Origin: %s" %(leg_origin)
            leg_departure = each_leg["departureTime"]
            # print "Departure Time: " + leg_departure
            leg_destination = each_leg["destination"] 
            # print "Destination: %s" %(leg_destination)
            leg_arrival = each_leg["arrivalTime"]
            # print "Arrival Time: " + leg_arrival

            # flight_data[x]["option_flight"][y][z]
            flight_data[x]["option_flight"][y][z]["leg_duration"] = leg_duration
            flight_data[x]["option_flight"][y][z]["leg_origin"] = leg_origin
            flight_data[x]["option_flight"][y][z]["leg_departure"] = leg_departure
            flight_data[x]["option_flight"][y][z]["leg_destination"] = leg_destination
            flight_data[x]["option_flight"][y][z]["leg_arrival"] = leg_arrival

            # print "\n\n\n"

        flight_data[x]["option_flight"][y].append({})
        flight_data[x]["option_flight"][y][-1]["flight_duration"] = flight_duration
        for a in range(len(segment_data)-1):
            connection_duration = segment_data[a]["connectionDuration"]

            flight_data[x]["option_flight"][y][-1]["connection_duration"] = connection_duration
            # print "Connection Duration: %s" %(connection_duration)
            # print "\n\n\n"
    # print "\n\n\n"

print flight_data

{'option_break': '\n\n\n\n\n\n', 
 'option_id': u'C1TDtZ534dKQihoVN4pVNS00g', 
 'option_price': u'USD3256.36', 
 'option_flight': [[{'leg_arrival': u'2016-06-11T19:49-07:00', 
                     'leg_origin': u'SFO', 
                     'leg_departure': u'2016-06-11T17:30-07:00', 
                     'leg_destination': u'YVR', 
                     'leg_duration': 139}, 
                    {'leg_arrival': u'2016-06-12T07:00-04:00', 
                     'leg_origin': u'YVR', 
                     'leg_departure': u'2016-06-11T22:50-07:00', 
                     'leg_destination': u'JFK', 
                     'leg_duration': 310}, 
                    {'flight_duration': 630, 
                     'connection_duration': 181}], 
                   [{'leg_arrival': u'2016-06-21T10:33-07:00', 
                     'leg_origin': u'JFK', 
                     'leg_departure': u'2016-06-21T07:15-04:00', 
                     'leg_destination': u'SEA', 
                     'leg_duration': 378}, 
                    {'leg_arrival': u'2016-06-21T16:10-07:00', 
                     'leg_origin': u'SEA', 
                     'leg_departure': u'2016-06-21T13:55-07:00', 
                     'leg_destination': u'SFO', 
                     'leg_duration': 135}, 
                    {'flight_duration': 715, 
                     'connection_duration': 202}]]
}

{'option_break': '\n\n\n\n\n\n', 
 'option_id': u'C1TDtZ534dKQihoVN4pVNS00g', 
 'option_price': u'USD3256.36', 
 'option_flight': [[{'leg_arrival': u'2016-06-11T19:49-07:00', 
                     'leg_origin': u'SFO', 
                     'leg_departure': u'2016-06-11T17:30-07:00', 
                     'leg_destination': u'YVR', 'leg_duration': 139
                    }, 
                    {'leg_arrival': u'2016-06-12T07:00-04:00', 
                     'leg_origin': u'YVR', 
                     'leg_departure': u'2016-06-11T22:50-07:00', 
                     'leg_destination': u'JFK', 
                     'leg_duration': 310
                    }, 
                    {'flight_duration': 630
                    }], 
                   [{'leg_arrival': u'2016-06-21T10:33-07:00', 
                     'leg_origin': u'JFK', 
                     'leg_departure': u'2016-06-21T07:15-04:00', 
                     'leg_destination': u'SEA', 
                     'leg_duration': 378
                    }, 
                    {'leg_arrival': u'2016-06-21T16:10-07:00', 
                     'leg_origin': u'SEA', 
                     'leg_departure': u'2016-06-21T13:55-07:00', 
                     'leg_destination': u'SFO', 'leg_duration': 135
                    }, 
                    {'flight_duration': 715}
                    ]]
}
