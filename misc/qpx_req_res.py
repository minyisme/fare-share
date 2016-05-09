JSON REQUEST SAMPLE:

{
  "request": {
    "slice": [
      {
        "origin": "SFO",
        "destination": "LHR",
        "date": "2016-05-11"
      }
    ],
    "passengers": {
      "adultCount": 1,
      "infantInLapCount": 0,
      "infantInSeatCount": 0,
      "childCount": 0,
      "seniorCount": 0
    },
    "solutions": 20,
    "maxPrice": "USD800.00",
    "refundable": false
  }
}

JSON REQUEST STRUCTURE:

{
  "request": {
    "passengers": {
      "kind": "qpxexpress#passengerCounts",
      "adultCount": integer,
      "childCount": integer,
      "infantInLapCount": integer,
      "infantInSeatCount": integer,
      "seniorCount": integer
    },
    "slice": [
      {
        "kind": "qpxexpress#sliceInput",
        "origin": string,
        "destination": string,
        "date": string,
        "maxStops": integer,
        "maxConnectionDuration": integer,
        "preferredCabin": string,
        "permittedDepartureTime": {
          "kind": "qpxexpress#timeOfDayRange",
          "earliestTime": string,
          "latestTime": string
        },
        "permittedCarrier": [
          string
        ],
        "alliance": string,
        "prohibitedCarrier": [
          string
        ]
      }
    ],
    "maxPrice": string,
    "saleCountry": string,
    "refundable": boolean,
    "solutions": integer
  }
}

JSON RESULT SAMPLE:

{
 "kind": "qpxExpress#tripsSearch",
 "trips": {
  "kind": "qpxexpress#tripOptions",
  "requestId": "gvvTiCEUeIsgS8R0q0OIuG",
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
     "code": "SFO",
     "city": "SFO",
     "name": "San Francisco International"
    }
   ],
   "city": [
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
     "code": "SFO",
     "name": "San Francisco"
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
    "saleTotal": "USD708.60",
    "id": "6empvn45ipLTmBrLTmNqE1002",
    "slice": [
     {
      "kind": "qpxexpress#sliceInfo",
      "duration": 1220,
      "segment": [
       {
        "kind": "qpxexpress#segmentInfo",
        "duration": 785,
        "flight": {
         "carrier": "TK",
         "number": "80"
        },
        "id": "G7OcLe0KQx2LHVKk",
        "cabin": "COACH",
        "bookingCode": "S",
        "bookingCodeCount": 9,
        "marriedSegmentGroup": "0",
        "leg": [
         {
          "kind": "qpxexpress#legInfo",
          "id": "LKuHk5mT1V3mWnTm",
          "aircraft": "77W",
          "arrivalTime": "2016-05-12T17:15+03:00",
          "departureTime": "2016-05-11T18:10-07:00",
          "origin": "SFO",
          "destination": "IST",
          "originTerminal": "I",
          "destinationTerminal": "I",
          "duration": 785,
          "mileage": 6706,
          "meal": "Meal",
          "secure": true
         }
        ],
        "connectionDuration": 185
       },
       {
        "kind": "qpxexpress#segmentInfo",
        "duration": 250,
        "flight": {
         "carrier": "TK",
         "number": "1987"
        },
        "id": "GGqD9FUmx0R35Pjm",
        "cabin": "COACH",
        "bookingCode": "S",
        "bookingCodeCount": 9,
        "marriedSegmentGroup": "1",
        "leg": [
         {
          "kind": "qpxexpress#legInfo",
          "id": "LZoes5SYO+YHIZWe",
          "aircraft": "32B",
          "arrivalTime": "2016-05-12T22:30+01:00",
          "departureTime": "2016-05-12T20:20+03:00",
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
        "id": "AE9DkkWrJat7UBwOlw23zyvgu4X0HJKcHRmx1614XNHE",
        "carrier": "TK",
        "origin": "SFO",
        "destination": "LON",
        "basisCode": "SLV3PXOW"
       }
      ],
      "segmentPricing": [
       {
        "kind": "qpxexpress#segmentPricing",
        "fareId": "AE9DkkWrJat7UBwOlw23zyvgu4X0HJKcHRmx1614XNHE",
        "segmentId": "GGqD9FUmx0R35Pjm"
       },
       {
        "kind": "qpxexpress#segmentPricing",
        "fareId": "AE9DkkWrJat7UBwOlw23zyvgu4X0HJKcHRmx1614XNHE",
        "segmentId": "G7OcLe0KQx2LHVKk"
       }
      ],
      "baseFareTotal": "USD468.00",
      "saleFareTotal": "USD468.00",
      "saleTaxTotal": "USD240.60",
      "saleTotal": "USD708.60",
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
        "salePrice": "USD207.00"
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
      "fareCalculation": "SFO TK X/IST TK LON 468.00SLV3PXOW NUC 468.00 END ROE 1.00 FARE USD 468.00 XT 17.80US 5.60AY 5.70TR 207.00YR 4.50XF SFO4.50",
      "latestTicketingTime": "2016-05-11T21:09-04:00",
      "ptc": "ADT",
      "refundable": true
     }
    ]
   },
   {
    "kind": "qpxexpress#tripOption",
    "saleTotal": "USD708.60",
    "id": "6empvn45ipLTmBrLTmNqE1001",
    "slice": [
     {
      "kind": "qpxexpress#sliceInfo",
      "duration": 1115,
      "segment": [
       {
        "kind": "qpxexpress#segmentInfo",
        "duration": 785,
        "flight": {
         "carrier": "TK",
         "number": "80"
        },
        "id": "G7OcLe0KQx2LHVKk",
        "cabin": "COACH",
        "bookingCode": "S",
        "bookingCodeCount": 9,
        "marriedSegmentGroup": "0",
        "leg": [
         {
          "kind": "qpxexpress#legInfo",
          "id": "LKuHk5mT1V3mWnTm",
          "aircraft": "77W",
          "arrivalTime": "2016-05-12T17:15+03:00",
          "departureTime": "2016-05-11T18:10-07:00",
          "origin": "SFO",
          "destination": "IST",
          "originTerminal": "I",
          "destinationTerminal": "I",
          "duration": 785,
          "mileage": 6706,
          "meal": "Meal",
          "secure": true
         }
        ],
        "connectionDuration": 85
       },
       {
        "kind": "qpxexpress#segmentInfo",
        "duration": 245,
        "flight": {
         "carrier": "TK",
         "number": "1983"
        },
        "id": "GR5VOxf0wPb4Gnwu",
        "cabin": "COACH",
        "bookingCode": "S",
        "bookingCodeCount": 9,
        "marriedSegmentGroup": "1",
        "leg": [
         {
          "kind": "qpxexpress#legInfo",
          "id": "LeTGyb21A0O0I5P5",
          "aircraft": "32B",
          "arrivalTime": "2016-05-12T20:45+01:00",
          "departureTime": "2016-05-12T18:40+03:00",
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
        "id": "AE9DkkWrJat7UBwOlw23zyvgu4X0HJKcHRmx1614XNHE",
        "carrier": "TK",
        "origin": "SFO",
        "destination": "LON",
        "basisCode": "SLV3PXOW"
       }
      ],
      "segmentPricing": [
       {
        "kind": "qpxexpress#segmentPricing",
        "fareId": "AE9DkkWrJat7UBwOlw23zyvgu4X0HJKcHRmx1614XNHE",
        "segmentId": "G7OcLe0KQx2LHVKk"
       },
       {
        "kind": "qpxexpress#segmentPricing",
        "fareId": "AE9DkkWrJat7UBwOlw23zyvgu4X0HJKcHRmx1614XNHE",
        "segmentId": "GR5VOxf0wPb4Gnwu"
       }
      ],
      "baseFareTotal": "USD468.00",
      "saleFareTotal": "USD468.00",
      "saleTaxTotal": "USD240.60",
      "saleTotal": "USD708.60",
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
        "salePrice": "USD207.00"
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
      "fareCalculation": "SFO TK X/IST TK LON 468.00SLV3PXOW NUC 468.00 END ROE 1.00 FARE USD 468.00 XT 17.80US 5.60AY 5.70TR 207.00YR 4.50XF SFO4.50",
      "latestTicketingTime": "2016-05-11T21:09-04:00",
      "ptc": "ADT",
      "refundable": true
     }
    ]
   }
  ]
 }
}

JSON RESPONSE STRUCTURE:

{
  "kind": "qpxExpress#tripsSearch",
  "trips": {
    "kind": "qpxexpress#tripOptions",
    "requestId": string,
    "data": {
      "kind": "qpxexpress#data",
      "airport": [
        {
          "kind": "qpxexpress#airportData",
          "code": string,
          "city": string,
          "name": string
        }
      ],
      "city": [
        {
          "kind": "qpxexpress#cityData",
          "code": string,
          "country": string,
          "name": string
        }
      ],
      "aircraft": [
        {
          "kind": "qpxexpress#aircraftData",
          "code": string,
          "name": string
        }
      ],
      "tax": [
        {
          "kind": "qpxexpress#taxData",
          "id": string,
          "name": string
        }
      ],
      "carrier": [
        {
          "kind": "qpxexpress#carrierData",
          "code": string,
          "name": string
        }
      ]
    },
    "tripOption": [
      {
        "kind": "qpxexpress#tripOption",
        "saleTotal": string,
        "id": string,
        "slice": [
          {
            "kind": "qpxexpress#sliceInfo",
            "duration": integer,
            "segment": [
              {
                "kind": "qpxexpress#segmentInfo",
                "duration": integer,
                "flight": {
                  "carrier": string,
                  "number": string
                },
                "id": string,
                "cabin": string,
                "bookingCode": string,
                "bookingCodeCount": integer,
                "marriedSegmentGroup": string,
                "subjectToGovernmentApproval": boolean,
                "leg": [
                  {
                    "kind": "qpxexpress#legInfo",
                    "id": string,
                    "aircraft": string,
                    "arrivalTime": string,
                    "departureTime": string,
                    "origin": string,
                    "destination": string,
                    "originTerminal": string,
                    "destinationTerminal": string,
                    "duration": integer,
                    "operatingDisclosure": string,
                    "onTimePerformance": integer,
                    "mileage": integer,
                    "meal": string,
                    "secure": boolean,
                    "connectionDuration": integer,
                    "changePlane": boolean
                  }
                ],
                "connectionDuration": integer
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
                "id": string,
                "carrier": string,
                "origin": string,
                "destination": string,
                "basisCode": string,
                "private": boolean
              }
            ],
            "segmentPricing": [
              {
                "kind": "qpxexpress#segmentPricing",
                "fareId": string,
                "segmentId": string,
                "freeBaggageOption": [
                  {
                    "kind": "qpxexpress#freeBaggageAllowance",
                    "bagDescriptor": [
                      {
                        "kind": "qpxexpress#bagDescriptor",
                        "commercialName": string,
                        "count": integer,
                        "description": [
                          string
                        ],
                        "subcode": string
                      }
                    ],
                    "kilos": integer,
                    "kilosPerPiece": integer,
                    "pieces": integer,
                    "pounds": integer
                  }
                ]
              }
            ],
            "baseFareTotal": string,
            "saleFareTotal": string,
            "saleTaxTotal": string,
            "saleTotal": string,
            "passengers": {
              "kind": "qpxexpress#passengerCounts",
              "adultCount": integer,
              "childCount": integer,
              "infantInLapCount": integer,
              "infantInSeatCount": integer,
              "seniorCount": integer
            },
            "tax": [
              {
                "kind": "qpxexpress#taxInfo",
                "id": string,
                "chargeType": string,
                "code": string,
                "country": string,
                "salePrice": string
              }
            ],
            "fareCalculation": string,
            "latestTicketingTime": string,
            "ptc": string,
            "refundable": boolean
          }
        ]
      }
    ]
  }
}