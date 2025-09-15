"""
Module Docstring
"""
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer, Float

Base= declarative_base() # model base class

#models

class Flight(Base): # our model class employee defined from ORM
    """
    Class Docstring
    """
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
        """
        Comment
        """
        return f'[id={self.id}, flight_number={self.flight_number}, ' + \
            f'flight_model={self.flight_model}, ' + \
            f'airline_name={self.airline_name}, seats={self.seats}, price={self.price}, ' + \
            f'source={self.source},destination={self.destination}]'

    def __str__(self):
        """
        Comment
        """
        return self.__repr__()
