'''

from db import repo_sql_dict as repo

def menu():
    message = ''#'
Options are:
1 - Create Flight
2 - List All Flights
3 - Search Flight By Id
4 - Update Flight
5 - Delete Flight
6 - Exit 
Your Option:''#'


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
                  'airline_name':airline_name, 'seats':seats, 'price':price,
                  'source':source, 'destination':destination}

        try:  
            repo.create_flight(flight)
            print('Flight Created Successfully.')
        except repo.FlightAlreadyExistError as ex:
            print(f"{ex}")
        except repo.DatabaseError as ex:
            print(f"{ex}")
    elif choice == 2:
        try:
            print('List of Flights:')
            for flight in repo.read_all_flights():
                print(flight)
        except repo.DatabaseError as ex:
            print(f"{ex}")
    elif choice == 3:
        try:
            id = int(input('ID:'))
            flight = repo.read_by_id(id)
            print(flight)
        except repo.FlightNotFound as ex:
            print(f"{ex}")
        except repo.DatabaseError as ex:
            print(f"{ex}")
    elif choice == 4:
        try:
            id = int(input('ID:'))
            flight = repo.read_by_id(id)
            print(flight)
            price = float(input('New Price:'))
            new_flight = {
                'id':flight['id'],
                'flight_number':flight['flight_number'],
                'flight_model':flight['flight_model'],
                'airline_name':flight['airline_name'],
                'seats':flight['seats'],
                'price':flight['price'],
                'source':flight['source'],
                'destination':flight['destination']
            }
            repo.update(id, new_flight)
            print('Flight updated successfully.')
        except repo.FlightNotFound as ex:
            print(f"{ex}")
        except repo.DatabaseError as ex:
            print(f"{ex}")
    elif choice == 5:
        try:
            id = int(input('ID:'))
            flight = repo.read_by_id(id)
            repo.delete_flight(id)
            print('Flight Deleted Succesfully.')
        except repo.FlightNotFound as ex:
            print(f"{ex}")
        except repo.DatabaseError as ex:
            print(f"{ex}")
    elif choice == 6: 
        print('Thank you for using Application')

    return choice 

def menus():
    choice = menu()
    while choice != 6:
        choice = menu()
    
menus()

'''

from db import repo_sql_dict as repo

def menu():
    """
    Function DocString
    """
    message = '''
Options are:
1 - Create Flight
2 - List All Flights
3 - Search Flight By Id
4 - Update Flight
5 - Delete Flight
6 - Exit
Your Option: '''

    try:
        choice = int(input(message))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return 0

    try:
        if choice == 1:
            id = int(input('ID: '))
            flight_number = input('Flight Number:')
            flight_model = input('Flight Model:')
            airline_name = input('Airline Name:')
            seats = int(input('Seats:'))
            price = float(input('Price:'))
            source = input('Source:')
            destination = input('Destination:')
            flight = {'id':id, 'flight_number':flight_number, 'flight_model':flight_model,
                      'airline_name':airline_name, 'seats':seats, 'price':price,
                      'source':source, 'destination':destination}
            repo.create_flight(flight)
            print('Flight Created Successfully.')


        elif choice == 2:
            print('List of Flights: ')
            for flight in repo.read_all_flights():
                print(flight)

        elif choice == 3:
            id = int(input('ID: '))
            flight = repo.read_by_id(id)
            print(flight)

        elif choice == 4:
            id = int(input('ID: '))
            flight = repo.read_by_id(id)
            print(flight)
            price = float(input('New Price: '))
            flight['price'] = price
            repo.update(id, flight)
            print('Flight updated successfully.')

        elif choice == 5:
            id = int(input('ID: '))
            repo.delete_flight(id)
            print('Flight deleted successfully.')

        elif choice == 6:
            print('Thank you for using the application.')
            return 6

        else:
            print("Invalid option. Please choose a number between 1 and 6.")

    except ValueError:
        print("Invalid input. Please enter the correct data types.")

    except repo.FlightNotFound as ex:
        print(f"{ex}")
    except repo.FlightAlreadyExistError as ex:
        print(f"{ex}")
    except repo.DatabaseError as ex:
        print(f"{ex}")

    return choice

def run_app():
    """
    Function DocString
    """
    while True:
        choice = menu()
        if choice == 6:
            break

run_app()
