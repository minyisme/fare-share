

origin_airport_codes = [u'SFO', u'LAX', u'ORD']

python_results = [{
 "kind": "qpxExpress#tripsSearch",
 "trips": {
  "kind": "qpxexpress#tripOptions",
  "requestId": "kAeRVisyakKmjpYnO0OLzR",
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
     "code": "SFO",
     "city": "SFO",
     "name": "San Francisco International"
    }
   ],
   "city": [
    {
     "kind": "qpxexpress#cityData",
     "code": "NYC",
     "name": "New York"
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
     "code": "32S",
     "name": "Airbus A320"
    }
   ],
   "tax": [
    {
     "kind": "qpxexpress#taxData",
     "id": "ZP",
     "name": "US Flight Segment Tax"
    },
    {
     "kind": "qpxexpress#taxData",
     "id": "AY_001",
     "name": "US September 11th Security Fee"
    },
    {
     "kind": "qpxexpress#taxData",
     "id": "US_001",
     "name": "US Transportation Tax"
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
     "code": "B6",
     "name": "Jetblue Airways Corporation"
    }
   ]
  },
  "tripOption": [
   {
    "kind": "qpxexpress#tripOption",
    "saleTotal": "USD449.60",
    "id": "8aJc7KsSrD4VJ3mTkxD80J001",
    "slice": [
     {
      "kind": "qpxexpress#sliceInfo",
      "duration": 338,
      "segment": [
       {
        "kind": "qpxexpress#segmentInfo",
        "duration": 338,
        "flight": {
         "carrier": "B6",
         "number": "16"
        },
        "id": "GzqOFgdv5JKb3XvS",
        "cabin": "COACH",
        "bookingCode": "Z",
        "bookingCodeCount": 1,
        "marriedSegmentGroup": "0",
        "leg": [
         {
          "kind": "qpxexpress#legInfo",
          "id": "LfsWxiEinrnBGHaw",
          "aircraft": "32S",
          "arrivalTime": "2016-07-11T15:38-04:00",
          "departureTime": "2016-07-11T07:00-07:00",
          "origin": "SFO",
          "destination": "JFK",
          "originTerminal": "I",
          "destinationTerminal": "5",
          "duration": 338,
          "onTimePerformance": 90,
          "mileage": 2579,
          "meal": "Meal",
          "secure": True
         }
        ]
       }
      ]
     },
     {
      "kind": "qpxexpress#sliceInfo",
      "duration": 398,
      "segment": [
       {
        "kind": "qpxexpress#segmentInfo",
        "duration": 398,
        "flight": {
         "carrier": "B6",
         "number": "1415"
        },
        "id": "GjuuL7Bz2H07intQ",
        "cabin": "COACH",
        "bookingCode": "O",
        "bookingCodeCount": 7,
        "marriedSegmentGroup": "1",
        "leg": [
         {
          "kind": "qpxexpress#legInfo",
          "id": "LxtSSNiyfygiMKZJ",
          "aircraft": "32S",
          "arrivalTime": "2016-07-11T21:48-07:00",
          "departureTime": "2016-07-11T18:10-04:00",
          "origin": "JFK",
          "destination": "SFO",
          "originTerminal": "5",
          "destinationTerminal": "I",
          "duration": 398,
          "mileage": 2579,
          "meal": "Meal",
          "secure": True
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
        "id": "AY53iUBBQPajkTs6VnRz5y6Y9PRxvV7d6qfnYL5rTFK2",
        "carrier": "B6",
        "origin": "SFO",
        "destination": "NYC",
        "basisCode": "ZH2ABEN"
       },
       {
        "kind": "qpxexpress#fareInfo",
        "id": "AdJQgNjf1Xwt9+97gwoLuQw94BL3sckoeZaEX8wSTuij12/72PD7Po4/jPrPAQqEy+fBfMfk5CED2VDARJvz7oUuT3Gpkuq700xDHUaY5as3Eftn1L+S7acApw97e/R0S9dNfZYU8ICOvz/",
        "carrier": "B6",
        "origin": "NYC",
        "destination": "SFO",
        "basisCode": "OH2AUEN5",
        "private": True
       }
      ],
      "segmentPricing": [
       {
        "kind": "qpxexpress#segmentPricing",
        "fareId": "AdJQgNjf1Xwt9+97gwoLuQw94BL3sckoeZaEX8wSTuij12/72PD7Po4/jPrPAQqEy+fBfMfk5CED2VDARJvz7oUuT3Gpkuq700xDHUaY5as3Eftn1L+S7acApw97e/R0S9dNfZYU8ICOvz/",
        "segmentId": "GjuuL7Bz2H07intQ"
       },
       {
        "kind": "qpxexpress#segmentPricing",
        "fareId": "AY53iUBBQPajkTs6VnRz5y6Y9PRxvV7d6qfnYL5rTFK2",
        "segmentId": "GzqOFgdv5JKb3XvS"
       }
      ],
      "baseFareTotal": "USD397.21",
      "saleFareTotal": "USD397.21",
      "saleTaxTotal": "USD52.39",
      "saleTotal": "USD449.60",
      "passengers": {
       "kind": "qpxexpress#passengerCounts",
       "adultCount": 1
      },
      "tax": [
       {
        "kind": "qpxexpress#taxInfo",
        "id": "US_001",
        "chargeType": "GOVERNMENT",
        "code": "US",
        "country": "US",
        "salePrice": "USD29.79"
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
        "salePrice": "USD9.00"
       },
       {
        "kind": "qpxexpress#taxInfo",
        "id": "ZP",
        "chargeType": "GOVERNMENT",
        "code": "ZP",
        "country": "US",
        "salePrice": "USD8.00"
       }
      ],
      "fareCalculation": "SFO B6 NYC 207.44ZH2ABEN B6 SFO 189.77OH2AUEN5 USD 397.21 END ZP SFO JFK XT 29.79US 8.00ZP 5.60AY 9.00XF SFO4.50 JFK4.50",
      "latestTicketingTime": "2016-05-18T23:59-04:00",
      "ptc": "ADT"
     }
    ]
   },
   {
    "kind": "qpxexpress#tripOption",
    "saleTotal": "USD522.76",
    "id": "WAZB3auJt95RXqRqK2miYN009",
    "slice": [
     {
      "kind": "qpxexpress#sliceInfo",
      "duration": 580,
      "segment": [
       {
        "kind": "qpxexpress#segmentInfo",
        "duration": 339,
        "flight": {
         "carrier": "B6",
         "number": "434"
        },
        "id": "GGn2S-4yGx6VoEKO",
        "cabin": "COACH",
        "bookingCode": "M",
        "bookingCodeCount": 4,
        "marriedSegmentGroup": "0",
        "leg": [
         {
          "kind": "qpxexpress#legInfo",
          "id": "LS192mP59F77LVRm",
          "aircraft": "320",
          "arrivalTime": "2016-07-11T16:14-04:00",
          "departureTime": "2016-07-11T07:35-07:00",
          "origin": "SFO",
          "destination": "BOS",
          "originTerminal": "I",
          "destinationTerminal": "C",
          "duration": 339,
          "onTimePerformance": 90,
          "mileage": 2697,
          "secure": True
         }
        ],
        "connectionDuration": 161
       },
       {
        "kind": "qpxexpress#segmentInfo",
        "duration": 80,
        "flight": {
         "carrier": "B6",
         "number": "317"
        },
        "id": "G3vLBNT4jdtLfNXi",
        "cabin": "COACH",
        "bookingCode": "U",
        "bookingCodeCount": 7,
        "marriedSegmentGroup": "1",
        "leg": [
         {
          "kind": "qpxexpress#legInfo",
          "id": "L+xpqK06kbnjjpIF",
          "aircraft": "320",
          "arrivalTime": "2016-07-11T20:15-04:00",
          "departureTime": "2016-07-11T18:55-04:00",
          "origin": "BOS",
          "destination": "JFK",
          "originTerminal": "C",
          "destinationTerminal": "5",
          "duration": 80,
          "onTimePerformance": 60,
          "mileage": 186,
          "secure": True
         }
        ]
       }
      ]
     },
     {
      "kind": "qpxexpress#sliceInfo",
      "duration": 390,
      "segment": [
       {
        "kind": "qpxexpress#segmentInfo",
        "duration": 390,
        "flight": {
         "carrier": "B6",
         "number": "1715"
        },
        "id": "GW8n+hTBSDAMZ6qM",
        "cabin": "COACH",
        "bookingCode": "U",
        "bookingCodeCount": 1,
        "marriedSegmentGroup": "2",
        "leg": [
         {
          "kind": "qpxexpress#legInfo",
          "id": "L8lFoOjHnRvVsGwT",
          "aircraft": "32S",
          "arrivalTime": "2016-07-12T00:50-07:00",
          "departureTime": "2016-07-11T21:20-04:00",
          "origin": "JFK",
          "destination": "SFO",
          "originTerminal": "5",
          "destinationTerminal": "I",
          "duration": 390,
          "onTimePerformance": 70,
          "mileage": 2579,
          "meal": "Meal",
          "secure": True
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
        "id": "AYaXQJgdDMlcVCeHBDgyBhhwelDQLICT4IGPmyGF1t9Ry87qxOSAIjzHGGeLEaKpbnoyrYI/OFtJ/C5yapl62mh2t/pp6Qu9ABLsdzC5NIuTdFFva/Ux855TkLXqpz7UFqc211i3V+rnSjo",
        "carrier": "B6",
        "origin": "SFO",
        "destination": "BOS",
        "basisCode": "MH4KUEN5",
        "private": True
       },
       {
        "kind": "qpxexpress#fareInfo",
        "id": "AsZ/Ayv9mwypBPLZj135dWwM84Y7NcxCQAoEAY1nMARo",
        "carrier": "B6",
        "origin": "BOS",
        "destination": "SFO",
        "basisCode": "UH2AUEN"
       }
      ],
      "segmentPricing": [
       {
        "kind": "qpxexpress#segmentPricing",
        "fareId": "AYaXQJgdDMlcVCeHBDgyBhhwelDQLICT4IGPmyGF1t9Ry87qxOSAIjzHGGeLEaKpbnoyrYI/OFtJ/C5yapl62mh2t/pp6Qu9ABLsdzC5NIuTdFFva/Ux855TkLXqpz7UFqc211i3V+rnSjo",
        "segmentId": "GGn2S-4yGx6VoEKO"
       },
       {
        "kind": "qpxexpress#segmentPricing",
        "fareId": "AsZ/Ayv9mwypBPLZj135dWwM84Y7NcxCQAoEAY1nMARo",
        "segmentId": "GW8n+hTBSDAMZ6qM"
       },
       {
        "kind": "qpxexpress#segmentPricing",
        "fareId": "AsZ/Ayv9mwypBPLZj135dWwM84Y7NcxCQAoEAY1nMARo",
        "segmentId": "G3vLBNT4jdtLfNXi"
       }
      ],
      "baseFareTotal": "USD457.36",
      "saleFareTotal": "USD457.36",
      "saleTaxTotal": "USD65.40",
      "saleTotal": "USD522.76",
      "passengers": {
       "kind": "qpxexpress#passengerCounts",
       "adultCount": 1
      },
      "tax": [
       {
        "kind": "qpxexpress#taxInfo",
        "id": "US_001",
        "chargeType": "GOVERNMENT",
        "code": "US",
        "country": "US",
        "salePrice": "USD34.30"
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
        "salePrice": "USD13.50"
       },
       {
        "kind": "qpxexpress#taxInfo",
        "id": "ZP",
        "chargeType": "GOVERNMENT",
        "code": "ZP",
        "country": "US",
        "salePrice": "USD12.00"
       }
      ],
      "fareCalculation": "SFO B6 X/BOS Q12.70 253.95MH4KUEN5 B6 X/NYC B6 SFO 190.70UH2AUEN 1S0.01 USD 457.36 END ZP SFO BOS JFK XT 34.30US 12.00ZP 5.60AY 13.50XF SFO4.50 BOS4.50 JFK4.50",
      "latestTicketingTime": "2016-05-18T23:59-04:00",
      "ptc": "ADT"
     }
    ]
   }
  ]
 }
},
{
 "kind": "qpxExpress#tripsSearch",
 "trips": {
  "kind": "qpxexpress#tripOptions",
  "requestId": "nUFnJbU4rFeuXQpN60OLzR",
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
     "code": "LAX",
     "city": "LAX",
     "name": "Los Angeles International"
    }
   ],
   "city": [
    {
     "kind": "qpxexpress#cityData",
     "code": "LAX",
     "name": "Los Angeles"
    },
    {
     "kind": "qpxexpress#cityData",
     "code": "NYC",
     "name": "New York"
    }
   ],
   "aircraft": [
    {
     "kind": "qpxexpress#aircraftData",
     "code": "32S",
     "name": "Airbus A320"
    }
   ],
   "tax": [
    {
     "kind": "qpxexpress#taxData",
     "id": "ZP",
     "name": "US Flight Segment Tax"
    },
    {
     "kind": "qpxexpress#taxData",
     "id": "AY_001",
     "name": "US September 11th Security Fee"
    },
    {
     "kind": "qpxexpress#taxData",
     "id": "US_001",
     "name": "US Transportation Tax"
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
     "code": "B6",
     "name": "Jetblue Airways Corporation"
    }
   ]
  },
  "tripOption": [
   {
    "kind": "qpxexpress#tripOption",
    "saleTotal": "USD502.20",
    "id": "RZ6pOC1XD7KPc63YG59xdD001",
    "slice": [
     {
      "kind": "qpxexpress#sliceInfo",
      "duration": 330,
      "segment": [
       {
        "kind": "qpxexpress#segmentInfo",
        "duration": 330,
        "flight": {
         "carrier": "B6",
         "number": "224"
        },
        "id": "GQ-H2bI3wCGOCrTU",
        "cabin": "COACH",
        "bookingCode": "Z",
        "bookingCodeCount": 1,
        "marriedSegmentGroup": "0",
        "leg": [
         {
          "kind": "qpxexpress#legInfo",
          "id": "LfFS71XgAR054YrW",
          "aircraft": "32S",
          "arrivalTime": "2016-07-11T18:15-04:00",
          "departureTime": "2016-07-11T09:45-07:00",
          "origin": "LAX",
          "destination": "JFK",
          "originTerminal": "3",
          "destinationTerminal": "5",
          "duration": 330,
          "mileage": 2468,
          "meal": "Meal",
          "secure": True
         }
        ]
       }
      ]
     },
     {
      "kind": "qpxexpress#sliceInfo",
      "duration": 358,
      "segment": [
       {
        "kind": "qpxexpress#segmentInfo",
        "duration": 358,
        "flight": {
         "carrier": "B6",
         "number": "2023"
        },
        "id": "G5b0HDy2qrHqkKH2",
        "cabin": "COACH",
        "bookingCode": "M",
        "bookingCodeCount": 7,
        "marriedSegmentGroup": "1",
        "leg": [
         {
          "kind": "qpxexpress#legInfo",
          "id": "LpwLPvtyUy1AUR6+",
          "aircraft": "32S",
          "arrivalTime": "2016-07-12T01:43-07:00",
          "departureTime": "2016-07-11T22:45-04:00",
          "origin": "JFK",
          "destination": "LAX",
          "originTerminal": "5",
          "destinationTerminal": "3",
          "duration": 358,
          "onTimePerformance": 70,
          "mileage": 2468,
          "meal": "Meal",
          "secure": True
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
        "id": "AYma/ib1CqckVTDpmyNKyS8t97l/0ACcPJLvxC+fysfyXSgprb1Rm22C6+vA0kPbxkbiGcyPUx02Mn1VFbcMFoUQz3Q1vKih1B2M6lzHsHfyoeZRcLwMrtElPwGRVlG4kgMxJyuD8yFtM6/",
        "carrier": "B6",
        "origin": "LAX",
        "destination": "NYC",
        "basisCode": "ZH4AUEN5",
        "private": True
       },
       {
        "kind": "qpxexpress#fareInfo",
        "id": "ANgd1wvCu6ENAYSx2W6LTpDZKVC/jB127HLBXiUQO3Vo",
        "carrier": "B6",
        "origin": "NYC",
        "destination": "LAX",
        "basisCode": "MH4ABEN"
       }
      ],
      "segmentPricing": [
       {
        "kind": "qpxexpress#segmentPricing",
        "fareId": "ANgd1wvCu6ENAYSx2W6LTpDZKVC/jB127HLBXiUQO3Vo",
        "segmentId": "G5b0HDy2qrHqkKH2"
       },
       {
        "kind": "qpxexpress#segmentPricing",
        "fareId": "AYma/ib1CqckVTDpmyNKyS8t97l/0ACcPJLvxC+fysfyXSgprb1Rm22C6+vA0kPbxkbiGcyPUx02Mn1VFbcMFoUQz3Q1vKih1B2M6lzHsHfyoeZRcLwMrtElPwGRVlG4kgMxJyuD8yFtM6/",
        "segmentId": "GQ-H2bI3wCGOCrTU"
       }
      ],
      "baseFareTotal": "USD440.93",
      "saleFareTotal": "USD440.93",
      "saleTaxTotal": "USD61.27",
      "saleTotal": "USD502.20",
      "passengers": {
       "kind": "qpxexpress#passengerCounts",
       "adultCount": 1
      },
      "tax": [
       {
        "kind": "qpxexpress#taxInfo",
        "id": "US_001",
        "chargeType": "GOVERNMENT",
        "code": "US",
        "country": "US",
        "salePrice": "USD33.07"
       },
       {
        "kind": "qpxexpress#taxInfo",
        "id": "AY_001",
        "chargeType": "GOVERNMENT",
        "code": "AY",
        "country": "US",
        "salePrice": "USD11.20"
       },
       {
        "kind": "qpxexpress#taxInfo",
        "id": "XF",
        "chargeType": "GOVERNMENT",
        "code": "XF",
        "country": "US",
        "salePrice": "USD9.00"
       },
       {
        "kind": "qpxexpress#taxInfo",
        "id": "ZP",
        "chargeType": "GOVERNMENT",
        "code": "ZP",
        "country": "US",
        "salePrice": "USD8.00"
       }
      ],
      "fareCalculation": "LAX B6 NYC 213.02ZH4AUEN5 B6 LAX 227.91MH4ABEN USD 440.93 END ZP LAX JFK XT 33.07US 8.00ZP 11.20AY 9.00XF LAX4.50 JFK4.50",
      "latestTicketingTime": "2016-05-18T23:59-04:00",
      "ptc": "ADT"
     }
    ]
   },
   {
    "kind": "qpxexpress#tripOption",
    "saleTotal": "USD512.60",
    "id": "RZ6pOC1XD7KPc63YG59xdD002",
    "slice": [
     {
      "kind": "qpxexpress#sliceInfo",
      "duration": 330,
      "segment": [
       {
        "kind": "qpxexpress#segmentInfo",
        "duration": 330,
        "flight": {
         "carrier": "B6",
         "number": "324"
        },
        "id": "G3WGJt7LCRt-iKGL",
        "cabin": "COACH",
        "bookingCode": "M",
        "bookingCodeCount": 7,
        "marriedSegmentGroup": "0",
        "leg": [
         {
          "kind": "qpxexpress#legInfo",
          "id": "L97q2yalL-8c1Ld9",
          "aircraft": "32S",
          "arrivalTime": "2016-07-11T20:05-04:00",
          "departureTime": "2016-07-11T11:35-07:00",
          "origin": "LAX",
          "destination": "JFK",
          "originTerminal": "3",
          "destinationTerminal": "5",
          "duration": 330,
          "onTimePerformance": 90,
          "mileage": 2468,
          "meal": "Meal",
          "secure": True
         }
        ]
       }
      ]
     },
     {
      "kind": "qpxexpress#sliceInfo",
      "duration": 358,
      "segment": [
       {
        "kind": "qpxexpress#segmentInfo",
        "duration": 358,
        "flight": {
         "carrier": "B6",
         "number": "2023"
        },
        "id": "G5b0HDy2qrHqkKH2",
        "cabin": "COACH",
        "bookingCode": "M",
        "bookingCodeCount": 7,
        "marriedSegmentGroup": "1",
        "leg": [
         {
          "kind": "qpxexpress#legInfo",
          "id": "LpwLPvtyUy1AUR6+",
          "aircraft": "32S",
          "arrivalTime": "2016-07-12T01:43-07:00",
          "departureTime": "2016-07-11T22:45-04:00",
          "origin": "JFK",
          "destination": "LAX",
          "originTerminal": "5",
          "destinationTerminal": "3",
          "duration": 358,
          "onTimePerformance": 70,
          "mileage": 2468,
          "meal": "Meal",
          "secure": True
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
        "id": "ANgd1wvCu6ENAYSx2W6LTpDZKVC/jB127HLBXiUQO3Vo",
        "carrier": "B6",
        "origin": "LAX",
        "destination": "NYC",
        "basisCode": "MH4ABEN"
       },
       {
        "kind": "qpxexpress#fareInfo",
        "id": "ANgd1wvCu6ENAYSx2W6LTpDZKVC/jB127HLBXiUQO3Vo",
        "carrier": "B6",
        "origin": "NYC",
        "destination": "LAX",
        "basisCode": "MH4ABEN"
       }
      ],
      "segmentPricing": [
       {
        "kind": "qpxexpress#segmentPricing",
        "fareId": "ANgd1wvCu6ENAYSx2W6LTpDZKVC/jB127HLBXiUQO3Vo",
        "segmentId": "G5b0HDy2qrHqkKH2"
       },
       {
        "kind": "qpxexpress#segmentPricing",
        "fareId": "ANgd1wvCu6ENAYSx2W6LTpDZKVC/jB127HLBXiUQO3Vo",
        "segmentId": "G3WGJt7LCRt-iKGL"
       }
      ],
      "baseFareTotal": "USD455.82",
      "saleFareTotal": "USD455.82",
      "saleTaxTotal": "USD56.78",
      "saleTotal": "USD512.60",
      "passengers": {
       "kind": "qpxexpress#passengerCounts",
       "adultCount": 1
      },
      "tax": [
       {
        "kind": "qpxexpress#taxInfo",
        "id": "US_001",
        "chargeType": "GOVERNMENT",
        "code": "US",
        "country": "US",
        "salePrice": "USD34.18"
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
        "salePrice": "USD9.00"
       },
       {
        "kind": "qpxexpress#taxInfo",
        "id": "ZP",
        "chargeType": "GOVERNMENT",
        "code": "ZP",
        "country": "US",
        "salePrice": "USD8.00"
       }
      ],
      "fareCalculation": "LAX B6 NYC 227.91MH4ABEN B6 LAX 227.91MH4ABEN USD 455.82 END ZP LAX JFK XT 34.18US 8.00ZP 5.60AY 9.00XF LAX4.50 JFK4.50",
      "latestTicketingTime": "2016-05-18T23:59-04:00",
      "ptc": "ADT"
     }
    ]
   }
  ]
 }
},
{
 "kind": "qpxExpress#tripsSearch",
 "trips": {
  "kind": "qpxexpress#tripOptions",
  "requestId": "H4paXxLlHnyrgz36h0OLzR",
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
     "code": "NYC",
     "name": "New York"
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
     "code": "E90",
     "name": "Embraer RJ-190"
    }
   ],
   "tax": [
    {
     "kind": "qpxexpress#taxData",
     "id": "ZP",
     "name": "US Flight Segment Tax"
    },
    {
     "kind": "qpxexpress#taxData",
     "id": "AY_001",
     "name": "US September 11th Security Fee"
    },
    {
     "kind": "qpxexpress#taxData",
     "id": "US_001",
     "name": "US Transportation Tax"
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
     "code": "B6",
     "name": "Jetblue Airways Corporation"
    }
   ]
  },
  "tripOption": [
   {
    "kind": "qpxexpress#tripOption",
    "saleTotal": "USD288.20",
    "id": "JLb8IuTAP41T6wu8qmEkrJ002",
    "slice": [
     {
      "kind": "qpxexpress#sliceInfo",
      "duration": 133,
      "segment": [
       {
        "kind": "qpxexpress#segmentInfo",
        "duration": 133,
        "flight": {
         "carrier": "B6",
         "number": "906"
        },
        "id": "GFMaEID0stp4343E",
        "cabin": "COACH",
        "bookingCode": "M",
        "bookingCodeCount": 1,
        "marriedSegmentGroup": "0",
        "leg": [
         {
          "kind": "qpxexpress#legInfo",
          "id": "LEMJBMf3iT3coS5+",
          "aircraft": "320",
          "arrivalTime": "2016-07-11T12:03-04:00",
          "departureTime": "2016-07-11T08:50-05:00",
          "origin": "ORD",
          "destination": "JFK",
          "originTerminal": "3",
          "destinationTerminal": "5",
          "duration": 133,
          "mileage": 737,
          "secure": True
         }
        ]
       }
      ]
     },
     {
      "kind": "qpxexpress#sliceInfo",
      "duration": 168,
      "segment": [
       {
        "kind": "qpxexpress#segmentInfo",
        "duration": 168,
        "flight": {
         "carrier": "B6",
         "number": "105"
        },
        "id": "G-sLpmxXrlFirVVW",
        "cabin": "COACH",
        "bookingCode": "U",
        "bookingCodeCount": 1,
        "marriedSegmentGroup": "1",
        "leg": [
         {
          "kind": "qpxexpress#legInfo",
          "id": "LKHKN1YMKOBnxeze",
          "aircraft": "E90",
          "arrivalTime": "2016-07-11T22:28-05:00",
          "departureTime": "2016-07-11T20:40-04:00",
          "origin": "JFK",
          "destination": "ORD",
          "originTerminal": "5",
          "destinationTerminal": "3",
          "duration": 168,
          "mileage": 737,
          "secure": True
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
        "id": "AWQSZKg4WdIzjGRe9MxuCxp1HWx5y2Qhb7p9up7xqYeM",
        "carrier": "B6",
        "origin": "CHI",
        "destination": "NYC",
        "basisCode": "MH4ADEN"
       },
       {
        "kind": "qpxexpress#fareInfo",
        "id": "AZU6Tx1goGk9mCCCZ5tC62Q+1jDZlYvi7CZt0ov+mMBeUSMDpEofiXOQSV/ZY1CkWBywEaMbS74zIndFfWaZ/VkqoiRZydRZz91koxjDECcuifZl8IB+LkljvqRibh06vGuxPzGTgrCBNyo",
        "carrier": "B6",
        "origin": "NYC",
        "destination": "CHI",
        "basisCode": "UI7ABEN5",
        "private": True
       }
      ],
      "segmentPricing": [
       {
        "kind": "qpxexpress#segmentPricing",
        "fareId": "AWQSZKg4WdIzjGRe9MxuCxp1HWx5y2Qhb7p9up7xqYeM",
        "segmentId": "GFMaEID0stp4343E"
       },
       {
        "kind": "qpxexpress#segmentPricing",
        "fareId": "AZU6Tx1goGk9mCCCZ5tC62Q+1jDZlYvi7CZt0ov+mMBeUSMDpEofiXOQSV/ZY1CkWBywEaMbS74zIndFfWaZ/VkqoiRZydRZz91koxjDECcuifZl8IB+LkljvqRibh06vGuxPzGTgrCBNyo",
        "segmentId": "G-sLpmxXrlFirVVW"
       }
      ],
      "baseFareTotal": "USD241.86",
      "saleFareTotal": "USD241.86",
      "saleTaxTotal": "USD46.34",
      "saleTotal": "USD288.20",
      "passengers": {
       "kind": "qpxexpress#passengerCounts",
       "adultCount": 1
      },
      "tax": [
       {
        "kind": "qpxexpress#taxInfo",
        "id": "US_001",
        "chargeType": "GOVERNMENT",
        "code": "US",
        "country": "US",
        "salePrice": "USD18.14"
       },
       {
        "kind": "qpxexpress#taxInfo",
        "id": "AY_001",
        "chargeType": "GOVERNMENT",
        "code": "AY",
        "country": "US",
        "salePrice": "USD11.20"
       },
       {
        "kind": "qpxexpress#taxInfo",
        "id": "XF",
        "chargeType": "GOVERNMENT",
        "code": "XF",
        "country": "US",
        "salePrice": "USD9.00"
       },
       {
        "kind": "qpxexpress#taxInfo",
        "id": "ZP",
        "chargeType": "GOVERNMENT",
        "code": "ZP",
        "country": "US",
        "salePrice": "USD8.00"
       }
      ],
      "fareCalculation": "CHI B6 JFK 146.98MH4ADEN B6 CHI 94.88UI7ABEN5 USD 241.86 END ZP ORD JFK XT 18.14US 8.00ZP 11.20AY 9.00XF ORD4.50 JFK4.50",
      "latestTicketingTime": "2016-05-18T23:59-04:00",
      "ptc": "ADT"
     }
    ]
   },
   {
    "kind": "qpxexpress#tripOption",
    "saleTotal": "USD288.20",
    "id": "JLb8IuTAP41T6wu8qmEkrJ001",
    "slice": [
     {
      "kind": "qpxexpress#sliceInfo",
      "duration": 129,
      "segment": [
       {
        "kind": "qpxexpress#segmentInfo",
        "duration": 129,
        "flight": {
         "carrier": "B6",
         "number": "106"
        },
        "id": "GM-vWt6g5m9rK1GO",
        "cabin": "COACH",
        "bookingCode": "M",
        "bookingCodeCount": 1,
        "marriedSegmentGroup": "0",
        "leg": [
         {
          "kind": "qpxexpress#legInfo",
          "id": "LUvOuw0XyHjnUxnd",
          "aircraft": "E90",
          "arrivalTime": "2016-07-11T09:09-04:00",
          "departureTime": "2016-07-11T06:00-05:00",
          "origin": "ORD",
          "destination": "JFK",
          "originTerminal": "3",
          "destinationTerminal": "5",
          "duration": 129,
          "mileage": 737,
          "secure": True
         }
        ]
       }
      ]
     },
     {
      "kind": "qpxexpress#sliceInfo",
      "duration": 168,
      "segment": [
       {
        "kind": "qpxexpress#segmentInfo",
        "duration": 168,
        "flight": {
         "carrier": "B6",
         "number": "105"
        },
        "id": "G-sLpmxXrlFirVVW",
        "cabin": "COACH",
        "bookingCode": "U",
        "bookingCodeCount": 1,
        "marriedSegmentGroup": "1",
        "leg": [
         {
          "kind": "qpxexpress#legInfo",
          "id": "LKHKN1YMKOBnxeze",
          "aircraft": "E90",
          "arrivalTime": "2016-07-11T22:28-05:00",
          "departureTime": "2016-07-11T20:40-04:00",
          "origin": "JFK",
          "destination": "ORD",
          "originTerminal": "5",
          "destinationTerminal": "3",
          "duration": 168,
          "mileage": 737,
          "secure": True
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
        "id": "AWQSZKg4WdIzjGRe9MxuCxp1HWx5y2Qhb7p9up7xqYeM",
        "carrier": "B6",
        "origin": "CHI",
        "destination": "NYC",
        "basisCode": "MH4ADEN"
       },
       {
        "kind": "qpxexpress#fareInfo",
        "id": "AZU6Tx1goGk9mCCCZ5tC62Q+1jDZlYvi7CZt0ov+mMBeUSMDpEofiXOQSV/ZY1CkWBywEaMbS74zIndFfWaZ/VkqoiRZydRZz91koxjDECcuifZl8IB+LkljvqRibh06vGuxPzGTgrCBNyo",
        "carrier": "B6",
        "origin": "NYC",
        "destination": "CHI",
        "basisCode": "UI7ABEN5",
        "private": True
       }
      ],
      "segmentPricing": [
       {
        "kind": "qpxexpress#segmentPricing",
        "fareId": "AWQSZKg4WdIzjGRe9MxuCxp1HWx5y2Qhb7p9up7xqYeM",
        "segmentId": "GM-vWt6g5m9rK1GO"
       },
       {
        "kind": "qpxexpress#segmentPricing",
        "fareId": "AZU6Tx1goGk9mCCCZ5tC62Q+1jDZlYvi7CZt0ov+mMBeUSMDpEofiXOQSV/ZY1CkWBywEaMbS74zIndFfWaZ/VkqoiRZydRZz91koxjDECcuifZl8IB+LkljvqRibh06vGuxPzGTgrCBNyo",
        "segmentId": "G-sLpmxXrlFirVVW"
       }
      ],
      "baseFareTotal": "USD241.86",
      "saleFareTotal": "USD241.86",
      "saleTaxTotal": "USD46.34",
      "saleTotal": "USD288.20",
      "passengers": {
       "kind": "qpxexpress#passengerCounts",
       "adultCount": 1
      },
      "tax": [
       {
        "kind": "qpxexpress#taxInfo",
        "id": "US_001",
        "chargeType": "GOVERNMENT",
        "code": "US",
        "country": "US",
        "salePrice": "USD18.14"
       },
       {
        "kind": "qpxexpress#taxInfo",
        "id": "AY_001",
        "chargeType": "GOVERNMENT",
        "code": "AY",
        "country": "US",
        "salePrice": "USD11.20"
       },
       {
        "kind": "qpxexpress#taxInfo",
        "id": "XF",
        "chargeType": "GOVERNMENT",
        "code": "XF",
        "country": "US",
        "salePrice": "USD9.00"
       },
       {
        "kind": "qpxexpress#taxInfo",
        "id": "ZP",
        "chargeType": "GOVERNMENT",
        "code": "ZP",
        "country": "US",
        "salePrice": "USD8.00"
       }
      ],
      "fareCalculation": "CHI B6 JFK 146.98MH4ADEN B6 CHI 94.88UI7ABEN5 USD 241.86 END ZP ORD JFK XT 18.14US 8.00ZP 11.20AY 9.00XF ORD4.50 JFK4.50",
      "latestTicketingTime": "2016-05-18T23:59-04:00",
      "ptc": "ADT"
     }
    ]
   }
  ]
 }
}]

count = 0
dict_results_by_origin = {}
for origin_airport_code in origin_airport_codes:
    dict_results_by_origin[origin_airport_code] = python_results[count]
    # print dict_results_by_origin
    count += 1


dict_flights = {}
dict_legs = {}
flights = []
for origin in dict_results_by_origin:
    dict_flights[origin] = []
    for w in range(len(dict_results_by_origin[origin]["trips"]["tripOption"])):
        dict_flights[origin].append(dict_results_by_origin[origin]["trips"]["tripOption"][w]["saleTotal"])
        # Calculating connection possible and duration time, but not needed once data model changes
        for x in range(len(dict_results_by_origin[origin]["trips"]["tripOption"][w]["slice"])):
            if dict_results_by_origin[origin]["trips"]["tripOption"][w]["slice"][x]["segment"][0].get("connectionDuration"):
                dict_flights[origin].append(True)
                dict_flights[origin].append(dict_results_by_origin[origin]["trips"]["tripOption"][w]["slice"][x]["segment"][0]["connectionDuration"])
            else:
                dict_flights[origin].append(False)
                dict_flights[origin].append(0)


    flight = Flight(option_id=option.option_id, flight_price=dict_flights[origin][0], has_layover=dict_flights[origin][1], layover_duration=dict_flights[origin][2])

    db.session.add(flight)
    db.session.commit()

    flights.append(flight.flight_id)

dict_legs = {}
for origin in dict_results_by_origin:





# flight = Flight(option_id=option.option_id, flight_price=dict_)
#     flight: self.flight_id, 
#             self.option_id, 
#             self.flight_price, 
#             self.has_layover, 
#             self.layover_duration


# #     leg: self.leg_id, 
# #          self.flight_id, 
# #          self.direction, 
# #          self.origin_airport, 
# #          self.departure_datetime, 
# #          self.destination_airport, 
# #          self.arrival_datetime, 
# #          self.leg_airline, 
# #          self.leg_flight_code, 
# #          self.leg_duration

# print search_results
# print flight_query_results2(search_results)
