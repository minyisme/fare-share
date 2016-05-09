parameters = {
  "request": {
    "passengers": {
      "kind": "qpxexpress#passengerCounts",
      "adultCount": 1,
    },
    "slice": [
      {
        "kind": "qpxexpress#sliceInput",
        "origin": "JFK",
        "destination": "LHR",
        "date": "2016-06-11",
        "maxStops": 1,
      }
    ],
    "solutions": 2,
    "maxPrice": "USD800.00",
  }
}

{
 "kind": "qpxExpress#tripsSearch",
 "trips": {
  "kind": "qpxexpress#tripOptions",
  "requestId": "ekPvRgcdaS9tovyU70OIxD",
  "data": {
   "kind": "qpxexpress#data",
   "airport": [
    {
     "kind": "qpxexpress#airportData",
     "code": "JFK",
     "city": "NYC",
     "name": "New York John F Kennedy International"
    },
    {
     "kind": "qpxexpress#airportData",
     "code": "KEF",
     "city": "REK",
     "name": "Reykjavik Keflavik International"
    },
    {
     "kind": "qpxexpress#airportData",
     "code": "LHR",
     "city": "LON",
     "name": "London Heathrow"
    },
    {
     "kind": "qpxexpress#airportData",
     "code": "SVO",
     "city": "MOW",
     "name": "Moscow Sheremetyevo"
    }
   ],
   "city": [
    {
     "kind": "qpxexpress#cityData",
     "code": "LON",
     "name": "London"
    },
    {
     "kind": "qpxexpress#cityData",
     "code": "MOW",
     "name": "Moscow"
    },
    {
     "kind": "qpxexpress#cityData",
     "code": "NYC",
     "name": "New York"
    },
    {
     "kind": "qpxexpress#cityData",
     "code": "REK",
     "name": "Reykjavik"
    }
   ],
   "aircraft": [
    {
     "kind": "qpxexpress#aircraftData",
     "code": "320",
     "name": "Airbus A320"
    },
    {
     "kind": "qpxexpress#aircraftData",
     "code": "76W",
     "name": "Boeing 767"
    },
    {
     "kind": "qpxexpress#aircraftData",
     "code": "77W",
     "name": "Boeing 777"
    }
   ],
   "tax": [
    {
     "kind": "qpxexpress#taxData",
     "id": "ZU_001",
     "name": "Iceland Passenger Fee Keflavik"
    },
    {
     "kind": "qpxexpress#taxData",
     "id": "IS_001",
     "name": "Iceland Airport Service Charge"
    },
    {
     "kind": "qpxexpress#taxData",
     "id": "YQ_F",
     "name": "SU YQ surcharge"
    },
    {
     "kind": "qpxexpress#taxData",
     "id": "AY_001",
     "name": "US September 11th Security Fee"
    },
    {
     "kind": "qpxexpress#taxData",
     "id": "US_002",
     "name": "US International Departure Tax"
    },
    {
     "kind": "qpxexpress#taxData",
     "id": "YR_F",
     "name": "FI YR surcharge"
    },
    {
     "kind": "qpxexpress#taxData",
     "id": "XF",
     "name": "US Passenger Facility Charge"
    }
   ],
   "carrier": [
    {
     "kind": "qpxexpress#carrierData",
     "code": "FI",
     "name": "Icelandair"
    },
    {
     "kind": "qpxexpress#carrierData",
     "code": "SU",
     "name": "PJSC \"Aeroflot\""
    }
   ]
  },
  "tripOption": [
   {
    "kind": "qpxexpress#tripOption",
    "saleTotal": "USD642.50",
    "id": "JziM7lRq1yUPVw5DWSnSqL002",
    "slice": [
     {
      "kind": "qpxexpress#sliceInfo",
      "duration": 865,
      "segment": [
       {
        "kind": "qpxexpress#segmentInfo",
        "duration": 545,
        "flight": {
         "carrier": "SU",
         "number": "101"
        },
        "id": "GkUtY7cMpLWsKc9K",
        "cabin": "COACH",
        "bookingCode": "L",
        "bookingCodeCount": 3,
        "marriedSegmentGroup": "0",
        "leg": [
         {
          "kind": "qpxexpress#legInfo",
          "id": "L-NsgKSx-LKJgLYM",
          "aircraft": "77W",
          "arrivalTime": "2016-06-12T06:25+03:00",
          "departureTime": "2016-06-11T14:20-04:00",
          "origin": "JFK",
          "destination": "SVO",
          "originTerminal": "1",
          "destinationTerminal": "D",
          "duration": 545,
          "mileage": 4646,
          "meal": "Lunch",
          "secure": true
         }
        ],
        "connectionDuration": 70
       },
       {
        "kind": "qpxexpress#segmentInfo",
        "duration": 250,
        "flight": {
         "carrier": "SU",
         "number": "2574"
        },
        "id": "GPUbSJb+13yPgtu7",
        "cabin": "COACH",
        "bookingCode": "L",
        "bookingCodeCount": 7,
        "marriedSegmentGroup": "1",
        "leg": [
         {
          "kind": "qpxexpress#legInfo",
          "id": "LjB6yjjz319Z+1RR",
          "aircraft": "320",
          "arrivalTime": "2016-06-12T09:45+01:00",
          "departureTime": "2016-06-12T07:35+03:00",
          "origin": "SVO",
          "destination": "LHR",
          "originTerminal": "D",
          "destinationTerminal": "4",
          "duration": 250,
          "mileage": 1557,
          "meal": "Breakfast"
         }
        ]
       }
      ]
     }
    ],
    "pricing": [
     {
      "kind": "qpxexpress#pricingInfo",
      "fare": [
       {
        "kind": "qpxexpress#fareInfo",
        "id": "Annk0d/k1PnyB0GQ8wqu7b86zwUihacx0RyHDyD54w+I",
        "carrier": "SU",
        "origin": "NYC",
        "destination": "LON",
        "basisCode": "LKEXOW"
       }
      ],
      "segmentPricing": [
       {
        "kind": "qpxexpress#segmentPricing",
        "fareId": "Annk0d/k1PnyB0GQ8wqu7b86zwUihacx0RyHDyD54w+I",
        "segmentId": "GPUbSJb+13yPgtu7"
       },
       {
        "kind": "qpxexpress#segmentPricing",
        "fareId": "Annk0d/k1PnyB0GQ8wqu7b86zwUihacx0RyHDyD54w+I",
        "segmentId": "GkUtY7cMpLWsKc9K"
       }
      ],
      "baseFareTotal": "USD460.00",
      "saleFareTotal": "USD460.00",
      "saleTaxTotal": "USD182.50",
      "saleTotal": "USD642.50",
      "passengers": {
       "kind": "qpxexpress#passengerCounts",
       "adultCount": 1
      },
      "tax": [
       {
        "kind": "qpxexpress#taxInfo",
        "id": "YQ_F",
        "chargeType": "CARRIER_SURCHARGE",
        "code": "YQ",
        "salePrice": "USD154.60"
       },
       {
        "kind": "qpxexpress#taxInfo",
        "id": "US_002",
        "chargeType": "GOVERNMENT",
        "code": "US",
        "country": "US",
        "salePrice": "USD17.80"
       },
       {
        "kind": "qpxexpress#taxInfo",
        "id": "AY_001",
        "chargeType": "GOVERNMENT",
        "code": "AY",
        "country": "US",
        "salePrice": "USD5.60"
       },
       {
        "kind": "qpxexpress#taxInfo",
        "id": "XF",
        "chargeType": "GOVERNMENT",
        "code": "XF",
        "country": "US",
        "salePrice": "USD4.50"
       }
      ],
      "fareCalculation": "NYC SU X/MOW SU LON 460.00LKEXOW NUC 460.00 END ROE 1.00 FARE USD 460.00 XT 17.80US 5.60AY 154.60YQ 4.50XF JFK4.50",
      "latestTicketingTime": "2016-05-16T23:59-04:00",
      "ptc": "ADT",
      "refundable": true
     }
    ]
   },
   {
    "kind": "qpxexpress#tripOption",
    "saleTotal": "USD733.20",
    "id": "JziM7lRq1yUPVw5DWSnSqL001",
    "slice": [
     {
      "kind": "qpxexpress#sliceInfo",
      "duration": 605,
      "segment": [
       {
        "kind": "qpxexpress#segmentInfo",
        "duration": 335,
        "flight": {
         "carrier": "FI",
         "number": "614"
        },
        "id": "GEqPlpjUvqj4PaeH",
        "cabin": "COACH",
        "bookingCode": "K",
        "bookingCodeCount": 9,
        "marriedSegmentGroup": "0",
        "leg": [
         {
          "kind": "qpxexpress#legInfo",
          "id": "L7tDRPDuBmxx-Rr7",
          "aircraft": "76W",
          "arrivalTime": "2016-06-12T06:15+00:00",
          "departureTime": "2016-06-11T20:40-04:00",
          "origin": "JFK",
          "destination": "KEF",
          "originTerminal": "7",
          "duration": 335,
          "mileage": 2585,
          "meal": "Alcoholic Beverages for Purchase",
          "secure": true
         }
        ],
        "connectionDuration": 85
       },
       {
        "kind": "qpxexpress#segmentInfo",
        "duration": 185,
        "flight": {
         "carrier": "FI",
         "number": "450"
        },
        "id": "GRLnblT1o3qNDpUL",
        "cabin": "COACH",
        "bookingCode": "K",
        "bookingCodeCount": 9,
        "marriedSegmentGroup": "1",
        "leg": [
         {
          "kind": "qpxexpress#legInfo",
          "id": "Lq8yrbOFX2O+xs5r",
          "aircraft": "76W",
          "arrivalTime": "2016-06-12T11:45+01:00",
          "departureTime": "2016-06-12T07:40+00:00",
          "origin": "KEF",
          "destination": "LHR",
          "destinationTerminal": "2",
          "duration": 185,
          "mileage": 1176,
          "meal": "Alcoholic Beverages for Purchase"
         }
        ]
       }
      ]
     }
    ],
    "pricing": [
     {
      "kind": "qpxexpress#pricingInfo",
      "fare": [
       {
        "kind": "qpxexpress#fareInfo",
        "id": "AC+9mgHviUzT4KzRehuuaP2tgk4yGTv4MOOABdZN/Y5s",
        "carrier": "FI",
        "origin": "NYC",
        "destination": "LON",
        "basisCode": "KQO3FLEX"
       }
      ],
      "segmentPricing": [
       {
        "kind": "qpxexpress#segmentPricing",
        "fareId": "AC+9mgHviUzT4KzRehuuaP2tgk4yGTv4MOOABdZN/Y5s",
        "segmentId": "GEqPlpjUvqj4PaeH"
       },
       {
        "kind": "qpxexpress#segmentPricing",
        "fareId": "AC+9mgHviUzT4KzRehuuaP2tgk4yGTv4MOOABdZN/Y5s",
        "segmentId": "GRLnblT1o3qNDpUL"
       }
      ],
      "baseFareTotal": "USD595.00",
      "saleFareTotal": "USD595.00",
      "saleTaxTotal": "USD138.20",
      "saleTotal": "USD733.20",
      "passengers": {
       "kind": "qpxexpress#passengerCounts",
       "adultCount": 1
      },
      "tax": [
       {
        "kind": "qpxexpress#taxInfo",
        "id": "ZU_001",
        "chargeType": "GOVERNMENT",
        "code": "ZU",
        "country": "IS",
        "salePrice": "USD6.60"
       },
       {
        "kind": "qpxexpress#taxInfo",
        "id": "IS_001",
        "chargeType": "GOVERNMENT",
        "code": "IS",
        "country": "IS",
        "salePrice": "USD3.70"
       },
       {
        "kind": "qpxexpress#taxInfo",
        "id": "YR_F",
        "chargeType": "CARRIER_SURCHARGE",
        "code": "YR",
        "salePrice": "USD100.00"
       },
       {
        "kind": "qpxexpress#taxInfo",
        "id": "US_002",
        "chargeType": "GOVERNMENT",
        "code": "US",
        "country": "US",
        "salePrice": "USD17.80"
       },
       {
        "kind": "qpxexpress#taxInfo",
        "id": "AY_001",
        "chargeType": "GOVERNMENT",
        "code": "AY",
        "country": "US",
        "salePrice": "USD5.60"
       },
       {
        "kind": "qpxexpress#taxInfo",
        "id": "XF",
        "chargeType": "GOVERNMENT",
        "code": "XF",
        "country": "US",
        "salePrice": "USD4.50"
       }
      ],
      "fareCalculation": "NYC FI X/REK FI LON 595.00KQO3FLEX NUC 595.00 END ROE 1.00 FARE USD 595.00 XT 17.80US 5.60AY 3.70IS 6.60ZU 100.00YR 4.50XF JFK4.50",
      "latestTicketingTime": "2016-05-16T23:59-04:00",
      "ptc": "ADT",
      "refundable": true
     }
    ]
   }
  ]
 }
}
