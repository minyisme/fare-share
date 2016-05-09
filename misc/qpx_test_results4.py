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
    "maxPrice": "USD2000.00",
  }
}

{
 "kind": "qpxExpress#tripsSearch",
 "trips": {
  "kind": "qpxexpress#tripOptions",
  "requestId": "LrDFru8ZskJuJ5ftD0OIxz",
  "data": {
   "kind": "qpxexpress#data",
   "airport": [
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
     "code": "LHR",
     "city": "LON",
     "name": "London Heathrow"
    },
    {
     "kind": "qpxexpress#airportData",
     "code": "ORD",
     "city": "CHI",
     "name": "Chicago O'Hare"
    },
    {
     "kind": "qpxexpress#airportData",
     "code": "SNN",
     "city": "SNN",
     "name": "Shannon International"
    },
    {
     "kind": "qpxexpress#airportData",
     "code": "WAW",
     "city": "WAW",
     "name": "Warsaw Frederic Chopin"
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
     "code": "SNN",
     "name": "Shannon"
    },
    {
     "kind": "qpxexpress#cityData",
     "code": "WAW",
     "name": "Warsaw"
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
     "code": "734",
     "name": "Boeing 737"
    },
    {
     "kind": "qpxexpress#aircraftData",
     "code": "752",
     "name": "Boeing 757"
    },
    {
     "kind": "qpxexpress#aircraftData",
     "code": "763",
     "name": "Boeing 767"
    },
    {
     "kind": "qpxexpress#aircraftData",
     "code": "772",
     "name": "Boeing 777"
    },
    {
     "kind": "qpxexpress#aircraftData",
     "code": "777",
     "name": "Boeing 777"
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
     "id": "XW_001",
     "name": "Poland Airport Tax"
    },
    {
     "kind": "qpxexpress#taxData",
     "id": "UP_001",
     "name": "Ireland Passenger Charge"
    },
    {
     "kind": "qpxexpress#taxData",
     "id": "TR_001",
     "name": "Turkey Airport Service Charge International"
    },
    {
     "kind": "qpxexpress#taxData",
     "id": "ND",
     "name": "Poland Passenger Service Charge"
    },
    {
     "kind": "qpxexpress#taxData",
     "id": "YQ_F",
     "name": "LO YQ surcharge"
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
     "id": "BC_001",
     "name": "Ireland Airport Security Charge"
    },
    {
     "kind": "qpxexpress#taxData",
     "id": "YR_F",
     "name": "TK YR surcharge"
    },
    {
     "kind": "qpxexpress#taxData",
     "id": "YR_I",
     "name": "AY YR surcharge"
    },
    {
     "kind": "qpxexpress#taxData",
     "id": "YQ_I",
     "name": "IB YQ surcharge"
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
     "code": "AY",
     "name": "Finnair Oyj"
    },
    {
     "kind": "qpxexpress#carrierData",
     "code": "BA",
     "name": "British Airways p.l.c."
    },
    {
     "kind": "qpxexpress#carrierData",
     "code": "EI",
     "name": "Aer Lingus Limited"
    },
    {
     "kind": "qpxexpress#carrierData",
     "code": "IB",
     "name": "Iberia Lineas Aereas de Espana S.A."
    },
    {
     "kind": "qpxexpress#carrierData",
     "code": "LO",
     "name": "LOT - Polish Airlines"
    },
    {
     "kind": "qpxexpress#carrierData",
     "code": "TK",
     "name": "Turkish Airlines Inc."
    },
    {
     "kind": "qpxexpress#carrierData",
     "code": "UA",
     "name": "United Airlines, Inc."
    }
   ]
  },
  "tripOption": [
   {
    "kind": "qpxexpress#tripOption",
    "saleTotal": "USD929.60",
    "id": "fMbiEAHAPe2MJLTR2P97l7003",
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
    "id": "fMbiEAHAPe2MJLTR2P97l7002",
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
   },
   {
    "kind": "qpxexpress#tripOption",
    "saleTotal": "USD1003.00",
    "id": "fMbiEAHAPe2MJLTR2P97l7004",
    "slice": [
     {
      "kind": "qpxexpress#sliceInfo",
      "duration": 1080,
      "segment": [
       {
        "kind": "qpxexpress#segmentInfo",
        "duration": 550,
        "flight": {
         "carrier": "LO",
         "number": "2"
        },
        "id": "G5MxnWVTyzN0UZJK",
        "cabin": "COACH",
        "bookingCode": "M",
        "bookingCodeCount": 9,
        "marriedSegmentGroup": "0",
        "leg": [
         {
          "kind": "qpxexpress#legInfo",
          "id": "LHwJR+-7AnutjdLe",
          "aircraft": "788",
          "arrivalTime": "2016-06-12T09:10+02:00",
          "departureTime": "2016-06-11T17:00-05:00",
          "origin": "ORD",
          "destination": "WAW",
          "originTerminal": "5",
          "duration": 550,
          "mileage": 4670,
          "meal": "Breakfast",
          "secure": true
         }
        ],
        "connectionDuration": 360
       },
       {
        "kind": "qpxexpress#segmentInfo",
        "duration": 170,
        "flight": {
         "carrier": "LO",
         "number": "279"
        },
        "id": "GJzHQw99N7Uhcj3W",
        "cabin": "COACH",
        "bookingCode": "M",
        "bookingCodeCount": 9,
        "marriedSegmentGroup": "1",
        "leg": [
         {
          "kind": "qpxexpress#legInfo",
          "id": "Lr8LjEMqfuFmd2q1",
          "aircraft": "734",
          "arrivalTime": "2016-06-12T17:00+01:00",
          "departureTime": "2016-06-12T15:10+02:00",
          "origin": "WAW",
          "destination": "LHR",
          "destinationTerminal": "2",
          "duration": 170,
          "mileage": 912,
          "meal": "Food for Purchase"
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
        "id": "AoCTSscD3pHok9izMTipe7U7yt4SdSoEHBoK2V4ktdVc",
        "carrier": "LO",
        "origin": "CHI",
        "destination": "LON",
        "basisCode": "M1RED"
       }
      ],
      "segmentPricing": [
       {
        "kind": "qpxexpress#segmentPricing",
        "fareId": "AoCTSscD3pHok9izMTipe7U7yt4SdSoEHBoK2V4ktdVc",
        "segmentId": "GJzHQw99N7Uhcj3W"
       },
       {
        "kind": "qpxexpress#segmentPricing",
        "fareId": "AoCTSscD3pHok9izMTipe7U7yt4SdSoEHBoK2V4ktdVc",
        "segmentId": "G5MxnWVTyzN0UZJK"
       }
      ],
      "baseFareTotal": "USD799.00",
      "saleFareTotal": "USD799.00",
      "saleTaxTotal": "USD204.00",
      "saleTotal": "USD1003.00",
      "passengers": {
       "kind": "qpxexpress#passengerCounts",
       "adultCount": 1
      },
      "tax": [
       {
        "kind": "qpxexpress#taxInfo",
        "id": "XW_001",
        "chargeType": "GOVERNMENT",
        "code": "XW",
        "country": "PL",
        "salePrice": "USD15.60"
       },
       {
        "kind": "qpxexpress#taxInfo",
        "id": "ND",
        "chargeType": "GOVERNMENT",
        "code": "ND",
        "country": "PL",
        "salePrice": "USD0.20"
       },
       {
        "kind": "qpxexpress#taxInfo",
        "id": "YQ_F",
        "chargeType": "CARRIER_SURCHARGE",
        "code": "YQ",
        "salePrice": "USD160.30"
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
      "fareCalculation": "CHI LO X/WAW LO LON 799.00M1RED NUC 799.00 END ROE 1.00 FARE USD 799.00 XT 17.80US 5.60AY 0.20ND 15.60XW 160.30YQ 4.50XF ORD4.50",
      "latestTicketingTime": "2016-05-12T17:23-04:00",
      "ptc": "ADT",
      "refundable": true
     }
    ]
   },
   {
    "kind": "qpxexpress#tripOption",
    "saleTotal": "USD1003.00",
    "id": "fMbiEAHAPe2MJLTR2P97l7006",
    "slice": [
     {
      "kind": "qpxexpress#sliceInfo",
      "duration": 1100,
      "segment": [
       {
        "kind": "qpxexpress#segmentInfo",
        "duration": 540,
        "flight": {
         "carrier": "LO",
         "number": "4"
        },
        "id": "GRYU7nyHMd0XNuU-",
        "cabin": "COACH",
        "bookingCode": "M",
        "bookingCodeCount": 9,
        "marriedSegmentGroup": "0",
        "leg": [
         {
          "kind": "qpxexpress#legInfo",
          "id": "LfPKpqh097ZS9nNQ",
          "aircraft": "788",
          "arrivalTime": "2016-06-12T13:25+02:00",
          "departureTime": "2016-06-11T21:25-05:00",
          "origin": "ORD",
          "destination": "WAW",
          "originTerminal": "5",
          "duration": 540,
          "mileage": 4670,
          "meal": "Breakfast",
          "secure": true
         }
        ],
        "connectionDuration": 395
       },
       {
        "kind": "qpxexpress#segmentInfo",
        "duration": 165,
        "flight": {
         "carrier": "LO",
         "number": "285"
        },
        "id": "GqO+tFXNAJQIxoFg",
        "cabin": "COACH",
        "bookingCode": "M",
        "bookingCodeCount": 9,
        "marriedSegmentGroup": "1",
        "leg": [
         {
          "kind": "qpxexpress#legInfo",
          "id": "Lb+tCJBNQ8E7AlyH",
          "aircraft": "734",
          "arrivalTime": "2016-06-12T21:45+01:00",
          "departureTime": "2016-06-12T20:00+02:00",
          "origin": "WAW",
          "destination": "LHR",
          "destinationTerminal": "2",
          "duration": 165,
          "mileage": 912,
          "meal": "Food for Purchase"
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
        "id": "AoCTSscD3pHok9izMTipe7U7yt4SdSoEHBoK2V4ktdVc",
        "carrier": "LO",
        "origin": "CHI",
        "destination": "LON",
        "basisCode": "M1RED"
       }
      ],
      "segmentPricing": [
       {
        "kind": "qpxexpress#segmentPricing",
        "fareId": "AoCTSscD3pHok9izMTipe7U7yt4SdSoEHBoK2V4ktdVc",
        "segmentId": "GRYU7nyHMd0XNuU-"
       },
       {
        "kind": "qpxexpress#segmentPricing",
        "fareId": "AoCTSscD3pHok9izMTipe7U7yt4SdSoEHBoK2V4ktdVc",
        "segmentId": "GqO+tFXNAJQIxoFg"
       }
      ],
      "baseFareTotal": "USD799.00",
      "saleFareTotal": "USD799.00",
      "saleTaxTotal": "USD204.00",
      "saleTotal": "USD1003.00",
      "passengers": {
       "kind": "qpxexpress#passengerCounts",
       "adultCount": 1
      },
      "tax": [
       {
        "kind": "qpxexpress#taxInfo",
        "id": "XW_001",
        "chargeType": "GOVERNMENT",
        "code": "XW",
        "country": "PL",
        "salePrice": "USD15.60"
       },
       {
        "kind": "qpxexpress#taxInfo",
        "id": "ND",
        "chargeType": "GOVERNMENT",
        "code": "ND",
        "country": "PL",
        "salePrice": "USD0.20"
       },
       {
        "kind": "qpxexpress#taxInfo",
        "id": "YQ_F",
        "chargeType": "CARRIER_SURCHARGE",
        "code": "YQ",
        "salePrice": "USD160.30"
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
      "fareCalculation": "CHI LO X/WAW LO LON 799.00M1RED NUC 799.00 END ROE 1.00 FARE USD 799.00 XT 17.80US 5.60AY 0.20ND 15.60XW 160.30YQ 4.50XF ORD4.50",
      "latestTicketingTime": "2016-05-12T17:23-04:00",
      "ptc": "ADT",
      "refundable": true
     }
    ]
   },
   {
    "kind": "qpxexpress#tripOption",
    "saleTotal": "USD1003.00",
    "id": "fMbiEAHAPe2MJLTR2P97l7001",
    "slice": [
     {
      "kind": "qpxexpress#sliceInfo",
      "duration": 815,
      "segment": [
       {
        "kind": "qpxexpress#segmentInfo",
        "duration": 540,
        "flight": {
         "carrier": "LO",
         "number": "4"
        },
        "id": "GRYU7nyHMd0XNuU-",
        "cabin": "COACH",
        "bookingCode": "M",
        "bookingCodeCount": 9,
        "marriedSegmentGroup": "0",
        "leg": [
         {
          "kind": "qpxexpress#legInfo",
          "id": "LfPKpqh097ZS9nNQ",
          "aircraft": "788",
          "arrivalTime": "2016-06-12T13:25+02:00",
          "departureTime": "2016-06-11T21:25-05:00",
          "origin": "ORD",
          "destination": "WAW",
          "originTerminal": "5",
          "duration": 540,
          "mileage": 4670,
          "meal": "Breakfast",
          "secure": true
         }
        ],
        "connectionDuration": 105
       },
       {
        "kind": "qpxexpress#segmentInfo",
        "duration": 170,
        "flight": {
         "carrier": "LO",
         "number": "279"
        },
        "id": "GJzHQw99N7Uhcj3W",
        "cabin": "COACH",
        "bookingCode": "M",
        "bookingCodeCount": 9,
        "marriedSegmentGroup": "0",
        "leg": [
         {
          "kind": "qpxexpress#legInfo",
          "id": "Lr8LjEMqfuFmd2q1",
          "aircraft": "734",
          "arrivalTime": "2016-06-12T17:00+01:00",
          "departureTime": "2016-06-12T15:10+02:00",
          "origin": "WAW",
          "destination": "LHR",
          "destinationTerminal": "2",
          "duration": 170,
          "mileage": 912,
          "meal": "Food for Purchase"
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
        "id": "AoCTSscD3pHok9izMTipe7U7yt4SdSoEHBoK2V4ktdVc",
        "carrier": "LO",
        "origin": "CHI",
        "destination": "LON",
        "basisCode": "M1RED"
       }
      ],
      "segmentPricing": [
       {
        "kind": "qpxexpress#segmentPricing",
        "fareId": "AoCTSscD3pHok9izMTipe7U7yt4SdSoEHBoK2V4ktdVc",
        "segmentId": "GJzHQw99N7Uhcj3W"
       },
       {
        "kind": "qpxexpress#segmentPricing",
        "fareId": "AoCTSscD3pHok9izMTipe7U7yt4SdSoEHBoK2V4ktdVc",
        "segmentId": "GRYU7nyHMd0XNuU-"
       }
      ],
      "baseFareTotal": "USD799.00",
      "saleFareTotal": "USD799.00",
      "saleTaxTotal": "USD204.00",
      "saleTotal": "USD1003.00",
      "passengers": {
       "kind": "qpxexpress#passengerCounts",
       "adultCount": 1
      },
      "tax": [
       {
        "kind": "qpxexpress#taxInfo",
        "id": "XW_001",
        "chargeType": "GOVERNMENT",
        "code": "XW",
        "country": "PL",
        "salePrice": "USD15.60"
       },
       {
        "kind": "qpxexpress#taxInfo",
        "id": "ND",
        "chargeType": "GOVERNMENT",
        "code": "ND",
        "country": "PL",
        "salePrice": "USD0.20"
       },
       {
        "kind": "qpxexpress#taxInfo",
        "id": "YQ_F",
        "chargeType": "CARRIER_SURCHARGE",
        "code": "YQ",
        "salePrice": "USD160.30"
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
      "fareCalculation": "CHI LO X/WAW LO LON 799.00M1RED NUC 799.00 END ROE 1.00 FARE USD 799.00 XT 17.80US 5.60AY 0.20ND 15.60XW 160.30YQ 4.50XF ORD4.50",
      "latestTicketingTime": "2016-05-12T17:23-04:00",
      "ptc": "ADT",
      "refundable": true
     }
    ]
   },
   {
    "kind": "qpxexpress#tripOption",
    "saleTotal": "USD1202.27",
    "id": "fMbiEAHAPe2MJLTR2P97l7005",
    "slice": [
     {
      "kind": "qpxexpress#sliceInfo",
      "duration": 615,
      "segment": [
       {
        "kind": "qpxexpress#segmentInfo",
        "duration": 445,
        "flight": {
         "carrier": "EI",
         "number": "122"
        },
        "id": "G27nVJXZ+GPIgdxI",
        "cabin": "COACH",
        "bookingCode": "B",
        "bookingCodeCount": 4,
        "marriedSegmentGroup": "0",
        "leg": [
         {
          "kind": "qpxexpress#legInfo",
          "id": "LWRFe8BuLzrpO2Vf",
          "aircraft": "330",
          "arrivalTime": "2016-06-12T05:15+01:00",
          "departureTime": "2016-06-11T15:50-05:00",
          "origin": "ORD",
          "destination": "DUB",
          "originTerminal": "5",
          "destinationTerminal": "2",
          "duration": 445,
          "mileage": 3661,
          "meal": "Meal",
          "secure": true
         }
        ],
        "connectionDuration": 85
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
        "id": "A8hnKAuzpTVkqzh5BLjEjMdt3bhQmSIB5qtXtEvRHmtg",
        "carrier": "EI",
        "origin": "CHI",
        "destination": "DUB",
        "basisCode": "BK1NS"
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
        "fareId": "A8hnKAuzpTVkqzh5BLjEjMdt3bhQmSIB5qtXtEvRHmtg",
        "segmentId": "G27nVJXZ+GPIgdxI"
       },
       {
        "kind": "qpxexpress#segmentPricing",
        "fareId": "AWnu1IgD58t41Jl+t2piVpe0G0R1+8MUpHcXW1z8RX3/",
        "segmentId": "Gk8zIF+il1s3RK-k"
       }
      ],
      "baseFareTotal": "USD1133.00",
      "saleFareTotal": "USD1133.00",
      "saleTaxTotal": "USD69.27",
      "saleTotal": "USD1202.27",
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
      "fareCalculation": "CHI EI X/DUB Q110.00 916.00BK1NS EI LHR 107.30FOW26GDS NUC 1133.30 END ROE 1.00 FARE USD 1133.00 XT 17.80US 5.60AY 13.10UP 28.27YQ 4.50XF ORD4.50",
      "latestTicketingTime": "2016-05-10T17:23-04:00",
      "ptc": "ADT"
     }
    ]
   },
   {
    "kind": "qpxexpress#tripOption",
    "saleTotal": "USD1208.57",
    "id": "fMbiEAHAPe2MJLTR2P97l700E",
    "slice": [
     {
      "kind": "qpxexpress#sliceInfo",
      "duration": 890,
      "segment": [
       {
        "kind": "qpxexpress#segmentInfo",
        "duration": 445,
        "flight": {
         "carrier": "EI",
         "number": "122"
        },
        "id": "G27nVJXZ+GPIgdxI",
        "cabin": "COACH",
        "bookingCode": "B",
        "bookingCodeCount": 4,
        "marriedSegmentGroup": "0",
        "leg": [
         {
          "kind": "qpxexpress#legInfo",
          "id": "LWRFe8BuLzrpO2Vf",
          "aircraft": "330",
          "arrivalTime": "2016-06-12T05:15+01:00",
          "departureTime": "2016-06-11T15:50-05:00",
          "origin": "ORD",
          "destination": "DUB",
          "originTerminal": "5",
          "destinationTerminal": "2",
          "duration": 445,
          "mileage": 3661,
          "meal": "Meal",
          "secure": true
         }
        ],
        "connectionDuration": 360
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
        "id": "A8hnKAuzpTVkqzh5BLjEjMdt3bhQmSIB5qtXtEvRHmtg",
        "carrier": "EI",
        "origin": "CHI",
        "destination": "DUB",
        "basisCode": "BK1NS"
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
        "fareId": "A8hnKAuzpTVkqzh5BLjEjMdt3bhQmSIB5qtXtEvRHmtg",
        "segmentId": "G27nVJXZ+GPIgdxI"
       },
       {
        "kind": "qpxexpress#segmentPricing",
        "fareId": "AWnu1IgD58t41Jl+t2piVpe0G0R1+8MUpHcXW1z8RX3/",
        "segmentId": "GQd8ROKIvrR-A1Cl"
       }
      ],
      "baseFareTotal": "USD1133.00",
      "saleFareTotal": "USD1133.00",
      "saleTaxTotal": "USD75.57",
      "saleTotal": "USD1208.57",
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
      "fareCalculation": "CHI EI X/DUB Q110.00 916.00BK1NS EI LHR 107.30FOW26GDS NUC 1133.30 END ROE 1.00 FARE USD 1133.00 XT 17.80US 5.60AY 19.40UP 28.27YQ 4.50XF ORD4.50",
      "latestTicketingTime": "2016-05-10T17:23-04:00",
      "ptc": "ADT"
     }
    ]
   },
   {
    "kind": "qpxexpress#tripOption",
    "saleTotal": "USD1213.27",
    "id": "fMbiEAHAPe2MJLTR2P97l700A",
    "slice": [
     {
      "kind": "qpxexpress#sliceInfo",
      "duration": 785,
      "segment": [
       {
        "kind": "qpxexpress#segmentInfo",
        "duration": 445,
        "flight": {
         "carrier": "EI",
         "number": "122"
        },
        "id": "G27nVJXZ+GPIgdxI",
        "cabin": "COACH",
        "bookingCode": "B",
        "bookingCodeCount": 4,
        "marriedSegmentGroup": "0",
        "leg": [
         {
          "kind": "qpxexpress#legInfo",
          "id": "LWRFe8BuLzrpO2Vf",
          "aircraft": "330",
          "arrivalTime": "2016-06-12T05:15+01:00",
          "departureTime": "2016-06-11T15:50-05:00",
          "origin": "ORD",
          "destination": "DUB",
          "originTerminal": "5",
          "destinationTerminal": "2",
          "duration": 445,
          "mileage": 3661,
          "meal": "Meal",
          "secure": true
         }
        ],
        "connectionDuration": 250
       },
       {
        "kind": "qpxexpress#segmentInfo",
        "duration": 90,
        "flight": {
         "carrier": "EI",
         "number": "8333"
        },
        "id": "Gm5cRgqkMpUhtyLR",
        "cabin": "COACH",
        "bookingCode": "V",
        "bookingCodeCount": 4,
        "marriedSegmentGroup": "1",
        "leg": [
         {
          "kind": "qpxexpress#legInfo",
          "id": "Lhd+bMFzzFTSIuwS",
          "aircraft": "319",
          "arrivalTime": "2016-06-12T10:55+01:00",
          "departureTime": "2016-06-12T09:25+01:00",
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
        "id": "A8hnKAuzpTVkqzh5BLjEjMdt3bhQmSIB5qtXtEvRHmtg",
        "carrier": "EI",
        "origin": "CHI",
        "destination": "DUB",
        "basisCode": "BK1NS"
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
        "segmentId": "Gm5cRgqkMpUhtyLR"
       },
       {
        "kind": "qpxexpress#segmentPricing",
        "fareId": "A8hnKAuzpTVkqzh5BLjEjMdt3bhQmSIB5qtXtEvRHmtg",
        "segmentId": "G27nVJXZ+GPIgdxI"
       }
      ],
      "baseFareTotal": "USD1144.00",
      "saleFareTotal": "USD1144.00",
      "saleTaxTotal": "USD69.27",
      "saleTotal": "USD1213.27",
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
      "fareCalculation": "CHI EI X/DUB Q110.00 916.00BK1NS EI LHR 118.25VOW26GDS NUC 1144.25 END ROE 1.00 FARE USD 1144.00 XT 17.80US 5.60AY 13.10UP 28.27YQ 4.50XF ORD4.50",
      "latestTicketingTime": "2016-05-10T17:23-04:00",
      "ptc": "ADT"
     }
    ]
   },
   {
    "kind": "qpxexpress#tripOption",
    "saleTotal": "USD1227.27",
    "id": "fMbiEAHAPe2MJLTR2P97l7008",
    "slice": [
     {
      "kind": "qpxexpress#sliceInfo",
      "duration": 675,
      "segment": [
       {
        "kind": "qpxexpress#segmentInfo",
        "duration": 445,
        "flight": {
         "carrier": "EI",
         "number": "122"
        },
        "id": "G27nVJXZ+GPIgdxI",
        "cabin": "COACH",
        "bookingCode": "B",
        "bookingCodeCount": 4,
        "marriedSegmentGroup": "0",
        "leg": [
         {
          "kind": "qpxexpress#legInfo",
          "id": "LWRFe8BuLzrpO2Vf",
          "aircraft": "330",
          "arrivalTime": "2016-06-12T05:15+01:00",
          "departureTime": "2016-06-11T15:50-05:00",
          "origin": "ORD",
          "destination": "DUB",
          "originTerminal": "5",
          "destinationTerminal": "2",
          "duration": 445,
          "mileage": 3661,
          "meal": "Meal",
          "secure": true
         }
        ],
        "connectionDuration": 145
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
        "id": "A8hnKAuzpTVkqzh5BLjEjMdt3bhQmSIB5qtXtEvRHmtg",
        "carrier": "EI",
        "origin": "CHI",
        "destination": "DUB",
        "basisCode": "BK1NS"
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
        "fareId": "A8hnKAuzpTVkqzh5BLjEjMdt3bhQmSIB5qtXtEvRHmtg",
        "segmentId": "G27nVJXZ+GPIgdxI"
       }
      ],
      "baseFareTotal": "USD1158.00",
      "saleFareTotal": "USD1158.00",
      "saleTaxTotal": "USD69.27",
      "saleTotal": "USD1227.27",
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
      "fareCalculation": "CHI EI X/DUB Q110.00 916.00BK1NS EI LHR 132.49MOW26GDS NUC 1158.49 END ROE 1.00 FARE USD 1158.00 XT 17.80US 5.60AY 13.10UP 28.27YQ 4.50XF ORD4.50",
      "latestTicketingTime": "2016-05-10T17:23-04:00",
      "ptc": "ADT"
     }
    ]
   },
   {
    "kind": "qpxexpress#tripOption",
    "saleTotal": "USD1233.47",
    "id": "fMbiEAHAPe2MJLTR2P97l7007",
    "slice": [
     {
      "kind": "qpxexpress#sliceInfo",
      "duration": 615,
      "segment": [
       {
        "kind": "qpxexpress#segmentInfo",
        "duration": 440,
        "flight": {
         "carrier": "EI",
         "number": "6996"
        },
        "id": "G-jssjfxPTpiynEE",
        "cabin": "COACH",
        "bookingCode": "G",
        "bookingCodeCount": 4,
        "marriedSegmentGroup": "0",
        "leg": [
         {
          "kind": "qpxexpress#legInfo",
          "id": "L1e7i4NsdiMXlGkp",
          "aircraft": "752",
          "arrivalTime": "2016-06-12T07:20+01:00",
          "departureTime": "2016-06-11T18:00-05:00",
          "origin": "ORD",
          "destination": "SNN",
          "originTerminal": "5",
          "duration": 440,
          "operatingDisclosure": "OPERATED BY UNITED AIRLINES",
          "mileage": 3578,
          "secure": true
         }
        ],
        "connectionDuration": 85
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
        "bookingCode": "N",
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
        "id": "A+7w2zfTI8vzPcQ9XOmp56xei6l34s8SUX0J6Nxe8PKE",
        "carrier": "EI",
        "origin": "CHI",
        "destination": "SNN",
        "basisCode": "GK1OUS"
       },
       {
        "kind": "qpxexpress#fareInfo",
        "id": "AmxqTNziPk8jJO0Sf9nVRDZUHz6M7hjDkEG68x5rm3Yg",
        "carrier": "EI",
        "origin": "SNN",
        "destination": "LON",
        "basisCode": "NOW26GDS"
       }
      ],
      "segmentPricing": [
       {
        "kind": "qpxexpress#segmentPricing",
        "fareId": "AmxqTNziPk8jJO0Sf9nVRDZUHz6M7hjDkEG68x5rm3Yg",
        "segmentId": "GDEjm2MlRD3j3mC-"
       },
       {
        "kind": "qpxexpress#segmentPricing",
        "fareId": "A+7w2zfTI8vzPcQ9XOmp56xei6l34s8SUX0J6Nxe8PKE",
        "segmentId": "G-jssjfxPTpiynEE"
       }
      ],
      "baseFareTotal": "USD1182.00",
      "saleFareTotal": "USD1182.00",
      "saleTaxTotal": "USD51.47",
      "saleTotal": "USD1233.47",
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
      "fareCalculation": "CHI EI X/SNN Q120.00 966.00GK1OUS EI LHR 96.35NOW26GDS NUC 1182.35 END ROE 1.00 FARE USD 1182.00 XT 17.80US 5.60AY 0.90UP 22.67YQ 4.50XF ORD4.50",
      "latestTicketingTime": "2016-05-10T17:23-04:00",
      "ptc": "ADT"
     }
    ]
   },
   {
    "kind": "qpxexpress#tripOption",
    "saleTotal": "USD1238.27",
    "id": "fMbiEAHAPe2MJLTR2P97l7009",
    "slice": [
     {
      "kind": "qpxexpress#sliceInfo",
      "duration": 680,
      "segment": [
       {
        "kind": "qpxexpress#segmentInfo",
        "duration": 445,
        "flight": {
         "carrier": "EI",
         "number": "122"
        },
        "id": "G27nVJXZ+GPIgdxI",
        "cabin": "COACH",
        "bookingCode": "B",
        "bookingCodeCount": 4,
        "marriedSegmentGroup": "0",
        "leg": [
         {
          "kind": "qpxexpress#legInfo",
          "id": "LWRFe8BuLzrpO2Vf",
          "aircraft": "330",
          "arrivalTime": "2016-06-12T05:15+01:00",
          "departureTime": "2016-06-11T15:50-05:00",
          "origin": "ORD",
          "destination": "DUB",
          "originTerminal": "5",
          "destinationTerminal": "2",
          "duration": 445,
          "mileage": 3661,
          "meal": "Meal",
          "secure": true
         }
        ],
        "connectionDuration": 145
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
        "id": "A8hnKAuzpTVkqzh5BLjEjMdt3bhQmSIB5qtXtEvRHmtg",
        "carrier": "EI",
        "origin": "CHI",
        "destination": "DUB",
        "basisCode": "BK1NS"
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
        "fareId": "A8hnKAuzpTVkqzh5BLjEjMdt3bhQmSIB5qtXtEvRHmtg",
        "segmentId": "G27nVJXZ+GPIgdxI"
       },
       {
        "kind": "qpxexpress#segmentPricing",
        "fareId": "ArEnjf/RXEYdLg+cee/ZxXOaa/nvzTSFDuC1DSqIbkZs",
        "segmentId": "GjhLpoyQWOJc24QG"
       }
      ],
      "baseFareTotal": "USD1169.00",
      "saleFareTotal": "USD1169.00",
      "saleTaxTotal": "USD69.27",
      "saleTotal": "USD1238.27",
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
      "fareCalculation": "CHI EI X/DUB Q110.00 916.00BK1NS EI LHR 143.44KOW26GDS NUC 1169.44 END ROE 1.00 FARE USD 1169.00 XT 17.80US 5.60AY 13.10UP 28.27YQ 4.50XF ORD4.50",
      "latestTicketingTime": "2016-05-10T17:23-04:00",
      "ptc": "ADT"
     }
    ]
   },
   {
    "kind": "qpxexpress#tripOption",
    "saleTotal": "USD1385.77",
    "id": "fMbiEAHAPe2MJLTR2P97l700F",
    "slice": [
     {
      "kind": "qpxexpress#sliceInfo",
      "duration": 875,
      "segment": [
       {
        "kind": "qpxexpress#segmentInfo",
        "duration": 440,
        "flight": {
         "carrier": "EI",
         "number": "6996"
        },
        "id": "G-jssjfxPTpiynEE",
        "cabin": "COACH",
        "bookingCode": "G",
        "bookingCodeCount": 4,
        "marriedSegmentGroup": "0",
        "leg": [
         {
          "kind": "qpxexpress#legInfo",
          "id": "L1e7i4NsdiMXlGkp",
          "aircraft": "752",
          "arrivalTime": "2016-06-12T07:20+01:00",
          "departureTime": "2016-06-11T18:00-05:00",
          "origin": "ORD",
          "destination": "SNN",
          "originTerminal": "5",
          "duration": 440,
          "operatingDisclosure": "OPERATED BY UNITED AIRLINES",
          "mileage": 3578,
          "secure": true
         }
        ],
        "connectionDuration": 350
       },
       {
        "kind": "qpxexpress#segmentInfo",
        "duration": 85,
        "flight": {
         "carrier": "EI",
         "number": "384"
        },
        "id": "G3dpk-xUarXXl5Q7",
        "cabin": "COACH",
        "bookingCode": "P",
        "bookingCodeCount": 4,
        "marriedSegmentGroup": "1",
        "leg": [
         {
          "kind": "qpxexpress#legInfo",
          "id": "LwkaKqKZA2csHENC",
          "aircraft": "319",
          "arrivalTime": "2016-06-12T14:35+01:00",
          "departureTime": "2016-06-12T13:10+01:00",
          "origin": "SNN",
          "destination": "LHR",
          "destinationTerminal": "2",
          "duration": 85,
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
        "id": "A+7w2zfTI8vzPcQ9XOmp56xei6l34s8SUX0J6Nxe8PKE",
        "carrier": "EI",
        "origin": "CHI",
        "destination": "SNN",
        "basisCode": "GK1OUS"
       },
       {
        "kind": "qpxexpress#fareInfo",
        "id": "AHXBzDuNDWQkRsAq8rWCjxbskuHYCxo2WCx6AFjx8HZM",
        "carrier": "EI",
        "origin": "SNN",
        "destination": "LON",
        "basisCode": "POW26GDS"
       }
      ],
      "segmentPricing": [
       {
        "kind": "qpxexpress#segmentPricing",
        "fareId": "AHXBzDuNDWQkRsAq8rWCjxbskuHYCxo2WCx6AFjx8HZM",
        "segmentId": "G3dpk-xUarXXl5Q7"
       },
       {
        "kind": "qpxexpress#segmentPricing",
        "fareId": "A+7w2zfTI8vzPcQ9XOmp56xei6l34s8SUX0J6Nxe8PKE",
        "segmentId": "G-jssjfxPTpiynEE"
       }
      ],
      "baseFareTotal": "USD1328.00",
      "saleFareTotal": "USD1328.00",
      "saleTaxTotal": "USD57.77",
      "saleTotal": "USD1385.77",
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
        "id": "BC_001",
        "chargeType": "GOVERNMENT",
        "code": "BC",
        "country": "IE",
        "salePrice": "USD6.30"
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
      "fareCalculation": "CHI EI X/SNN Q120.00 966.00GK1OUS EI LHR 241.99POW26GDS NUC 1327.99 END ROE 1.00 FARE USD 1328.00 XT 17.80US 5.60AY 6.30BC 0.90UP 22.67YQ 4.50XF ORD4.50",
      "latestTicketingTime": "2016-05-10T17:23-04:00",
      "ptc": "ADT"
     }
    ]
   },
   {
    "kind": "qpxexpress#tripOption",
    "saleTotal": "USD1813.90",
    "id": "fMbiEAHAPe2MJLTR2P97l700I",
    "slice": [
     {
      "kind": "qpxexpress#sliceInfo",
      "duration": 465,
      "segment": [
       {
        "kind": "qpxexpress#segmentInfo",
        "duration": 465,
        "flight": {
         "carrier": "AY",
         "number": "5788"
        },
        "id": "Gvivhd5OmxJ1Mazo",
        "cabin": "COACH",
        "bookingCode": "H",
        "bookingCodeCount": 9,
        "marriedSegmentGroup": "0",
        "leg": [
         {
          "kind": "qpxexpress#legInfo",
          "id": "L-pUiYlgjEJQsLmC",
          "aircraft": "788",
          "arrivalTime": "2016-06-12T09:05+01:00",
          "departureTime": "2016-06-11T19:20-05:00",
          "origin": "ORD",
          "destination": "LHR",
          "originTerminal": "3",
          "destinationTerminal": "3",
          "duration": 465,
          "operatingDisclosure": "OPERATED BY AMERICAN AIRLINES INC.",
          "mileage": 3939,
          "meal": "Breakfast",
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
        "id": "Aud2Y3nloFDJoOWAXksLyogPIPNGRSVwK9VGfAMNrbKE",
        "carrier": "AY",
        "origin": "CHI",
        "destination": "LON",
        "basisCode": "H1N0O1C5"
       }
      ],
      "segmentPricing": [
       {
        "kind": "qpxexpress#segmentPricing",
        "fareId": "Aud2Y3nloFDJoOWAXksLyogPIPNGRSVwK9VGfAMNrbKE",
        "segmentId": "Gvivhd5OmxJ1Mazo"
       }
      ],
      "baseFareTotal": "USD1557.00",
      "saleFareTotal": "USD1557.00",
      "saleTaxTotal": "USD256.90",
      "saleTotal": "USD1813.90",
      "passengers": {
       "kind": "qpxexpress#passengerCounts",
       "adultCount": 1
      },
      "tax": [
       {
        "kind": "qpxexpress#taxInfo",
        "id": "YR_I",
        "chargeType": "CARRIER_SURCHARGE",
        "code": "YR",
        "salePrice": "USD229.00"
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
      "fareCalculation": "CHI AY LON M 1557.00H1N0O1C5 NUC 1557.00 END ROE 1.00 FARE USD 1557.00 XT 17.80US 5.60AY 229.00YR 4.50XF ORD4.50",
      "latestTicketingTime": "2016-05-12T23:59-04:00",
      "ptc": "ADT",
      "refundable": true
     }
    ]
   },
   {
    "kind": "qpxexpress#tripOption",
    "saleTotal": "USD1813.90",
    "id": "fMbiEAHAPe2MJLTR2P97l700G",
    "slice": [
     {
      "kind": "qpxexpress#sliceInfo",
      "duration": 460,
      "segment": [
       {
        "kind": "qpxexpress#segmentInfo",
        "duration": 460,
        "flight": {
         "carrier": "AY",
         "number": "5748"
        },
        "id": "GCAoXJBM2zIrJCen",
        "cabin": "COACH",
        "bookingCode": "H",
        "bookingCodeCount": 9,
        "marriedSegmentGroup": "0",
        "leg": [
         {
          "kind": "qpxexpress#legInfo",
          "id": "L5BZ-I8-uINMCRXL",
          "aircraft": "772",
          "arrivalTime": "2016-06-12T12:05+01:00",
          "departureTime": "2016-06-11T22:25-05:00",
          "origin": "ORD",
          "destination": "LHR",
          "originTerminal": "3",
          "destinationTerminal": "3",
          "duration": 460,
          "operatingDisclosure": "OPERATED BY AMERICAN AIRLINES INC.",
          "mileage": 3939,
          "meal": "Breakfast",
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
        "id": "Aud2Y3nloFDJoOWAXksLyogPIPNGRSVwK9VGfAMNrbKE",
        "carrier": "AY",
        "origin": "CHI",
        "destination": "LON",
        "basisCode": "H1N0O1C5"
       }
      ],
      "segmentPricing": [
       {
        "kind": "qpxexpress#segmentPricing",
        "fareId": "Aud2Y3nloFDJoOWAXksLyogPIPNGRSVwK9VGfAMNrbKE",
        "segmentId": "GCAoXJBM2zIrJCen"
       }
      ],
      "baseFareTotal": "USD1557.00",
      "saleFareTotal": "USD1557.00",
      "saleTaxTotal": "USD256.90",
      "saleTotal": "USD1813.90",
      "passengers": {
       "kind": "qpxexpress#passengerCounts",
       "adultCount": 1
      },
      "tax": [
       {
        "kind": "qpxexpress#taxInfo",
        "id": "YR_I",
        "chargeType": "CARRIER_SURCHARGE",
        "code": "YR",
        "salePrice": "USD229.00"
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
      "fareCalculation": "CHI AY LON M 1557.00H1N0O1C5 NUC 1557.00 END ROE 1.00 FARE USD 1557.00 XT 17.80US 5.60AY 229.00YR 4.50XF ORD4.50",
      "latestTicketingTime": "2016-05-12T23:59-04:00",
      "ptc": "ADT",
      "refundable": true
     }
    ]
   },
   {
    "kind": "qpxexpress#tripOption",
    "saleTotal": "USD1813.90",
    "id": "fMbiEAHAPe2MJLTR2P97l700B",
    "slice": [
     {
      "kind": "qpxexpress#sliceInfo",
      "duration": 475,
      "segment": [
       {
        "kind": "qpxexpress#segmentInfo",
        "duration": 475,
        "flight": {
         "carrier": "AY",
         "number": "5752"
        },
        "id": "Gef3ddO3flBnKmP8",
        "cabin": "COACH",
        "bookingCode": "H",
        "bookingCodeCount": 9,
        "marriedSegmentGroup": "0",
        "leg": [
         {
          "kind": "qpxexpress#legInfo",
          "id": "L63jEsv47gGTsu5F",
          "aircraft": "763",
          "arrivalTime": "2016-06-11T22:45+01:00",
          "departureTime": "2016-06-11T08:50-05:00",
          "origin": "ORD",
          "destination": "LHR",
          "originTerminal": "3",
          "destinationTerminal": "3",
          "duration": 475,
          "operatingDisclosure": "OPERATED BY AMERICAN AIRLINES INC.",
          "mileage": 3939,
          "meal": "Breakfast",
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
        "id": "Aud2Y3nloFDJoOWAXksLyogPIPNGRSVwK9VGfAMNrbKE",
        "carrier": "AY",
        "origin": "CHI",
        "destination": "LON",
        "basisCode": "H1N0O1C5"
       }
      ],
      "segmentPricing": [
       {
        "kind": "qpxexpress#segmentPricing",
        "fareId": "Aud2Y3nloFDJoOWAXksLyogPIPNGRSVwK9VGfAMNrbKE",
        "segmentId": "Gef3ddO3flBnKmP8"
       }
      ],
      "baseFareTotal": "USD1557.00",
      "saleFareTotal": "USD1557.00",
      "saleTaxTotal": "USD256.90",
      "saleTotal": "USD1813.90",
      "passengers": {
       "kind": "qpxexpress#passengerCounts",
       "adultCount": 1
      },
      "tax": [
       {
        "kind": "qpxexpress#taxInfo",
        "id": "YR_I",
        "chargeType": "CARRIER_SURCHARGE",
        "code": "YR",
        "salePrice": "USD229.00"
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
      "fareCalculation": "CHI AY LON M 1557.00H1N0O1C5 NUC 1557.00 END ROE 1.00 FARE USD 1557.00 XT 17.80US 5.60AY 229.00YR 4.50XF ORD4.50",
      "latestTicketingTime": "2016-05-12T23:59-04:00",
      "ptc": "ADT",
      "refundable": true
     }
    ]
   },
   {
    "kind": "qpxexpress#tripOption",
    "saleTotal": "USD1813.90",
    "id": "fMbiEAHAPe2MJLTR2P97l700J",
    "slice": [
     {
      "kind": "qpxexpress#sliceInfo",
      "duration": 465,
      "segment": [
       {
        "kind": "qpxexpress#segmentInfo",
        "duration": 465,
        "flight": {
         "carrier": "IB",
         "number": "4188"
        },
        "id": "G2-nCbu2TT0VpG1L",
        "cabin": "COACH",
        "bookingCode": "H",
        "bookingCodeCount": 9,
        "marriedSegmentGroup": "0",
        "leg": [
         {
          "kind": "qpxexpress#legInfo",
          "id": "LmwdIX5Gr+tS0eTB",
          "aircraft": "777",
          "arrivalTime": "2016-06-12T09:05+01:00",
          "departureTime": "2016-06-11T19:20-05:00",
          "origin": "ORD",
          "destination": "LHR",
          "originTerminal": "3",
          "destinationTerminal": "3",
          "duration": 465,
          "operatingDisclosure": "OPERATED BY AMERICAN AIRLINES INC.",
          "mileage": 3939,
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
        "id": "Aefu7R4/poP2CUXxdbOPUPWom/1u8VTBRbqut4mz+NAY",
        "carrier": "IB",
        "origin": "CHI",
        "destination": "LON",
        "basisCode": "H1N0O1C5"
       }
      ],
      "segmentPricing": [
       {
        "kind": "qpxexpress#segmentPricing",
        "fareId": "Aefu7R4/poP2CUXxdbOPUPWom/1u8VTBRbqut4mz+NAY",
        "segmentId": "G2-nCbu2TT0VpG1L"
       }
      ],
      "baseFareTotal": "USD1557.00",
      "saleFareTotal": "USD1557.00",
      "saleTaxTotal": "USD256.90",
      "saleTotal": "USD1813.90",
      "passengers": {
       "kind": "qpxexpress#passengerCounts",
       "adultCount": 1
      },
      "tax": [
       {
        "kind": "qpxexpress#taxInfo",
        "id": "YQ_I",
        "chargeType": "CARRIER_SURCHARGE",
        "code": "YQ",
        "salePrice": "USD229.00"
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
      "fareCalculation": "CHI IB LON M 1557.00H1N0O1C5 NUC 1557.00 END ROE 1.00 FARE USD 1557.00 XT 17.80US 5.60AY 229.00YQ 4.50XF ORD4.50",
      "latestTicketingTime": "2016-05-12T23:59-04:00",
      "ptc": "ADT",
      "refundable": true
     }
    ]
   },
   {
    "kind": "qpxexpress#tripOption",
    "saleTotal": "USD1813.90",
    "id": "fMbiEAHAPe2MJLTR2P97l700K",
    "slice": [
     {
      "kind": "qpxexpress#sliceInfo",
      "duration": 480,
      "segment": [
       {
        "kind": "qpxexpress#segmentInfo",
        "duration": 480,
        "flight": {
         "carrier": "UA",
         "number": "958"
        },
        "id": "GIb3p-+Hbm5cNWgz",
        "cabin": "COACH",
        "bookingCode": "H",
        "bookingCodeCount": 9,
        "marriedSegmentGroup": "0",
        "leg": [
         {
          "kind": "qpxexpress#legInfo",
          "id": "LZoW4KsriN0XP0G8",
          "aircraft": "763",
          "arrivalTime": "2016-06-12T05:55+01:00",
          "departureTime": "2016-06-11T15:55-05:00",
          "origin": "ORD",
          "destination": "LHR",
          "originTerminal": "1",
          "destinationTerminal": "2",
          "duration": 480,
          "mileage": 3939,
          "meal": "Dinner",
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
        "id": "A+bg6O5W7szddViI4MMa0/5986Ix1v0TB8Gx+4ZI",
        "carrier": "UA",
        "origin": "CHI",
        "destination": "LON",
        "basisCode": "H4E"
       }
      ],
      "segmentPricing": [
       {
        "kind": "qpxexpress#segmentPricing",
        "fareId": "A+bg6O5W7szddViI4MMa0/5986Ix1v0TB8Gx+4ZI",
        "segmentId": "GIb3p-+Hbm5cNWgz"
       }
      ],
      "baseFareTotal": "USD1557.00",
      "saleFareTotal": "USD1557.00",
      "saleTaxTotal": "USD256.90",
      "saleTotal": "USD1813.90",
      "passengers": {
       "kind": "qpxexpress#passengerCounts",
       "adultCount": 1
      },
      "tax": [
       {
        "kind": "qpxexpress#taxInfo",
        "id": "YQ_I",
        "chargeType": "CARRIER_SURCHARGE",
        "code": "YQ",
        "salePrice": "USD229.00"
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
      "fareCalculation": "CHI UA LON 1557.00H4E NUC 1557.00 END ROE 1.00 FARE USD 1557.00 XT 17.80US 5.60AY 229.00YQ 4.50XF ORD4.50",
      "latestTicketingTime": "2016-05-12T17:23-04:00",
      "ptc": "ADT",
      "refundable": true
     }
    ]
   },
   {
    "kind": "qpxexpress#tripOption",
    "saleTotal": "USD1813.90",
    "id": "fMbiEAHAPe2MJLTR2P97l700H",
    "slice": [
     {
      "kind": "qpxexpress#sliceInfo",
      "duration": 465,
      "segment": [
       {
        "kind": "qpxexpress#segmentInfo",
        "duration": 465,
        "flight": {
         "carrier": "AY",
         "number": "5536"
        },
        "id": "G1Jg1qjk8mOu2oL2",
        "cabin": "COACH",
        "bookingCode": "H",
        "bookingCodeCount": 3,
        "marriedSegmentGroup": "0",
        "leg": [
         {
          "kind": "qpxexpress#legInfo",
          "id": "LKmVaJevTSAvNzxp",
          "aircraft": "777",
          "arrivalTime": "2016-06-12T10:20+01:00",
          "departureTime": "2016-06-11T20:35-05:00",
          "origin": "ORD",
          "destination": "LHR",
          "originTerminal": "5",
          "destinationTerminal": "5",
          "duration": 465,
          "operatingDisclosure": "OPERATED BY BRITISH AIRWAYS",
          "mileage": 3939,
          "meal": "Meal",
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
        "id": "Aud2Y3nloFDJoOWAXksLyogPIPNGRSVwK9VGfAMNrbKE",
        "carrier": "AY",
        "origin": "CHI",
        "destination": "LON",
        "basisCode": "H1N0O1C5"
       }
      ],
      "segmentPricing": [
       {
        "kind": "qpxexpress#segmentPricing",
        "fareId": "Aud2Y3nloFDJoOWAXksLyogPIPNGRSVwK9VGfAMNrbKE",
        "segmentId": "G1Jg1qjk8mOu2oL2"
       }
      ],
      "baseFareTotal": "USD1557.00",
      "saleFareTotal": "USD1557.00",
      "saleTaxTotal": "USD256.90",
      "saleTotal": "USD1813.90",
      "passengers": {
       "kind": "qpxexpress#passengerCounts",
       "adultCount": 1
      },
      "tax": [
       {
        "kind": "qpxexpress#taxInfo",
        "id": "YR_I",
        "chargeType": "CARRIER_SURCHARGE",
        "code": "YR",
        "salePrice": "USD229.00"
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
      "fareCalculation": "CHI AY LON M 1557.00H1N0O1C5 NUC 1557.00 END ROE 1.00 FARE USD 1557.00 XT 17.80US 5.60AY 229.00YR 4.50XF ORD4.50",
      "latestTicketingTime": "2016-05-12T23:59-04:00",
      "ptc": "ADT",
      "refundable": true
     }
    ]
   },
   {
    "kind": "qpxexpress#tripOption",
    "saleTotal": "USD1813.90",
    "id": "fMbiEAHAPe2MJLTR2P97l700C",
    "slice": [
     {
      "kind": "qpxexpress#sliceInfo",
      "duration": 475,
      "segment": [
       {
        "kind": "qpxexpress#segmentInfo",
        "duration": 475,
        "flight": {
         "carrier": "IB",
         "number": "4212"
        },
        "id": "GRKIBbyuuSHMOfee",
        "cabin": "COACH",
        "bookingCode": "H",
        "bookingCodeCount": 9,
        "marriedSegmentGroup": "0",
        "leg": [
         {
          "kind": "qpxexpress#legInfo",
          "id": "LPFmjip21D0xmEaa",
          "aircraft": "763",
          "arrivalTime": "2016-06-11T22:45+01:00",
          "departureTime": "2016-06-11T08:50-05:00",
          "origin": "ORD",
          "destination": "LHR",
          "originTerminal": "3",
          "destinationTerminal": "3",
          "duration": 475,
          "operatingDisclosure": "OPERATED BY AMERICAN AIRLINES INC.",
          "mileage": 3939,
          "meal": "Breakfast",
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
        "id": "Aefu7R4/poP2CUXxdbOPUPWom/1u8VTBRbqut4mz+NAY",
        "carrier": "IB",
        "origin": "CHI",
        "destination": "LON",
        "basisCode": "H1N0O1C5"
       }
      ],
      "segmentPricing": [
       {
        "kind": "qpxexpress#segmentPricing",
        "fareId": "Aefu7R4/poP2CUXxdbOPUPWom/1u8VTBRbqut4mz+NAY",
        "segmentId": "GRKIBbyuuSHMOfee"
       }
      ],
      "baseFareTotal": "USD1557.00",
      "saleFareTotal": "USD1557.00",
      "saleTaxTotal": "USD256.90",
      "saleTotal": "USD1813.90",
      "passengers": {
       "kind": "qpxexpress#passengerCounts",
       "adultCount": 1
      },
      "tax": [
       {
        "kind": "qpxexpress#taxInfo",
        "id": "YQ_I",
        "chargeType": "CARRIER_SURCHARGE",
        "code": "YQ",
        "salePrice": "USD229.00"
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
      "fareCalculation": "CHI IB LON M 1557.00H1N0O1C5 NUC 1557.00 END ROE 1.00 FARE USD 1557.00 XT 17.80US 5.60AY 229.00YQ 4.50XF ORD4.50",
      "latestTicketingTime": "2016-05-12T23:59-04:00",
      "ptc": "ADT",
      "refundable": true
     }
    ]
   },
   {
    "kind": "qpxexpress#tripOption",
    "saleTotal": "USD1828.90",
    "id": "fMbiEAHAPe2MJLTR2P97l700D",
    "slice": [
     {
      "kind": "qpxexpress#sliceInfo",
      "duration": 475,
      "segment": [
       {
        "kind": "qpxexpress#segmentInfo",
        "duration": 475,
        "flight": {
         "carrier": "BA",
         "number": "1541"
        },
        "id": "GH0SjH5Mzen5v0ZN",
        "cabin": "COACH",
        "bookingCode": "H",
        "bookingCodeCount": 9,
        "marriedSegmentGroup": "0",
        "leg": [
         {
          "kind": "qpxexpress#legInfo",
          "id": "L2S2Qmj89pKJWxH2",
          "aircraft": "763",
          "arrivalTime": "2016-06-11T22:45+01:00",
          "departureTime": "2016-06-11T08:50-05:00",
          "origin": "ORD",
          "destination": "LHR",
          "originTerminal": "3",
          "destinationTerminal": "3",
          "duration": 475,
          "operatingDisclosure": "OPERATED BY AMERICAN AIRLINES INC.",
          "mileage": 3939,
          "meal": "Breakfast",
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
        "id": "AojGx4n6XsVcWSkdQ4cZB/I93sOQTw+m0usMDJRZFTFU",
        "carrier": "BA",
        "origin": "CHI",
        "destination": "LON",
        "basisCode": "H1N0O1CI"
       }
      ],
      "segmentPricing": [
       {
        "kind": "qpxexpress#segmentPricing",
        "fareId": "AojGx4n6XsVcWSkdQ4cZB/I93sOQTw+m0usMDJRZFTFU",
        "segmentId": "GH0SjH5Mzen5v0ZN"
       }
      ],
      "baseFareTotal": "USD1572.00",
      "saleFareTotal": "USD1572.00",
      "saleTaxTotal": "USD256.90",
      "saleTotal": "USD1828.90",
      "passengers": {
       "kind": "qpxexpress#passengerCounts",
       "adultCount": 1
      },
      "tax": [
       {
        "kind": "qpxexpress#taxInfo",
        "id": "YQ_I",
        "chargeType": "CARRIER_SURCHARGE",
        "code": "YQ",
        "salePrice": "USD229.00"
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
      "fareCalculation": "CHI BA LON M 1572.00H1N0O1CI NUC 1572.00 END ROE 1.00 FARE USD 1572.00 XT 17.80US 5.60AY 229.00YQ 4.50XF ORD4.50",
      "latestTicketingTime": "2016-05-12T23:59-04:00",
      "ptc": "ADT"
     }
    ]
   }
  ]
 }
}
