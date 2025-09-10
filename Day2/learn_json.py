import json
flight={'flight_number': 'I700', 'airline': 'Indigo','capacity': 225, 'price': 4500,'source': 'Bangalore', 'destination': 'Hyderabad'}
file_name='learn_json.json'
print('Before file:', flight)

with open(file_name, 'w') as writer:
    json.dump(flight, writer)
    print('Saved the flight to json file')

with open(file_name, 'r') as reader:
    flight_from_file = json.load(reader) #the byte by byte from the file is read from flight.dat and converted as flight object

print('Flight after read from json file:', flight_from_file)