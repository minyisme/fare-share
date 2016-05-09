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
    "solutions": 20,
    "maxPrice": "USD1000.00",
  }
}

{
 "kind": "qpxExpress#tripsSearch",
 "trips": {
  "kind": "qpxexpress#tripOptions",
  "requestId": "qt3ax16SU1bDTMND00OIxa",
  "data": {
   "kind": "qpxexpress#data",
   "airport": [
    {
     "kind": "qpxexpress#airportData",
     "code": "CMN",
     "city": "CAS",
     "name": "Casablanca Mohammed V"
    },
    {
     "kind": "qpxexpress#airportData",
     "code": "DUB",
     "city": "DUB",
     "name": "Dublin International"
    },
    {
     "kind": "qpxexpress#airportData",
     "code": "IST",
     "city": "IST",
     "name": "Istanbul Ataturk"
    },
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
     "code": "SNN",
     "city": "SNN",
     "name": "Shannon International"
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
     "code": "CAS",
     "name": "Casablanca"
    },
    {
     "kind": "qpxexpress#cityData",
     "code": "DUB",
     "name": "Dublin"
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
    },
    {
     "kind": "qpxexpress#cityData",
     "code": "SNN",
     "name": "Shannon"
    }
   ],
   "aircraft": [
    {
     "kind": "qpxexpress#aircraftData",
     "code": "319",
     "name": "Airbus A319"
    },
    {
     "kind": "qpxexpress#aircraftData",
     "code": "320",
     "name": "Airbus A320"
    },
    {
     "kind": "qpxexpress#aircraftData",
     "code": "32B",
     "name": "Airbus A321 (Sharklets)"
    },
    {
     "kind": "qpxexpress#aircraftData",
     "code": "330",
     "name": "Airbus A330"
    },
    {
     "kind": "qpxexpress#aircraftData",
     "code": "332",
     "name": "Airbus A330"
    },
    {
     "kind": "qpxexpress#aircraftData",
     "code": "333",
     "name": "Airbus A330"
    },
    {
     "kind": "qpxexpress#aircraftData",
     "code": "738",
     "name": "Boeing 737"
    },
    {
     "kind": "qpxexpress#aircraftData",
     "code": "757",
     "name": "Boeing 757"
    },
    {
     "kind": "qpxexpress#aircraftData",
     "code": "75W",
     "name": "Boeing 757"
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
    },
    {
     "kind": "qpxexpress#aircraftData",
     "code": "788",
     "name": "Boeing 787"
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
     "id": "UP_001",
     "name": "Ireland Passenger Charge"
    },
    {
     "kind": "qpxexpress#taxData",
     "id": "MA_001",
     "name": "Morocco Passenger Service Charge CMN"
    },
    {
     "kind": "qpxexpress#taxData",
     "id": "MA_012",
     "name": "Morocco Airport Security Tax"
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
     "code": "AT",
     "name": "Royal Air Maroc"
    },
    {
     "kind": "qpxexpress#carrierData",
     "code": "EI",
     "name": "Aer Lingus Limited"
    },
    {
     "kind": "qpxexpress#carrierData",
     "code": "FI",
     "name": "Icelandair"
    },
    {
     "kind": "qpxexpress#carrierData",
     "code": "SU",
     "name": "PJSC \"Aeroflot\""
    },
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
    "saleTotal": "USD642.50",
    "id": "LgTYp0kFZU8VNuBuRvQjMM00E",
    "slice": [
     {
      "kind": "qpxexpress#sliceInfo",
      "duration": 1275,
      "segment": [
       {
        "kind": "qpxexpress#segmentInfo",
        "duration": 545,
        "flight": {
         "carrier": "SU",
         "number": "103"
        },
        "id": "Gs+YFRH+N0r-6Li0",
        "cabin": "COACH",
        "bookingCode": "L",
        "bookingCodeCount": 7,
        "marriedSegmentGroup": "0",
        "leg": [
         {
          "kind": "qpxexpress#legInfo",
          "id": "LNnX7UYn815wbdSg",
          "aircraft": "77W",
          "arrivalTime": "2016-06-12T11:15+03:00",
          "departureTime": "2016-06-11T19:10-04:00",
          "origin": "JFK",
          "destination": "SVO",
          "originTerminal": "1",
          "destinationTerminal": "D",
          "duration": 545,
          "mileage": 4646,
          "meal": "Dinner",
          "secure": true
         }
        ],
        "connectionDuration": 490
       },
       {
        "kind": "qpxexpress#segmentInfo",
        "duration": 240,
        "flight": {
         "carrier": "SU",
         "number": "2584"
        },
        "id": "GpT2GAuVBTwrVSry",
        "cabin": "COACH",
        "bookingCode": "L",
        "bookingCodeCount": 7,
        "marriedSegmentGroup": "1",
        "leg": [
         {
          "kind": "qpxexpress#legInfo",
          "id": "L4MLHMjNQ4jhuoea",
          "aircraft": "333",
          "arrivalTime": "2016-06-12T21:25+01:00",
          "departureTime": "2016-06-12T19:25+03:00",
          "origin": "SVO",
          "destination": "LHR",
          "originTerminal": "D",
          "destinationTerminal": "4",
          "duration": 240,
          "mileage": 1557,
          "meal": "Dinner"
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
        "segmentId": "Gs+YFRH+N0r-6Li0"
       },
       {
        "kind": "qpxexpress#segmentPricing",
        "fareId": "Annk0d/k1PnyB0GQ8wqu7b86zwUihacx0RyHDyD54w+I",
        "segmentId": "GpT2GAuVBTwrVSry"
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
    "saleTotal": "USD642.50",
    "id": "LgTYp0kFZU8VNuBuRvQjMM002",
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
    "saleTotal": "USD642.50",
    "id": "LgTYp0kFZU8VNuBuRvQjMM004",
    "slice": [
     {
      "kind": "qpxexpress#sliceInfo",
      "duration": 1005,
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
        "connectionDuration": 220
       },
       {
        "kind": "qpxexpress#segmentInfo",
        "duration": 240,
        "flight": {
         "carrier": "SU",
         "number": "2578"
        },
        "id": "GziE9N9SfQD7VMlB",
        "cabin": "COACH",
        "bookingCode": "L",
        "bookingCodeCount": 7,
        "marriedSegmentGroup": "1",
        "leg": [
         {
          "kind": "qpxexpress#legInfo",
          "id": "Ls4bYvutu-yAB053",
          "aircraft": "333",
          "arrivalTime": "2016-06-12T12:05+01:00",
          "departureTime": "2016-06-12T10:05+03:00",
          "origin": "SVO",
          "destination": "LHR",
          "originTerminal": "D",
          "destinationTerminal": "4",
          "duration": 240,
          "mileage": 1557,
          "meal": "Lunch"
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
        "segmentId": "GziE9N9SfQD7VMlB"
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
    "saleTotal": "USD678.90",
    "id": "LgTYp0kFZU8VNuBuRvQjMM005",
    "slice": [
     {
      "kind": "qpxexpress#sliceInfo",
      "duration": 920,
      "segment": [
       {
        "kind": "qpxexpress#segmentInfo",
        "duration": 410,
        "flight": {
         "carrier": "AT",
         "number": "201"
        },
        "id": "GArPe3xUMb7NcU4y",
        "cabin": "COACH",
        "bookingCode": "K",
        "bookingCodeCount": 9,
        "marriedSegmentGroup": "0",
        "leg": [
         {
          "kind": "qpxexpress#legInfo",
          "id": "LoySmmW-WTEWUi5u",
          "aircraft": "788",
          "arrivalTime": "2016-06-12T08:20+01:00",
          "departureTime": "2016-06-11T20:30-04:00",
          "origin": "JFK",
          "destination": "CMN",
          "originTerminal": "1",
          "destinationTerminal": "2",
          "duration": 410,
          "mileage": 3599,
          "meal": "Breakfast",
          "secure": true
         }
        ],
        "connectionDuration": 310
       },
       {
        "kind": "qpxexpress#segmentInfo",
        "duration": 200,
        "flight": {
         "carrier": "AT",
         "number": "800"
        },
        "id": "GfPubm1-iap4gpJR",
        "cabin": "COACH",
        "bookingCode": "K",
        "bookingCodeCount": 9,
        "marriedSegmentGroup": "1",
        "leg": [
         {
          "kind": "qpxexpress#legInfo",
          "id": "LHEUVr1B7I-b4P7h",
          "aircraft": "738",
          "arrivalTime": "2016-06-12T16:50+01:00",
          "departureTime": "2016-06-12T13:30+01:00",
          "origin": "CMN",
          "destination": "LHR",
          "originTerminal": "2",
          "destinationTerminal": "4",
          "duration": 200,
          "mileage": 1300,
          "meal": "Dinner"
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
        "id": "ArDQOrtMdcjkfXNAUjsnTgyAJzTbww/Tkl5M2qLEIEi/",
        "carrier": "AT",
        "origin": "NYC",
        "destination": "LON",
        "basisCode": "KA0W0USA"
       }
      ],
      "segmentPricing": [
       {
        "kind": "qpxexpress#segmentPricing",
        "fareId": "ArDQOrtMdcjkfXNAUjsnTgyAJzTbww/Tkl5M2qLEIEi/",
        "segmentId": "GfPubm1-iap4gpJR"
       },
       {
        "kind": "qpxexpress#segmentPricing",
        "fareId": "ArDQOrtMdcjkfXNAUjsnTgyAJzTbww/Tkl5M2qLEIEi/",
        "segmentId": "GArPe3xUMb7NcU4y"
       }
      ],
      "baseFareTotal": "USD505.00",
      "saleFareTotal": "USD505.00",
      "saleTaxTotal": "USD173.90",
      "saleTotal": "USD678.90",
      "passengers": {
       "kind": "qpxexpress#passengerCounts",
       "adultCount": 1
      },
      "tax": [
       {
        "kind": "qpxexpress#taxInfo",
        "id": "MA_001",
        "chargeType": "GOVERNMENT",
        "code": "MA",
        "country": "MA",
        "salePrice": "USD14.00"
       },
       {
        "kind": "qpxexpress#taxInfo",
        "id": "MA_012",
        "chargeType": "GOVERNMENT",
        "code": "MA",
        "country": "MA",
        "salePrice": "USD5.00"
       },
       {
        "kind": "qpxexpress#taxInfo",
        "id": "YQ_F",
        "chargeType": "CARRIER_SURCHARGE",
        "code": "YQ",
        "salePrice": "USD127.00"
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
      "fareCalculation": "NYC AT X/CAS AT LON 505.00KA0W0USA NUC 505.00 END ROE 1.00 FARE USD 505.00 XT 17.80US 5.60AY 19.00MA 127.00YQ 4.50XF JFK4.50",
      "latestTicketingTime": "2016-06-11T20:29-04:00",
      "ptc": "ADT"
     }
    ]
   },
   {
    "kind": "qpxexpress#tripOption",
    "saleTotal": "USD733.20",
    "id": "LgTYp0kFZU8VNuBuRvQjMM001",
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
   },
   {
    "kind": "qpxexpress#tripOption",
    "saleTotal": "USD733.20",
    "id": "LgTYp0kFZU8VNuBuRvQjMM00G",
    "slice": [
     {
      "kind": "qpxexpress#sliceInfo",
      "duration": 1110,
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
        "connectionDuration": 595
       },
       {
        "kind": "qpxexpress#segmentInfo",
        "duration": 180,
        "flight": {
         "carrier": "FI",
         "number": "454"
        },
        "id": "GhKKWiXpK1E4Os2t",
        "cabin": "COACH",
        "bookingCode": "K",
        "bookingCodeCount": 9,
        "marriedSegmentGroup": "1",
        "leg": [
         {
          "kind": "qpxexpress#legInfo",
          "id": "LVpy1sJkCB1aUjHB",
          "aircraft": "75W",
          "arrivalTime": "2016-06-12T20:10+01:00",
          "departureTime": "2016-06-12T16:10+00:00",
          "origin": "KEF",
          "destination": "LHR",
          "destinationTerminal": "2",
          "duration": 180,
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
        "segmentId": "GhKKWiXpK1E4Os2t"
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
   },
   {
    "kind": "qpxexpress#tripOption",
    "saleTotal": "USD792.27",
    "id": "LgTYp0kFZU8VNuBuRvQjMM006",
    "slice": [
     {
      "kind": "qpxexpress#sliceInfo",
      "duration": 690,
      "segment": [
       {
        "kind": "qpxexpress#segmentInfo",
        "duration": 400,
        "flight": {
         "carrier": "EI",
         "number": "108"
        },
        "id": "G3Zqa3yIdmCK+vqb",
        "cabin": "COACH",
        "bookingCode": "M",
        "bookingCodeCount": 4,
        "marriedSegmentGroup": "0",
        "leg": [
         {
          "kind": "qpxexpress#legInfo",
          "id": "LvfPDgbO25dNEwVW",
          "aircraft": "330",
          "arrivalTime": "2016-06-12T08:40+01:00",
          "departureTime": "2016-06-11T21:00-04:00",
          "origin": "JFK",
          "destination": "DUB",
          "originTerminal": "5",
          "destinationTerminal": "2",
          "duration": 400,
          "mileage": 3169,
          "meal": "Meal",
          "secure": true
         }
        ],
        "connectionDuration": 205
       },
       {
        "kind": "qpxexpress#segmentInfo",
        "duration": 85,
        "flight": {
         "carrier": "EI",
         "number": "164"
        },
        "id": "GeRsT2R8EcE7jgJD",
        "cabin": "COACH",
        "bookingCode": "F",
        "bookingCodeCount": 4,
        "marriedSegmentGroup": "1",
        "leg": [
         {
          "kind": "qpxexpress#legInfo",
          "id": "L55htjvJlG7aX8T3",
          "aircraft": "320",
          "arrivalTime": "2016-06-12T13:30+01:00",
          "departureTime": "2016-06-12T12:05+01:00",
          "origin": "DUB",
          "destination": "LHR",
          "originTerminal": "2",
          "destinationTerminal": "2",
          "duration": 85,
          "mileage": 278,
          "meal": "Food and Beverages for Purchase"
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
        "id": "ACIztrtOWe5/ixXvBpAqZ5H5yy5+E8t+xtSUqHtzWnnA",
        "carrier": "EI",
        "origin": "NYC",
        "destination": "DUB",
        "basisCode": "MK1US"
       },
       {
        "kind": "qpxexpress#fareInfo",
        "id": "AWnu1IgD58t41Jl+t2piVpe0G0R1+8MUpHcXW1z8RX3/",
        "carrier": "EI",
        "origin": "DUB",
        "destination": "LON",
        "basisCode": "FOW26GDS"
       }
      ],
      "segmentPricing": [
       {
        "kind": "qpxexpress#segmentPricing",
        "fareId": "ACIztrtOWe5/ixXvBpAqZ5H5yy5+E8t+xtSUqHtzWnnA",
        "segmentId": "G3Zqa3yIdmCK+vqb"
       },
       {
        "kind": "qpxexpress#segmentPricing",
        "fareId": "AWnu1IgD58t41Jl+t2piVpe0G0R1+8MUpHcXW1z8RX3/",
        "segmentId": "GeRsT2R8EcE7jgJD"
       }
      ],
      "baseFareTotal": "USD723.00",
      "saleFareTotal": "USD723.00",
      "saleTaxTotal": "USD69.27",
      "saleTotal": "USD792.27",
      "passengers": {
       "kind": "qpxexpress#passengerCounts",
       "adultCount": 1
      },
      "tax": [
       {
        "kind": "qpxexpress#taxInfo",
        "id": "UP_001",
        "chargeType": "GOVERNMENT",
        "code": "UP",
        "country": "IE",
        "salePrice": "USD13.10"
       },
       {
        "kind": "qpxexpress#taxInfo",
        "id": "YQ_F",
        "chargeType": "CARRIER_SURCHARGE",
        "code": "YQ",
        "salePrice": "USD21.90"
       },
       {
        "kind": "qpxexpress#taxInfo",
        "id": "YQ_F",
        "chargeType": "CARRIER_SURCHARGE",
        "code": "YQ",
        "salePrice": "USD6.37"
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
      "fareCalculation": "NYC EI X/DUB Q90.00 526.00MK1US EI LHR 107.30FOW26GDS NUC 723.30 END ROE 1.00 FARE USD 723.00 XT 17.80US 5.60AY 13.10UP 28.27YQ 4.50XF JFK4.50",
      "latestTicketingTime": "2016-05-10T17:58-04:00",
      "ptc": "ADT"
     }
    ]
   },
   {
    "kind": "qpxexpress#tripOption",
    "saleTotal": "USD792.27",
    "id": "LgTYp0kFZU8VNuBuRvQjMM003",
    "slice": [
     {
      "kind": "qpxexpress#sliceInfo",
      "duration": 640,
      "segment": [
       {
        "kind": "qpxexpress#segmentInfo",
        "duration": 400,
        "flight": {
         "carrier": "EI",
         "number": "108"
        },
        "id": "G3Zqa3yIdmCK+vqb",
        "cabin": "COACH",
        "bookingCode": "M",
        "bookingCodeCount": 4,
        "marriedSegmentGroup": "0",
        "leg": [
         {
          "kind": "qpxexpress#legInfo",
          "id": "LvfPDgbO25dNEwVW",
          "aircraft": "330",
          "arrivalTime": "2016-06-12T08:40+01:00",
          "departureTime": "2016-06-11T21:00-04:00",
          "origin": "JFK",
          "destination": "DUB",
          "originTerminal": "5",
          "destinationTerminal": "2",
          "duration": 400,
          "mileage": 3169,
          "meal": "Meal",
          "secure": true
         }
        ],
        "connectionDuration": 155
       },
       {
        "kind": "qpxexpress#segmentInfo",
        "duration": 85,
        "flight": {
         "carrier": "EI",
         "number": "162"
        },
        "id": "GQd8ROKIvrR-A1Cl",
        "cabin": "COACH",
        "bookingCode": "F",
        "bookingCodeCount": 4,
        "marriedSegmentGroup": "1",
        "leg": [
         {
          "kind": "qpxexpress#legInfo",
          "id": "LWv1I24z3iAJ4E9+",
          "aircraft": "320",
          "arrivalTime": "2016-06-12T12:40+01:00",
          "departureTime": "2016-06-12T11:15+01:00",
          "origin": "DUB",
          "destination": "LHR",
          "originTerminal": "2",
          "destinationTerminal": "2",
          "duration": 85,
          "mileage": 278,
          "meal": "Food and Beverages for Purchase"
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
        "id": "ACIztrtOWe5/ixXvBpAqZ5H5yy5+E8t+xtSUqHtzWnnA",
        "carrier": "EI",
        "origin": "NYC",
        "destination": "DUB",
        "basisCode": "MK1US"
       },
       {
        "kind": "qpxexpress#fareInfo",
        "id": "AWnu1IgD58t41Jl+t2piVpe0G0R1+8MUpHcXW1z8RX3/",
        "carrier": "EI",
        "origin": "DUB",
        "destination": "LON",
        "basisCode": "FOW26GDS"
       }
      ],
      "segmentPricing": [
       {
        "kind": "qpxexpress#segmentPricing",
        "fareId": "ACIztrtOWe5/ixXvBpAqZ5H5yy5+E8t+xtSUqHtzWnnA",
        "segmentId": "G3Zqa3yIdmCK+vqb"
       },
       {
        "kind": "qpxexpress#segmentPricing",
        "fareId": "AWnu1IgD58t41Jl+t2piVpe0G0R1+8MUpHcXW1z8RX3/",
        "segmentId": "GQd8ROKIvrR-A1Cl"
       }
      ],
      "baseFareTotal": "USD723.00",
      "saleFareTotal": "USD723.00",
      "saleTaxTotal": "USD69.27",
      "saleTotal": "USD792.27",
      "passengers": {
       "kind": "qpxexpress#passengerCounts",
       "adultCount": 1
      },
      "tax": [
       {
        "kind": "qpxexpress#taxInfo",
        "id": "UP_001",
        "chargeType": "GOVERNMENT",
        "code": "UP",
        "country": "IE",
        "salePrice": "USD13.10"
       },
       {
        "kind": "qpxexpress#taxInfo",
        "id": "YQ_F",
        "chargeType": "CARRIER_SURCHARGE",
        "code": "YQ",
        "salePrice": "USD21.90"
       },
       {
        "kind": "qpxexpress#taxInfo",
        "id": "YQ_F",
        "chargeType": "CARRIER_SURCHARGE",
        "code": "YQ",
        "salePrice": "USD6.37"
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
      "fareCalculation": "NYC EI X/DUB Q90.00 526.00MK1US EI LHR 107.30FOW26GDS NUC 723.30 END ROE 1.00 FARE USD 723.00 XT 17.80US 5.60AY 13.10UP 28.27YQ 4.50XF JFK4.50",
      "latestTicketingTime": "2016-05-10T17:58-04:00",
      "ptc": "ADT"
     }
    ]
   },
   {
    "kind": "qpxexpress#tripOption",
    "saleTotal": "USD798.57",
    "id": "LgTYp0kFZU8VNuBuRvQjMM00B",
    "slice": [
     {
      "kind": "qpxexpress#sliceInfo",
      "duration": 835,
      "segment": [
       {
        "kind": "qpxexpress#segmentInfo",
        "duration": 400,
        "flight": {
         "carrier": "EI",
         "number": "108"
        },
        "id": "G3Zqa3yIdmCK+vqb",
        "cabin": "COACH",
        "bookingCode": "M",
        "bookingCodeCount": 4,
        "marriedSegmentGroup": "0",
        "leg": [
         {
          "kind": "qpxexpress#legInfo",
          "id": "LvfPDgbO25dNEwVW",
          "aircraft": "330",
          "arrivalTime": "2016-06-12T08:40+01:00",
          "departureTime": "2016-06-11T21:00-04:00",
          "origin": "JFK",
          "destination": "DUB",
          "originTerminal": "5",
          "destinationTerminal": "2",
          "duration": 400,
          "mileage": 3169,
          "meal": "Meal",
          "secure": true
         }
        ],
        "connectionDuration": 360
       },
       {
        "kind": "qpxexpress#segmentInfo",
        "duration": 75,
        "flight": {
         "carrier": "EI",
         "number": "168"
        },
        "id": "GHBFltqndmX8wKXk",
        "cabin": "COACH",
        "bookingCode": "F",
        "bookingCodeCount": 4,
        "marriedSegmentGroup": "1",
        "leg": [
         {
          "kind": "qpxexpress#legInfo",
          "id": "L5pKe6-kPbEskevy",
          "aircraft": "320",
          "arrivalTime": "2016-06-12T15:55+01:00",
          "departureTime": "2016-06-12T14:40+01:00",
          "origin": "DUB",
          "destination": "LHR",
          "originTerminal": "2",
          "destinationTerminal": "2",
          "duration": 75,
          "mileage": 278,
          "meal": "Food and Beverages for Purchase"
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
        "id": "ACIztrtOWe5/ixXvBpAqZ5H5yy5+E8t+xtSUqHtzWnnA",
        "carrier": "EI",
        "origin": "NYC",
        "destination": "DUB",
        "basisCode": "MK1US"
       },
       {
        "kind": "qpxexpress#fareInfo",
        "id": "AWnu1IgD58t41Jl+t2piVpe0G0R1+8MUpHcXW1z8RX3/",
        "carrier": "EI",
        "origin": "DUB",
        "destination": "LON",
        "basisCode": "FOW26GDS"
       }
      ],
      "segmentPricing": [
       {
        "kind": "qpxexpress#segmentPricing",
        "fareId": "ACIztrtOWe5/ixXvBpAqZ5H5yy5+E8t+xtSUqHtzWnnA",
        "segmentId": "G3Zqa3yIdmCK+vqb"
       },
       {
        "kind": "qpxexpress#segmentPricing",
        "fareId": "AWnu1IgD58t41Jl+t2piVpe0G0R1+8MUpHcXW1z8RX3/",
        "segmentId": "GHBFltqndmX8wKXk"
       }
      ],
      "baseFareTotal": "USD723.00",
      "saleFareTotal": "USD723.00",
      "saleTaxTotal": "USD75.57",
      "saleTotal": "USD798.57",
      "passengers": {
       "kind": "qpxexpress#passengerCounts",
       "adultCount": 1
      },
      "tax": [
       {
        "kind": "qpxexpress#taxInfo",
        "id": "UP_001",
        "chargeType": "GOVERNMENT",
        "code": "UP",
        "country": "IE",
        "salePrice": "USD19.40"
       },
       {
        "kind": "qpxexpress#taxInfo",
        "id": "YQ_F",
        "chargeType": "CARRIER_SURCHARGE",
        "code": "YQ",
        "salePrice": "USD21.90"
       },
       {
        "kind": "qpxexpress#taxInfo",
        "id": "YQ_F",
        "chargeType": "CARRIER_SURCHARGE",
        "code": "YQ",
        "salePrice": "USD6.37"
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
      "fareCalculation": "NYC EI X/DUB Q90.00 526.00MK1US EI LHR 107.30FOW26GDS NUC 723.30 END ROE 1.00 FARE USD 723.00 XT 17.80US 5.60AY 19.40UP 28.27YQ 4.50XF JFK4.50",
      "latestTicketingTime": "2016-05-10T17:58-04:00",
      "ptc": "ADT"
     }
    ]
   },
   {
    "kind": "qpxexpress#tripOption",
    "saleTotal": "USD803.27",
    "id": "LgTYp0kFZU8VNuBuRvQjMM00A",
    "slice": [
     {
      "kind": "qpxexpress#sliceInfo",
      "duration": 785,
      "segment": [
       {
        "kind": "qpxexpress#segmentInfo",
        "duration": 400,
        "flight": {
         "carrier": "EI",
         "number": "108"
        },
        "id": "G3Zqa3yIdmCK+vqb",
        "cabin": "COACH",
        "bookingCode": "M",
        "bookingCodeCount": 4,
        "marriedSegmentGroup": "0",
        "leg": [
         {
          "kind": "qpxexpress#legInfo",
          "id": "LvfPDgbO25dNEwVW",
          "aircraft": "330",
          "arrivalTime": "2016-06-12T08:40+01:00",
          "departureTime": "2016-06-11T21:00-04:00",
          "origin": "JFK",
          "destination": "DUB",
          "originTerminal": "5",
          "destinationTerminal": "2",
          "duration": 400,
          "mileage": 3169,
          "meal": "Meal",
          "secure": true
         }
        ],
        "connectionDuration": 300
       },
       {
        "kind": "qpxexpress#segmentInfo",
        "duration": 85,
        "flight": {
         "carrier": "EI",
         "number": "166"
        },
        "id": "GLfWNgzdxStELGhJ",
        "cabin": "COACH",
        "bookingCode": "V",
        "bookingCodeCount": 4,
        "marriedSegmentGroup": "1",
        "leg": [
         {
          "kind": "qpxexpress#legInfo",
          "id": "LDklfIOoY+ZjQtjq",
          "aircraft": "320",
          "arrivalTime": "2016-06-12T15:05+01:00",
          "departureTime": "2016-06-12T13:40+01:00",
          "origin": "DUB",
          "destination": "LHR",
          "originTerminal": "2",
          "destinationTerminal": "2",
          "duration": 85,
          "mileage": 278,
          "meal": "Food and Beverages for Purchase"
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
        "id": "ACIztrtOWe5/ixXvBpAqZ5H5yy5+E8t+xtSUqHtzWnnA",
        "carrier": "EI",
        "origin": "NYC",
        "destination": "DUB",
        "basisCode": "MK1US"
       },
       {
        "kind": "qpxexpress#fareInfo",
        "id": "AN9DIwfA4PfJ+xPIC+77bAn4q+IGAiAAVWTDETVbDPEc",
        "carrier": "EI",
        "origin": "DUB",
        "destination": "LON",
        "basisCode": "VOW26GDS"
       }
      ],
      "segmentPricing": [
       {
        "kind": "qpxexpress#segmentPricing",
        "fareId": "AN9DIwfA4PfJ+xPIC+77bAn4q+IGAiAAVWTDETVbDPEc",
        "segmentId": "GLfWNgzdxStELGhJ"
       },
       {
        "kind": "qpxexpress#segmentPricing",
        "fareId": "ACIztrtOWe5/ixXvBpAqZ5H5yy5+E8t+xtSUqHtzWnnA",
        "segmentId": "G3Zqa3yIdmCK+vqb"
       }
      ],
      "baseFareTotal": "USD734.00",
      "saleFareTotal": "USD734.00",
      "saleTaxTotal": "USD69.27",
      "saleTotal": "USD803.27",
      "passengers": {
       "kind": "qpxexpress#passengerCounts",
       "adultCount": 1
      },
      "tax": [
       {
        "kind": "qpxexpress#taxInfo",
        "id": "UP_001",
        "chargeType": "GOVERNMENT",
        "code": "UP",
        "country": "IE",
        "salePrice": "USD13.10"
       },
       {
        "kind": "qpxexpress#taxInfo",
        "id": "YQ_F",
        "chargeType": "CARRIER_SURCHARGE",
        "code": "YQ",
        "salePrice": "USD21.90"
       },
       {
        "kind": "qpxexpress#taxInfo",
        "id": "YQ_F",
        "chargeType": "CARRIER_SURCHARGE",
        "code": "YQ",
        "salePrice": "USD6.37"
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
      "fareCalculation": "NYC EI X/DUB Q90.00 526.00MK1US EI LHR 118.25VOW26GDS NUC 734.25 END ROE 1.00 FARE USD 734.00 XT 17.80US 5.60AY 13.10UP 28.27YQ 4.50XF JFK4.50",
      "latestTicketingTime": "2016-05-10T17:58-04:00",
      "ptc": "ADT"
     }
    ]
   },
   {
    "kind": "qpxexpress#tripOption",
    "saleTotal": "USD809.57",
    "id": "LgTYp0kFZU8VNuBuRvQjMM00F",
    "slice": [
     {
      "kind": "qpxexpress#sliceInfo",
      "duration": 885,
      "segment": [
       {
        "kind": "qpxexpress#segmentInfo",
        "duration": 400,
        "flight": {
         "carrier": "EI",
         "number": "108"
        },
        "id": "G3Zqa3yIdmCK+vqb",
        "cabin": "COACH",
        "bookingCode": "M",
        "bookingCodeCount": 4,
        "marriedSegmentGroup": "0",
        "leg": [
         {
          "kind": "qpxexpress#legInfo",
          "id": "LvfPDgbO25dNEwVW",
          "aircraft": "330",
          "arrivalTime": "2016-06-12T08:40+01:00",
          "departureTime": "2016-06-11T21:00-04:00",
          "origin": "JFK",
          "destination": "DUB",
          "originTerminal": "5",
          "destinationTerminal": "2",
          "duration": 400,
          "mileage": 3169,
          "meal": "Meal",
          "secure": true
         }
        ],
        "connectionDuration": 400
       },
       {
        "kind": "qpxexpress#segmentInfo",
        "duration": 85,
        "flight": {
         "carrier": "EI",
         "number": "8337"
        },
        "id": "GAfoXeFHTzK2C6jx",
        "cabin": "COACH",
        "bookingCode": "V",
        "bookingCodeCount": 4,
        "marriedSegmentGroup": "1",
        "leg": [
         {
          "kind": "qpxexpress#legInfo",
          "id": "L2P-v3MyWTrFuk-Y",
          "aircraft": "319",
          "arrivalTime": "2016-06-12T16:45+01:00",
          "departureTime": "2016-06-12T15:20+01:00",
          "origin": "DUB",
          "destination": "LHR",
          "originTerminal": "1",
          "destinationTerminal": "5",
          "duration": 85,
          "operatingDisclosure": "OPERATED BY BA BRITISH AIRWAYS",
          "mileage": 278,
          "secure": true
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
        "id": "ACIztrtOWe5/ixXvBpAqZ5H5yy5+E8t+xtSUqHtzWnnA",
        "carrier": "EI",
        "origin": "NYC",
        "destination": "DUB",
        "basisCode": "MK1US"
       },
       {
        "kind": "qpxexpress#fareInfo",
        "id": "AN9DIwfA4PfJ+xPIC+77bAn4q+IGAiAAVWTDETVbDPEc",
        "carrier": "EI",
        "origin": "DUB",
        "destination": "LON",
        "basisCode": "VOW26GDS"
       }
      ],
      "segmentPricing": [
       {
        "kind": "qpxexpress#segmentPricing",
        "fareId": "ACIztrtOWe5/ixXvBpAqZ5H5yy5+E8t+xtSUqHtzWnnA",
        "segmentId": "G3Zqa3yIdmCK+vqb"
       },
       {
        "kind": "qpxexpress#segmentPricing",
        "fareId": "AN9DIwfA4PfJ+xPIC+77bAn4q+IGAiAAVWTDETVbDPEc",
        "segmentId": "GAfoXeFHTzK2C6jx"
       }
      ],
      "baseFareTotal": "USD734.00",
      "saleFareTotal": "USD734.00",
      "saleTaxTotal": "USD75.57",
      "saleTotal": "USD809.57",
      "passengers": {
       "kind": "qpxexpress#passengerCounts",
       "adultCount": 1
      },
      "tax": [
       {
        "kind": "qpxexpress#taxInfo",
        "id": "UP_001",
        "chargeType": "GOVERNMENT",
        "code": "UP",
        "country": "IE",
        "salePrice": "USD19.40"
       },
       {
        "kind": "qpxexpress#taxInfo",
        "id": "YQ_F",
        "chargeType": "CARRIER_SURCHARGE",
        "code": "YQ",
        "salePrice": "USD21.90"
       },
       {
        "kind": "qpxexpress#taxInfo",
        "id": "YQ_F",
        "chargeType": "CARRIER_SURCHARGE",
        "code": "YQ",
        "salePrice": "USD6.37"
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
      "fareCalculation": "NYC EI X/DUB Q90.00 526.00MK1US EI LHR 118.25VOW26GDS NUC 734.25 END ROE 1.00 FARE USD 734.00 XT 17.80US 5.60AY 19.40UP 28.27YQ 4.50XF JFK4.50",
      "latestTicketingTime": "2016-05-10T17:58-04:00",
      "ptc": "ADT"
     }
    ]
   },
   {
    "kind": "qpxexpress#tripOption",
    "saleTotal": "USD812.47",
    "id": "LgTYp0kFZU8VNuBuRvQjMM007",
    "slice": [
     {
      "kind": "qpxexpress#sliceInfo",
      "duration": 645,
      "segment": [
       {
        "kind": "qpxexpress#segmentInfo",
        "duration": 390,
        "flight": {
         "carrier": "EI",
         "number": "110"
        },
        "id": "Gu465SBu-7-wfgg4",
        "cabin": "COACH",
        "bookingCode": "M",
        "bookingCodeCount": 4,
        "marriedSegmentGroup": "0",
        "leg": [
         {
          "kind": "qpxexpress#legInfo",
          "id": "LBbsjh-bEooFJhee",
          "aircraft": "757",
          "arrivalTime": "2016-06-12T06:00+01:00",
          "departureTime": "2016-06-11T18:30-04:00",
          "origin": "JFK",
          "destination": "SNN",
          "originTerminal": "5",
          "duration": 390,
          "operatingDisclosure": "OPERATED BY AG ASL AIRLINES IRL",
          "mileage": 3072,
          "meal": "Meal",
          "secure": true
         }
        ],
        "connectionDuration": 165
       },
       {
        "kind": "qpxexpress#segmentInfo",
        "duration": 90,
        "flight": {
         "carrier": "EI",
         "number": "380"
        },
        "id": "GDEjm2MlRD3j3mC-",
        "cabin": "COACH",
        "bookingCode": "H",
        "bookingCodeCount": 4,
        "marriedSegmentGroup": "1",
        "leg": [
         {
          "kind": "qpxexpress#legInfo",
          "id": "L9U9AL2kkYDPmzYL",
          "aircraft": "319",
          "arrivalTime": "2016-06-12T10:15+01:00",
          "departureTime": "2016-06-12T08:45+01:00",
          "origin": "SNN",
          "destination": "LHR",
          "destinationTerminal": "2",
          "duration": 90,
          "mileage": 368,
          "meal": "Food and Beverages for Purchase"
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
        "id": "AKguzrtPap7vmtMAaRyb4/tBr4gZ/NvaPY6WmkyE7OYw",
        "carrier": "EI",
        "origin": "NYC",
        "destination": "LON",
        "basisCode": "MK1US"
       }
      ],
      "segmentPricing": [
       {
        "kind": "qpxexpress#segmentPricing",
        "fareId": "AKguzrtPap7vmtMAaRyb4/tBr4gZ/NvaPY6WmkyE7OYw",
        "segmentId": "Gu465SBu-7-wfgg4"
       },
       {
        "kind": "qpxexpress#segmentPricing",
        "fareId": "AKguzrtPap7vmtMAaRyb4/tBr4gZ/NvaPY6WmkyE7OYw",
        "segmentId": "GDEjm2MlRD3j3mC-"
       }
      ],
      "baseFareTotal": "USD761.00",
      "saleFareTotal": "USD761.00",
      "saleTaxTotal": "USD51.47",
      "saleTotal": "USD812.47",
      "passengers": {
       "kind": "qpxexpress#passengerCounts",
       "adultCount": 1
      },
      "tax": [
       {
        "kind": "qpxexpress#taxInfo",
        "id": "UP_001",
        "chargeType": "GOVERNMENT",
        "code": "UP",
        "country": "IE",
        "salePrice": "USD0.90"
       },
       {
        "kind": "qpxexpress#taxInfo",
        "id": "YQ_F",
        "chargeType": "CARRIER_SURCHARGE",
        "code": "YQ",
        "salePrice": "USD16.30"
       },
       {
        "kind": "qpxexpress#taxInfo",
        "id": "YQ_F",
        "chargeType": "CARRIER_SURCHARGE",
        "code": "YQ",
        "salePrice": "USD6.37"
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
      "fareCalculation": "NYC EI X/SNN Q90.00 EI LHR 671.00MK1US NUC 761.00 END ROE 1.00 FARE USD 761.00 XT 17.80US 5.60AY 0.90UP 22.67YQ 4.50XF JFK4.50",
      "latestTicketingTime": "2016-05-10T17:58-04:00",
      "ptc": "ADT"
     }
    ]
   },
   {
    "kind": "qpxexpress#tripOption",
    "saleTotal": "USD828.27",
    "id": "LgTYp0kFZU8VNuBuRvQjMM009",
    "slice": [
     {
      "kind": "qpxexpress#sliceInfo",
      "duration": 670,
      "segment": [
       {
        "kind": "qpxexpress#segmentInfo",
        "duration": 400,
        "flight": {
         "carrier": "EI",
         "number": "108"
        },
        "id": "G3Zqa3yIdmCK+vqb",
        "cabin": "COACH",
        "bookingCode": "M",
        "bookingCodeCount": 4,
        "marriedSegmentGroup": "0",
        "leg": [
         {
          "kind": "qpxexpress#legInfo",
          "id": "LvfPDgbO25dNEwVW",
          "aircraft": "330",
          "arrivalTime": "2016-06-12T08:40+01:00",
          "departureTime": "2016-06-11T21:00-04:00",
          "origin": "JFK",
          "destination": "DUB",
          "originTerminal": "5",
          "destinationTerminal": "2",
          "duration": 400,
          "mileage": 3169,
          "meal": "Meal",
          "secure": true
         }
        ],
        "connectionDuration": 180
       },
       {
        "kind": "qpxexpress#segmentInfo",
        "duration": 90,
        "flight": {
         "carrier": "EI",
         "number": "8327"
        },
        "id": "Gv9j14FBFPEyHKaB",
        "cabin": "COACH",
        "bookingCode": "K",
        "bookingCodeCount": 4,
        "marriedSegmentGroup": "1",
        "leg": [
         {
          "kind": "qpxexpress#legInfo",
          "id": "LvAGw391HW6sNLkV",
          "aircraft": "319",
          "arrivalTime": "2016-06-12T13:10+01:00",
          "departureTime": "2016-06-12T11:40+01:00",
          "origin": "DUB",
          "destination": "LHR",
          "originTerminal": "1",
          "destinationTerminal": "5",
          "duration": 90,
          "operatingDisclosure": "OPERATED BY BA BRITISH AIRWAYS",
          "mileage": 278,
          "secure": true
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
        "id": "ACIztrtOWe5/ixXvBpAqZ5H5yy5+E8t+xtSUqHtzWnnA",
        "carrier": "EI",
        "origin": "NYC",
        "destination": "DUB",
        "basisCode": "MK1US"
       },
       {
        "kind": "qpxexpress#fareInfo",
        "id": "ArEnjf/RXEYdLg+cee/ZxXOaa/nvzTSFDuC1DSqIbkZs",
        "carrier": "EI",
        "origin": "DUB",
        "destination": "LON",
        "basisCode": "KOW26GDS"
       }
      ],
      "segmentPricing": [
       {
        "kind": "qpxexpress#segmentPricing",
        "fareId": "ArEnjf/RXEYdLg+cee/ZxXOaa/nvzTSFDuC1DSqIbkZs",
        "segmentId": "Gv9j14FBFPEyHKaB"
       },
       {
        "kind": "qpxexpress#segmentPricing",
        "fareId": "ACIztrtOWe5/ixXvBpAqZ5H5yy5+E8t+xtSUqHtzWnnA",
        "segmentId": "G3Zqa3yIdmCK+vqb"
       }
      ],
      "baseFareTotal": "USD759.00",
      "saleFareTotal": "USD759.00",
      "saleTaxTotal": "USD69.27",
      "saleTotal": "USD828.27",
      "passengers": {
       "kind": "qpxexpress#passengerCounts",
       "adultCount": 1
      },
      "tax": [
       {
        "kind": "qpxexpress#taxInfo",
        "id": "UP_001",
        "chargeType": "GOVERNMENT",
        "code": "UP",
        "country": "IE",
        "salePrice": "USD13.10"
       },
       {
        "kind": "qpxexpress#taxInfo",
        "id": "YQ_F",
        "chargeType": "CARRIER_SURCHARGE",
        "code": "YQ",
        "salePrice": "USD21.90"
       },
       {
        "kind": "qpxexpress#taxInfo",
        "id": "YQ_F",
        "chargeType": "CARRIER_SURCHARGE",
        "code": "YQ",
        "salePrice": "USD6.37"
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
      "fareCalculation": "NYC EI X/DUB Q90.00 526.00MK1US EI LHR 143.44KOW26GDS NUC 759.44 END ROE 1.00 FARE USD 759.00 XT 17.80US 5.60AY 13.10UP 28.27YQ 4.50XF JFK4.50",
      "latestTicketingTime": "2016-05-10T17:58-04:00",
      "ptc": "ADT"
     }
    ]
   },
   {
    "kind": "qpxexpress#tripOption",
    "saleTotal": "USD857.27",
    "id": "LgTYp0kFZU8VNuBuRvQjMM008",
    "slice": [
     {
      "kind": "qpxexpress#sliceInfo",
      "duration": 575,
      "segment": [
       {
        "kind": "qpxexpress#segmentInfo",
        "duration": 400,
        "flight": {
         "carrier": "EI",
         "number": "104"
        },
        "id": "GMYKWIcM2VtlwCy3",
        "cabin": "COACH",
        "bookingCode": "K",
        "bookingCodeCount": 4,
        "marriedSegmentGroup": "0",
        "leg": [
         {
          "kind": "qpxexpress#legInfo",
          "id": "LsU6YJmCYFvhvV6W",
          "aircraft": "330",
          "arrivalTime": "2016-06-12T05:10+01:00",
          "departureTime": "2016-06-11T17:30-04:00",
          "origin": "JFK",
          "destination": "DUB",
          "originTerminal": "5",
          "destinationTerminal": "2",
          "duration": 400,
          "mileage": 3169,
          "meal": "Meal",
          "secure": true
         }
        ],
        "connectionDuration": 90
       },
       {
        "kind": "qpxexpress#segmentInfo",
        "duration": 85,
        "flight": {
         "carrier": "EI",
         "number": "152"
        },
        "id": "Gk8zIF+il1s3RK-k",
        "cabin": "COACH",
        "bookingCode": "F",
        "bookingCodeCount": 4,
        "marriedSegmentGroup": "1",
        "leg": [
         {
          "kind": "qpxexpress#legInfo",
          "id": "LWk43sU8h6VC2opV",
          "aircraft": "320",
          "arrivalTime": "2016-06-12T08:05+01:00",
          "departureTime": "2016-06-12T06:40+01:00",
          "origin": "DUB",
          "destination": "LHR",
          "originTerminal": "2",
          "destinationTerminal": "2",
          "duration": 85,
          "mileage": 278,
          "meal": "Food and Beverages for Purchase"
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
        "id": "Ahm9zDKISj7OUSRRahqh+KKCzrczjHlw3XAl2fzRQ89w",
        "carrier": "EI",
        "origin": "NYC",
        "destination": "DUB",
        "basisCode": "KK1US"
       },
       {
        "kind": "qpxexpress#fareInfo",
        "id": "AWnu1IgD58t41Jl+t2piVpe0G0R1+8MUpHcXW1z8RX3/",
        "carrier": "EI",
        "origin": "DUB",
        "destination": "LON",
        "basisCode": "FOW26GDS"
       }
      ],
      "segmentPricing": [
       {
        "kind": "qpxexpress#segmentPricing",
        "fareId": "Ahm9zDKISj7OUSRRahqh+KKCzrczjHlw3XAl2fzRQ89w",
        "segmentId": "GMYKWIcM2VtlwCy3"
       },
       {
        "kind": "qpxexpress#segmentPricing",
        "fareId": "AWnu1IgD58t41Jl+t2piVpe0G0R1+8MUpHcXW1z8RX3/",
        "segmentId": "Gk8zIF+il1s3RK-k"
       }
      ],
      "baseFareTotal": "USD788.00",
      "saleFareTotal": "USD788.00",
      "saleTaxTotal": "USD69.27",
      "saleTotal": "USD857.27",
      "passengers": {
       "kind": "qpxexpress#passengerCounts",
       "adultCount": 1
      },
      "tax": [
       {
        "kind": "qpxexpress#taxInfo",
        "id": "UP_001",
        "chargeType": "GOVERNMENT",
        "code": "UP",
        "country": "IE",
        "salePrice": "USD13.10"
       },
       {
        "kind": "qpxexpress#taxInfo",
        "id": "YQ_F",
        "chargeType": "CARRIER_SURCHARGE",
        "code": "YQ",
        "salePrice": "USD21.90"
       },
       {
        "kind": "qpxexpress#taxInfo",
        "id": "YQ_F",
        "chargeType": "CARRIER_SURCHARGE",
        "code": "YQ",
        "salePrice": "USD6.37"
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
      "fareCalculation": "NYC EI X/DUB Q90.00 591.00KK1US EI LHR 107.30FOW26GDS NUC 788.30 END ROE 1.00 FARE USD 788.00 XT 17.80US 5.60AY 13.10UP 28.27YQ 4.50XF JFK4.50",
      "latestTicketingTime": "2016-05-10T17:58-04:00",
      "ptc": "ADT"
     }
    ]
   },
   {
    "kind": "qpxexpress#tripOption",
    "saleTotal": "USD874.20",
    "id": "LgTYp0kFZU8VNuBuRvQjMM00K",
    "slice": [
     {
      "kind": "qpxexpress#sliceInfo",
      "duration": 995,
      "segment": [
       {
        "kind": "qpxexpress#segmentInfo",
        "duration": 330,
        "flight": {
         "carrier": "FI",
         "number": "612"
        },
        "id": "GNkjNL65DhDfxw-M",
        "cabin": "COACH",
        "bookingCode": "B",
        "bookingCodeCount": 5,
        "marriedSegmentGroup": "0",
        "leg": [
         {
          "kind": "qpxexpress#legInfo",
          "id": "LkokNtijo00ykYV-",
          "aircraft": "75W",
          "arrivalTime": "2016-06-11T23:40+00:00",
          "departureTime": "2016-06-11T14:10-04:00",
          "origin": "JFK",
          "destination": "KEF",
          "originTerminal": "7",
          "duration": 330,
          "mileage": 2585,
          "meal": "Alcoholic Beverages for Purchase",
          "secure": true
         }
        ],
        "connectionDuration": 480
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
        "bookingCode": "B",
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
        "id": "AIiLzoZoTunss39nqplAOtIxMLf1gSMNYEhrR5t1an5I",
        "carrier": "FI",
        "origin": "NYC",
        "destination": "LON",
        "basisCode": "BQO2FLEX"
       }
      ],
      "segmentPricing": [
       {
        "kind": "qpxexpress#segmentPricing",
        "fareId": "AIiLzoZoTunss39nqplAOtIxMLf1gSMNYEhrR5t1an5I",
        "segmentId": "GNkjNL65DhDfxw-M"
       },
       {
        "kind": "qpxexpress#segmentPricing",
        "fareId": "AIiLzoZoTunss39nqplAOtIxMLf1gSMNYEhrR5t1an5I",
        "segmentId": "GRLnblT1o3qNDpUL"
       }
      ],
      "baseFareTotal": "USD736.00",
      "saleFareTotal": "USD736.00",
      "saleTaxTotal": "USD138.20",
      "saleTotal": "USD874.20",
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
      "fareCalculation": "NYC FI X/REK FI LON 736.00BQO2FLEX NUC 736.00 END ROE 1.00 FARE USD 736.00 XT 17.80US 5.60AY 3.70IS 6.60ZU 100.00YR 4.50XF JFK4.50",
      "latestTicketingTime": "2016-05-16T23:59-04:00",
      "ptc": "ADT",
      "refundable": true
     }
    ]
   },
   {
    "kind": "qpxexpress#tripOption",
    "saleTotal": "USD882.27",
    "id": "LgTYp0kFZU8VNuBuRvQjMM00C",
    "slice": [
     {
      "kind": "qpxexpress#sliceInfo",
      "duration": 635,
      "segment": [
       {
        "kind": "qpxexpress#segmentInfo",
        "duration": 400,
        "flight": {
         "carrier": "EI",
         "number": "104"
        },
        "id": "GMYKWIcM2VtlwCy3",
        "cabin": "COACH",
        "bookingCode": "K",
        "bookingCodeCount": 4,
        "marriedSegmentGroup": "0",
        "leg": [
         {
          "kind": "qpxexpress#legInfo",
          "id": "LsU6YJmCYFvhvV6W",
          "aircraft": "330",
          "arrivalTime": "2016-06-12T05:10+01:00",
          "departureTime": "2016-06-11T17:30-04:00",
          "origin": "JFK",
          "destination": "DUB",
          "originTerminal": "5",
          "destinationTerminal": "2",
          "duration": 400,
          "mileage": 3169,
          "meal": "Meal",
          "secure": true
         }
        ],
        "connectionDuration": 150
       },
       {
        "kind": "qpxexpress#segmentInfo",
        "duration": 85,
        "flight": {
         "carrier": "EI",
         "number": "154"
        },
        "id": "GVlKu7fqwUlpOrx9",
        "cabin": "COACH",
        "bookingCode": "M",
        "bookingCodeCount": 4,
        "marriedSegmentGroup": "1",
        "leg": [
         {
          "kind": "qpxexpress#legInfo",
          "id": "LckHgGkwMY47nKJJ",
          "aircraft": "320",
          "arrivalTime": "2016-06-12T09:05+01:00",
          "departureTime": "2016-06-12T07:40+01:00",
          "origin": "DUB",
          "destination": "LHR",
          "originTerminal": "2",
          "destinationTerminal": "2",
          "duration": 85,
          "mileage": 278,
          "meal": "Food and Beverages for Purchase"
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
        "id": "Ahm9zDKISj7OUSRRahqh+KKCzrczjHlw3XAl2fzRQ89w",
        "carrier": "EI",
        "origin": "NYC",
        "destination": "DUB",
        "basisCode": "KK1US"
       },
       {
        "kind": "qpxexpress#fareInfo",
        "id": "AK1GQus5R3eXfcg8DxSCHKQbmpH3Ck1XH/062SkZBjjg",
        "carrier": "EI",
        "origin": "DUB",
        "destination": "LON",
        "basisCode": "MOW26GDS"
       }
      ],
      "segmentPricing": [
       {
        "kind": "qpxexpress#segmentPricing",
        "fareId": "AK1GQus5R3eXfcg8DxSCHKQbmpH3Ck1XH/062SkZBjjg",
        "segmentId": "GVlKu7fqwUlpOrx9"
       },
       {
        "kind": "qpxexpress#segmentPricing",
        "fareId": "Ahm9zDKISj7OUSRRahqh+KKCzrczjHlw3XAl2fzRQ89w",
        "segmentId": "GMYKWIcM2VtlwCy3"
       }
      ],
      "baseFareTotal": "USD813.00",
      "saleFareTotal": "USD813.00",
      "saleTaxTotal": "USD69.27",
      "saleTotal": "USD882.27",
      "passengers": {
       "kind": "qpxexpress#passengerCounts",
       "adultCount": 1
      },
      "tax": [
       {
        "kind": "qpxexpress#taxInfo",
        "id": "UP_001",
        "chargeType": "GOVERNMENT",
        "code": "UP",
        "country": "IE",
        "salePrice": "USD13.10"
       },
       {
        "kind": "qpxexpress#taxInfo",
        "id": "YQ_F",
        "chargeType": "CARRIER_SURCHARGE",
        "code": "YQ",
        "salePrice": "USD21.90"
       },
       {
        "kind": "qpxexpress#taxInfo",
        "id": "YQ_F",
        "chargeType": "CARRIER_SURCHARGE",
        "code": "YQ",
        "salePrice": "USD6.37"
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
      "fareCalculation": "NYC EI X/DUB Q90.00 591.00KK1US EI LHR 132.49MOW26GDS NUC 813.49 END ROE 1.00 FARE USD 813.00 XT 17.80US 5.60AY 13.10UP 28.27YQ 4.50XF JFK4.50",
      "latestTicketingTime": "2016-05-10T17:58-04:00",
      "ptc": "ADT"
     }
    ]
   },
   {
    "kind": "qpxexpress#tripOption",
    "saleTotal": "USD890.60",
    "id": "LgTYp0kFZU8VNuBuRvQjMM00H",
    "slice": [
     {
      "kind": "qpxexpress#sliceInfo",
      "duration": 950,
      "segment": [
       {
        "kind": "qpxexpress#segmentInfo",
        "duration": 590,
        "flight": {
         "carrier": "TK",
         "number": "12"
        },
        "id": "Gz0RNITWzjdq1M8I",
        "cabin": "COACH",
        "bookingCode": "M",
        "bookingCodeCount": 9,
        "marriedSegmentGroup": "0",
        "leg": [
         {
          "kind": "qpxexpress#legInfo",
          "id": "Lh9vlXq2l34kKPiD",
          "aircraft": "77W",
          "arrivalTime": "2016-06-12T16:45+03:00",
          "departureTime": "2016-06-11T23:55-04:00",
          "origin": "JFK",
          "destination": "IST",
          "originTerminal": "1",
          "destinationTerminal": "I",
          "duration": 590,
          "mileage": 5001,
          "meal": "Meal",
          "secure": true
         }
        ],
        "connectionDuration": 115
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
        "id": "AvXRnuI1WEFYyGs4OUwFuM5GrzMdKHIjOLLJm3oEuQIw",
        "carrier": "TK",
        "origin": "NYC",
        "destination": "LON",
        "basisCode": "MHVOW"
       }
      ],
      "segmentPricing": [
       {
        "kind": "qpxexpress#segmentPricing",
        "fareId": "AvXRnuI1WEFYyGs4OUwFuM5GrzMdKHIjOLLJm3oEuQIw",
        "segmentId": "Gz0RNITWzjdq1M8I"
       },
       {
        "kind": "qpxexpress#segmentPricing",
        "fareId": "AvXRnuI1WEFYyGs4OUwFuM5GrzMdKHIjOLLJm3oEuQIw",
        "segmentId": "G2aATo-gKAya4osF"
       }
      ],
      "baseFareTotal": "USD687.00",
      "saleFareTotal": "USD687.00",
      "saleTaxTotal": "USD203.60",
      "saleTotal": "USD890.60",
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
      "fareCalculation": "NYC TK X/IST TK LON 687.00MHVOW NUC 687.00 END ROE 1.00 FARE USD 687.00 XT 17.80US 5.60AY 5.70TR 170.00YR 4.50XF JFK4.50",
      "latestTicketingTime": "2016-06-11T23:54-04:00",
      "ptc": "ADT",
      "refundable": true
     }
    ]
   },
   {
    "kind": "qpxexpress#tripOption",
    "saleTotal": "USD890.60",
    "id": "LgTYp0kFZU8VNuBuRvQjMM00J",
    "slice": [
     {
      "kind": "qpxexpress#sliceInfo",
      "duration": 985,
      "segment": [
       {
        "kind": "qpxexpress#segmentInfo",
        "duration": 590,
        "flight": {
         "carrier": "TK",
         "number": "4"
        },
        "id": "GLj4I62CSKlDDNVm",
        "cabin": "COACH",
        "bookingCode": "M",
        "bookingCodeCount": 9,
        "marriedSegmentGroup": "0",
        "leg": [
         {
          "kind": "qpxexpress#legInfo",
          "id": "LapmPWp5M0fBDoKh",
          "aircraft": "333",
          "arrivalTime": "2016-06-12T05:15+03:00",
          "departureTime": "2016-06-11T12:25-04:00",
          "origin": "JFK",
          "destination": "IST",
          "originTerminal": "1",
          "destinationTerminal": "I",
          "duration": 590,
          "mileage": 5001,
          "meal": "Meal",
          "secure": true
         }
        ],
        "connectionDuration": 150
       },
       {
        "kind": "qpxexpress#segmentInfo",
        "duration": 245,
        "flight": {
         "carrier": "TK",
         "number": "1979"
        },
        "id": "GjFmyYEW1GamQsVs",
        "cabin": "COACH",
        "bookingCode": "M",
        "bookingCodeCount": 9,
        "marriedSegmentGroup": "1",
        "leg": [
         {
          "kind": "qpxexpress#legInfo",
          "id": "LzAupNor6uMEqh0j",
          "aircraft": "77W",
          "arrivalTime": "2016-06-12T09:50+01:00",
          "departureTime": "2016-06-12T07:45+03:00",
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
        "id": "AvXRnuI1WEFYyGs4OUwFuM5GrzMdKHIjOLLJm3oEuQIw",
        "carrier": "TK",
        "origin": "NYC",
        "destination": "LON",
        "basisCode": "MHVOW"
       }
      ],
      "segmentPricing": [
       {
        "kind": "qpxexpress#segmentPricing",
        "fareId": "AvXRnuI1WEFYyGs4OUwFuM5GrzMdKHIjOLLJm3oEuQIw",
        "segmentId": "GjFmyYEW1GamQsVs"
       },
       {
        "kind": "qpxexpress#segmentPricing",
        "fareId": "AvXRnuI1WEFYyGs4OUwFuM5GrzMdKHIjOLLJm3oEuQIw",
        "segmentId": "GLj4I62CSKlDDNVm"
       }
      ],
      "baseFareTotal": "USD687.00",
      "saleFareTotal": "USD687.00",
      "saleTaxTotal": "USD203.60",
      "saleTotal": "USD890.60",
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
      "fareCalculation": "NYC TK X/IST TK LON 687.00MHVOW NUC 687.00 END ROE 1.00 FARE USD 687.00 XT 17.80US 5.60AY 5.70TR 170.00YR 4.50XF JFK4.50",
      "latestTicketingTime": "2016-06-11T12:24-04:00",
      "ptc": "ADT",
      "refundable": true
     }
    ]
   },
   {
    "kind": "qpxexpress#tripOption",
    "saleTotal": "USD890.60",
    "id": "LgTYp0kFZU8VNuBuRvQjMM00I",
    "slice": [
     {
      "kind": "qpxexpress#sliceInfo",
      "duration": 975,
      "segment": [
       {
        "kind": "qpxexpress#segmentInfo",
        "duration": 595,
        "flight": {
         "carrier": "TK",
         "number": "2"
        },
        "id": "GPpFIE+0LioIAZrE",
        "cabin": "COACH",
        "bookingCode": "M",
        "bookingCodeCount": 9,
        "marriedSegmentGroup": "0",
        "leg": [
         {
          "kind": "qpxexpress#legInfo",
          "id": "LPeWRVzZHHc9ptpj",
          "aircraft": "333",
          "arrivalTime": "2016-06-12T12:10+03:00",
          "departureTime": "2016-06-11T19:15-04:00",
          "origin": "JFK",
          "destination": "IST",
          "originTerminal": "1",
          "destinationTerminal": "I",
          "duration": 595,
          "mileage": 5001,
          "meal": "Meal",
          "secure": true
         }
        ],
        "connectionDuration": 135
       },
       {
        "kind": "qpxexpress#segmentInfo",
        "duration": 245,
        "flight": {
         "carrier": "TK",
         "number": "1971"
        },
        "id": "GnHvW330vpX0cymG",
        "cabin": "COACH",
        "bookingCode": "M",
        "bookingCodeCount": 9,
        "marriedSegmentGroup": "1",
        "leg": [
         {
          "kind": "qpxexpress#legInfo",
          "id": "LHj75hOYFSgJlLUP",
          "aircraft": "332",
          "arrivalTime": "2016-06-12T16:30+01:00",
          "departureTime": "2016-06-12T14:25+03:00",
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
        "id": "AvXRnuI1WEFYyGs4OUwFuM5GrzMdKHIjOLLJm3oEuQIw",
        "carrier": "TK",
        "origin": "NYC",
        "destination": "LON",
        "basisCode": "MHVOW"
       }
      ],
      "segmentPricing": [
       {
        "kind": "qpxexpress#segmentPricing",
        "fareId": "AvXRnuI1WEFYyGs4OUwFuM5GrzMdKHIjOLLJm3oEuQIw",
        "segmentId": "GnHvW330vpX0cymG"
       },
       {
        "kind": "qpxexpress#segmentPricing",
        "fareId": "AvXRnuI1WEFYyGs4OUwFuM5GrzMdKHIjOLLJm3oEuQIw",
        "segmentId": "GPpFIE+0LioIAZrE"
       }
      ],
      "baseFareTotal": "USD687.00",
      "saleFareTotal": "USD687.00",
      "saleTaxTotal": "USD203.60",
      "saleTotal": "USD890.60",
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
      "fareCalculation": "NYC TK X/IST TK LON 687.00MHVOW NUC 687.00 END ROE 1.00 FARE USD 687.00 XT 17.80US 5.60AY 5.70TR 170.00YR 4.50XF JFK4.50",
      "latestTicketingTime": "2016-06-11T19:14-04:00",
      "ptc": "ADT",
      "refundable": true
     }
    ]
   },
   {
    "kind": "qpxexpress#tripOption",
    "saleTotal": "USD893.27",
    "id": "LgTYp0kFZU8VNuBuRvQjMM00D",
    "slice": [
     {
      "kind": "qpxexpress#sliceInfo",
      "duration": 640,
      "segment": [
       {
        "kind": "qpxexpress#segmentInfo",
        "duration": 400,
        "flight": {
         "carrier": "EI",
         "number": "104"
        },
        "id": "GMYKWIcM2VtlwCy3",
        "cabin": "COACH",
        "bookingCode": "K",
        "bookingCodeCount": 4,
        "marriedSegmentGroup": "0",
        "leg": [
         {
          "kind": "qpxexpress#legInfo",
          "id": "LsU6YJmCYFvhvV6W",
          "aircraft": "330",
          "arrivalTime": "2016-06-12T05:10+01:00",
          "departureTime": "2016-06-11T17:30-04:00",
          "origin": "JFK",
          "destination": "DUB",
          "originTerminal": "5",
          "destinationTerminal": "2",
          "duration": 400,
          "mileage": 3169,
          "meal": "Meal",
          "secure": true
         }
        ],
        "connectionDuration": 150
       },
       {
        "kind": "qpxexpress#segmentInfo",
        "duration": 90,
        "flight": {
         "carrier": "EI",
         "number": "8331"
        },
        "id": "GjhLpoyQWOJc24QG",
        "cabin": "COACH",
        "bookingCode": "K",
        "bookingCodeCount": 4,
        "marriedSegmentGroup": "1",
        "leg": [
         {
          "kind": "qpxexpress#legInfo",
          "id": "LDQd2q3OgLE9Se53",
          "aircraft": "319",
          "arrivalTime": "2016-06-12T09:10+01:00",
          "departureTime": "2016-06-12T07:40+01:00",
          "origin": "DUB",
          "destination": "LHR",
          "originTerminal": "1",
          "destinationTerminal": "5",
          "duration": 90,
          "operatingDisclosure": "OPERATED BY BA BRITISH AIRWAYS",
          "mileage": 278,
          "secure": true
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
        "id": "Ahm9zDKISj7OUSRRahqh+KKCzrczjHlw3XAl2fzRQ89w",
        "carrier": "EI",
        "origin": "NYC",
        "destination": "DUB",
        "basisCode": "KK1US"
       },
       {
        "kind": "qpxexpress#fareInfo",
        "id": "ArEnjf/RXEYdLg+cee/ZxXOaa/nvzTSFDuC1DSqIbkZs",
        "carrier": "EI",
        "origin": "DUB",
        "destination": "LON",
        "basisCode": "KOW26GDS"
       }
      ],
      "segmentPricing": [
       {
        "kind": "qpxexpress#segmentPricing",
        "fareId": "ArEnjf/RXEYdLg+cee/ZxXOaa/nvzTSFDuC1DSqIbkZs",
        "segmentId": "GjhLpoyQWOJc24QG"
       },
       {
        "kind": "qpxexpress#segmentPricing",
        "fareId": "Ahm9zDKISj7OUSRRahqh+KKCzrczjHlw3XAl2fzRQ89w",
        "segmentId": "GMYKWIcM2VtlwCy3"
       }
      ],
      "baseFareTotal": "USD824.00",
      "saleFareTotal": "USD824.00",
      "saleTaxTotal": "USD69.27",
      "saleTotal": "USD893.27",
      "passengers": {
       "kind": "qpxexpress#passengerCounts",
       "adultCount": 1
      },
      "tax": [
       {
        "kind": "qpxexpress#taxInfo",
        "id": "UP_001",
        "chargeType": "GOVERNMENT",
        "code": "UP",
        "country": "IE",
        "salePrice": "USD13.10"
       },
       {
        "kind": "qpxexpress#taxInfo",
        "id": "YQ_F",
        "chargeType": "CARRIER_SURCHARGE",
        "code": "YQ",
        "salePrice": "USD21.90"
       },
       {
        "kind": "qpxexpress#taxInfo",
        "id": "YQ_F",
        "chargeType": "CARRIER_SURCHARGE",
        "code": "YQ",
        "salePrice": "USD6.37"
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
      "fareCalculation": "NYC EI X/DUB Q90.00 591.00KK1US EI LHR 143.44KOW26GDS NUC 824.44 END ROE 1.00 FARE USD 824.00 XT 17.80US 5.60AY 13.10UP 28.27YQ 4.50XF JFK4.50",
      "latestTicketingTime": "2016-05-10T17:58-04:00",
      "ptc": "ADT"
     }
    ]
   }
  ]
 }
}
