from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer, Float, Boolean

Base= declarative_base() # model base class

#models

class Flight(Base): # our model class employee defined from ORM
    __tablename__ = "flights"
    id=Column(Integer, primary_key=True)
    flight_number=Column(String(255), nullable=False)
    flight_model=Column(String(255), nullable=False)
    airline_name=Column(String(255), nullable=False)
    seats=Column(Integer, nullable=False)
    price=Column(Float, nullable=False)
    source=Column(String(255), nullable=False)
    destination=Column(String(255), nullable=False)


    def __repr__(self):
        return f'[id={self.id}, flight_number={self.flight_number}, flight_model={self.flight_model}, airline_name={self.airline_name}, seats={self.seats}, price={self.price}, source={self.source}, destination={self.destination}]'
