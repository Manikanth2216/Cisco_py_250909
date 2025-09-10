import json 
import os

def read_from_file(filename = 'flight.json'):
    if not os.path.exists(filename):
        flights = []
        return flights
    
    with open(filename, 'r') as reader:
        flights = json.load(reader)
        return flights
    
def write_to_file(flights, filename = 'flight.json'):
    with open(filename, 'w') as writer:
        json.dump(flights, writer) 