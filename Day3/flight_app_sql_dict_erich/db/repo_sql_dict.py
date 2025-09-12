from .db_setup import session, Flight 
from .log import logging 
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from .exc import FlightNotFound,FlightAlreadyExistError,DatabaseError
#CRUD (Create, Read All | Read One, Update, Delete)
#Flight App - SQL DB - dict element

def create_flight(flight):
    try:
        flight_model = Flight(
            id = flight['id'],
            flight_number=flight['flight_number'],
            flight_model=flight['flight_model'],
            airline_name=flight['airline_name'],
            seats=flight['seats'],
            price=flight['price'],
            source=flight['source'],
            destination=flight['destination']
        )
        
        session.add(flight_model) #INSERT stmt db 
        session.commit() 
        logging.info("Flight created.")
    except IntegrityError as ex:
        session.rollback()
        logging.error("Duplicate Flight id:%s",ex)
        raise FlightAlreadyExistError(f"Flight ID={flight['id']} exists already.")
    except SQLAlchemyError as ex:
        session.rollback()
        logging.error("Database error in creating flight:%s",ex)
        raise DatabaseError("Error in creating flight.")

def read_all_flights():
    try:
        flights = session.query(Flight).all()
        dict_flights = []
        for flight in flights:
            flight_dict = {
                'id':flight.id,
                'flight_number':flight.flight_number,
                'flight_model':flight.flight_model,
                'airline_name':flight.airline_name,
                'seats':flight.seats,
                'price':flight.price,
                'source':flight.source,
                'destination':flight.destination
            }
            dict_flights.append(flight_dict)
        logging.info("read all flights.")
        return dict_flights
    except SQLAlchemyError as ex:
        session.rollback()
        logging.error("Database error in Reading Flights:%s",ex)
        raise DatabaseError("Error in Reading all Flights.") 
def read_model_by_id(id):
    try:
        flight = session.query(Flight).filter_by(id = id).first()
        logging.info("Read Flight model by ID.")
        return flight
    except IntegrityError as ex:
        session.rollback()
        logging.error("Flight model is not found, ID:%s",ex)
        raise FlightNotFound(f"Flight model ID={flight['id']} not found.")
    except SQLAlchemyError as ex:
        session.rollback()
        logging.error("Database error in Reading Flight model by ID:%s",ex)
        raise DatabaseError("Error in Reading Flight model by ID.")

def read_by_id(id):
    try:
        flight = read_model_by_id(id)
        if not flight:
            logging.error("Flight not found, ID: %s", id)
            raise FlightNotFound(f"Flight ID={id} not found.")
        flight_dict = {
            'id':flight.id,
            'flight_number':flight.flight_number,
            'flight_model':flight.flight_model,
            'airline_name':flight.airline_name,
            'seats':flight.seats,
            'price':flight.price,
            'source':flight.source,
            'destination':flight.destination
        } 
        logging.info("Read flight for given ID.")
        return flight_dict
    except SQLAlchemyError as ex:
        session.rollback()
        logging.error("Database error in Reading Flight by ID:%s",ex)
        raise DatabaseError("Error in Reading Flight by ID.")

def update(id, new_flight):
    try:
        flight = read_model_by_id(id)
        if not flight:
            logging.error("Flight not found, ID:%s",id)
            raise FlightNotFound(f"Flight ID={id} not found.")
        flight.price = new_flight['price']
        session.commit()
        logging.info("Flight price updated.")
    except SQLAlchemyError as ex:
        session.rollback()
        logging.error("Database error in Updating Flight by ID:%s",ex)
        raise DatabaseError("Error in Updating Flight  by ID.")
    
def delete_flight(id):
    try:
        flight = read_model_by_id(id)
        if not flight:
            logging.error("Flight not found, ID:%s",id)
            raise FlightNotFound(f"Flight ID={id} not found.")
        session.delete(flight)
        session.commit()
        logging.info("Flight deleted.")
    except SQLAlchemyError as ex:
        session.rollback()
        logging.error("Database error in Deleting Flight by ID:%s",ex)
        raise DatabaseError("Error in Deleting Flight m by ID.")