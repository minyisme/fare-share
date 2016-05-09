parameters = {
  "request": {
    "passengers": {
      "kind": "qpxexpress#passengerCounts",
      "adultCount": 1,
    },
    "slice": [
      {
        "kind": "qpxexpress#sliceInput",
        "origin": "ORD",
        "destination": "LHR",
        "date": "2016-06-11",
        "maxStops": 1,
      }
    ],
    "solutions": 20,
    "maxPrice": "USD1000.00",
  }
}

{
 "kind": "qpxExpress#tripsSearch",
 "trips": {
  "kind": "qpxexpress#tripOptions",
  "requestId": "1vgFetgHZmLJi4wwG0OIxw",
  "data": {
   "kind": "qpxexpress#data",
   "airport": [
    {
     "kind": "qpxexpress#airportData",
     "code": "IST",
     "city": "IST",
     "name": "Istanbul Ataturk"
    },
    {
     "kind": "qpxexpress#airportData",
     "code": "LHR",
     "city": "LON",
     "name": "London Heathrow"
    },
    {
     "kind": "qpxexpress#airportData",
     "code": "ORD",
     "city": "CHI",
     "name": "Chicago O'Hare"
    }
   ],
   "city": [
    {
     "kind": "qpxexpress#cityData",
     "code": "CHI",
     "name": "Chicago"
    },
    {
     "kind": "qpxexpress#cityData",
     "code": "IST",
     "name": "Istanbul"
    },
    {
     "kind": "qpxexpress#cityData",
     "code": "LON",
     "name": "London"
    }
   ],
   "aircraft": [
    {
     "kind": "qpxexpress#aircraftData",
     "code": "32B",
     "name": "Airbus A321 (Sharklets)"
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
     "id": "TR_001",
     "name": "Turkey Airport Service Charge International"
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
     "name": "TK YR surcharge"
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
     "code": "TK",
     "name": "Turkish Airlines Inc."
    }
   ]
  },
  "tripOption": [
   {
    "kind": "qpxexpress#tripOption",
    "saleTotal": "USD929.60",
    "id": "2nkh6ZYBOwGOnL3oO9P30A002",
    "slice": [
     {
      "kind": "qpxexpress#sliceInfo",
      "duration": 1140,
      "segment": [
       {
        "kind": "qpxexpress#segmentInfo",
        "duration": 645,
        "flight": {
         "carrier": "TK",
         "number": "6"
        },
        "id": "GO1NtJ9P5u4xp3Sc",
        "cabin": "COACH",
        "bookingCode": "M",
        "bookingCodeCount": 9,
        "marriedSegmentGroup": "0",
        "leg": [
         {
          "kind": "qpxexpress#legInfo",
          "id": "LbgqFAvUQfbqtnJq",
          "aircraft": "77W",
          "arrivalTime": "2016-06-12T16:15+03:00",
          "departureTime": "2016-06-11T21:30-05:00",
          "origin": "ORD",
          "destination": "IST",
          "originTerminal": "5",
          "destinationTerminal": "I",
          "duration": 645,
          "mileage": 5474,
          "meal": "Meal",
          "secure": true
         }
        ],
        "connectionDuration": 245
       },
       {
        "kind": "qpxexpress#segmentInfo",
        "duration": 250,
        "flight": {
         "carrier": "TK",
         "number": "1987"
        },
        "id": "GkyuEbW69ST5XOtV",
        "cabin": "COACH",
        "bookingCode": "M",
        "bookingCodeCount": 9,
        "marriedSegmentGroup": "1",
        "leg": [
         {
          "kind": "qpxexpress#legInfo",
          "id": "L8UyryBRnnHzh62x",
          "aircraft": "32B",
          "arrivalTime": "2016-06-12T22:30+01:00",
          "departureTime": "2016-06-12T20:20+03:00",
          "origin": "IST",
          "destination": "LHR",
          "originTerminal": "I",
          "destinationTerminal": "2",
          "duration": 250,
          "mileage": 1561,
          "meal": "Meal"
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
        "id": "ATAMu3DjnFi+FpU06TwqCA7ovbPsdfr2E7XOoYStFSE6",
        "carrier": "TK",
        "origin": "CHI",
        "destination": "LON",
        "basisCode": "MHVOW"
       }
      ],
      "segmentPricing": [
       {
        "kind": "qpxexpress#segmentPricing",
        "fareId": "ATAMu3DjnFi+FpU06TwqCA7ovbPsdfr2E7XOoYStFSE6",
        "segmentId": "GkyuEbW69ST5XOtV"
       },
       {
        "kind": "qpxexpress#segmentPricing",
        "fareId": "ATAMu3DjnFi+FpU06TwqCA7ovbPsdfr2E7XOoYStFSE6",
        "segmentId": "GO1NtJ9P5u4xp3Sc"
       }
      ],
      "baseFareTotal": "USD726.00",
      "saleFareTotal": "USD726.00",
      "saleTaxTotal": "USD203.60",
      "saleTotal": "USD929.60",
      "passengers": {
       "kind": "qpxexpress#passengerCounts",
       "adultCount": 1
      },
      "tax": [
       {
        "kind": "qpxexpress#taxInfo",
        "id": "TR_001",
        "chargeType": "GOVERNMENT",
        "code": "TR",
        "country": "TR",
        "salePrice": "USD5.70"
       },
       {
        "kind": "qpxexpress#taxInfo",
        "id": "YR_F",
        "chargeType": "CARRIER_SURCHARGE",
        "code": "YR",
        "salePrice": "USD170.00"
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
      "fareCalculation": "CHI TK X/IST TK LON 726.00MHVOW NUC 726.00 END ROE 1.00 FARE USD 726.00 XT 17.80US 5.60AY 5.70TR 170.00YR 4.50XF ORD4.50",
      "latestTicketingTime": "2016-06-11T22:29-04:00",
      "ptc": "ADT",
      "refundable": true
     }
    ]
   },
   {
    "kind": "qpxexpress#tripOption",
    "saleTotal": "USD929.60",
    "id": "2nkh6ZYBOwGOnL3oO9P30A001",
    "slice": [
     {
      "kind": "qpxexpress#sliceInfo",
      "duration": 1035,
      "segment": [
       {
        "kind": "qpxexpress#segmentInfo",
        "duration": 645,
        "flight": {
         "carrier": "TK",
         "number": "6"
        },
        "id": "GO1NtJ9P5u4xp3Sc",
        "cabin": "COACH",
        "bookingCode": "M",
        "bookingCodeCount": 9,
        "marriedSegmentGroup": "0",
        "leg": [
         {
          "kind": "qpxexpress#legInfo",
          "id": "LbgqFAvUQfbqtnJq",
          "aircraft": "77W",
          "arrivalTime": "2016-06-12T16:15+03:00",
          "departureTime": "2016-06-11T21:30-05:00",
          "origin": "ORD",
          "destination": "IST",
          "originTerminal": "5",
          "destinationTerminal": "I",
          "duration": 645,
          "mileage": 5474,
          "meal": "Meal",
          "secure": true
         }
        ],
        "connectionDuration": 145
       },
       {
        "kind": "qpxexpress#segmentInfo",
        "duration": 245,
        "flight": {
         "carrier": "TK",
         "number": "1983"
        },
        "id": "G2aATo-gKAya4osF",
        "cabin": "COACH",
        "bookingCode": "M",
        "bookingCodeCount": 9,
        "marriedSegmentGroup": "1",
        "leg": [
         {
          "kind": "qpxexpress#legInfo",
          "id": "LI8fkmoa22llvh35",
          "aircraft": "32B",
          "arrivalTime": "2016-06-12T20:45+01:00",
          "departureTime": "2016-06-12T18:40+03:00",
          "origin": "IST",
          "destination": "LHR",
          "originTerminal": "I",
          "destinationTerminal": "2",
          "duration": 245,
          "mileage": 1561,
          "meal": "Meal"
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
        "id": "ATAMu3DjnFi+FpU06TwqCA7ovbPsdfr2E7XOoYStFSE6",
        "carrier": "TK",
        "origin": "CHI",
        "destination": "LON",
        "basisCode": "MHVOW"
       }
      ],
      "segmentPricing": [
       {
        "kind": "qpxexpress#segmentPricing",
        "fareId": "ATAMu3DjnFi+FpU06TwqCA7ovbPsdfr2E7XOoYStFSE6",
        "segmentId": "G2aATo-gKAya4osF"
       },
       {
        "kind": "qpxexpress#segmentPricing",
        "fareId": "ATAMu3DjnFi+FpU06TwqCA7ovbPsdfr2E7XOoYStFSE6",
        "segmentId": "GO1NtJ9P5u4xp3Sc"
       }
      ],
      "baseFareTotal": "USD726.00",
      "saleFareTotal": "USD726.00",
      "saleTaxTotal": "USD203.60",
      "saleTotal": "USD929.60",
      "passengers": {
       "kind": "qpxexpress#passengerCounts",
       "adultCount": 1
      },
      "tax": [
       {
        "kind": "qpxexpress#taxInfo",
        "id": "TR_001",
        "chargeType": "GOVERNMENT",
        "code": "TR",
        "country": "TR",
        "salePrice": "USD5.70"
       },
       {
        "kind": "qpxexpress#taxInfo",
        "id": "YR_F",
        "chargeType": "CARRIER_SURCHARGE",
        "code": "YR",
        "salePrice": "USD170.00"
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
      "fareCalculation": "CHI TK X/IST TK LON 726.00MHVOW NUC 726.00 END ROE 1.00 FARE USD 726.00 XT 17.80US 5.60AY 5.70TR 170.00YR 4.50XF ORD4.50",
      "latestTicketingTime": "2016-06-11T22:29-04:00",
      "ptc": "ADT",
      "refundable": true
     }
    ]
   }
  ]
 }
}
