import flight_db_json as flight_db

file_name = 'flight.json'
flights = flight_db.read_from_file(file_name) #[]

def create_flight(flight):
    global flights 
    flights.append(flight)
    flight_db.write_to_file(flights, file_name)

def search_all_flights():
    return flights 

def read_by_id(id):
    for flight in flights:
        if flight['id'] == id:
            return flight
    return None 

'''
def update(id, new_flight):#new_employee is update at id
    global flights
    I = 0
    for flight in flights:
        if flight['id'] == id:
            flight[I] = new_flight
            flight_db.write_to_file(flights, file_name)
            break 
        I += 1
'''
def update(id, new_flight):
    global flights
    for i in range(len(flights)):
        if flights[i]['id'] == id:
            flights[i] = new_flight
            flight_db.write_to_file(flights, file_name)
            break

    
def delete_flight(id):
    global flights
    index = -1
    I = 0
    for flight in flights:
        if flight['id'] == id:
            index = I
            break 
        I += 1
    if index != -1:
        flights.pop(index)
        flight_db.write_to_file(flights, file_name)