import flight_repo_json_dict as flight_repo

def menu():
    message = '''
Options are:
1 - Create Flight
2 - List All Flights
3 - Search Flight By Id
4 - Update Flight
5 - Delete Flight
6 - Exit 
Your Option:'''
    choice = int(input(message))
    if choice == 1:
        id = int(input('ID:'))
        flight_number = input('Flight Number:')
        flight_model = input('Flight Model:')
        airline_name = input('Airline Name:')
        seats = int(input('Seats:'))
        price = float(input('Price:'))
        source = input('Source:')
        destination = input('Destination:')

        flight = {'id':id, 'flight_number':flight_number, 'flight_model':flight_model,
                  'airline_name':airline_name, 'seats':seats, 'price':price, 'source':source, 'destination':destination}

        flight_repo.create_flight(flight)

        print('Flight Created Successfully.')
    elif choice == 2:
        print('List of Flights:')
        for flight in flight_repo.search_all_flights():
            print(flight)
    elif choice == 3:
        id = int(input('ID:'))
        flight = flight_repo.read_by_id(id)
        if flight == None:
            print('Flight not found.')
        else:
            print(flight)
    elif choice == 4:
        id = int(input('ID:'))
        flight = flight_repo.read_by_id(id)
        if flight == None: 
            print('Flight Not Found')
        else:
            print(flight)
            price = float(input('New Price:'))
            new_flight = {
                'id':flight['id'],
                'flight_number':flight['flight_number'],
                'flight_model':flight['flight_model'],
                'airline_name':flight['airline_name'],
                'seats':flight['seats'],
                'price':price, 
                'source':flight['source'], 
                'destination':flight['destination']
            }
            flight_repo.update(id, new_flight)
            print('Flight updated successfully.')
    elif choice == 5:
        id = int(input('ID:'))
        flight = flight_repo.read_by_id(id)
        if flight == None: 
            print('Flight Not Found')
        else:
            flight_repo.delete_flight(id)
            print('Flight Deleted Succesfully.')
    elif choice == 6: 
        print('Thank you for using Application')

    return choice 

def menus():
    choice = menu()
    while choice != 6:
        choice = menu()
    
menus()