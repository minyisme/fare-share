f = open('airport.txt')

list_of_airports = []

for line in f:
    list_of_airports.append(line[4:])

list_of_airports2 = []

for airport in list_of_airports:
    list_of_airports2.append(airport[:-6])

print list_of_airports2
