class FlightException(Exception):
    pass

class FlightNotFound(FlightException):
    pass

class FlightAlreadyExistError(FlightException):
    pass

class DatabaseError(FlightException):
    pass