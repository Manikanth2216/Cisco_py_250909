class EmployeeException(Exception):
    pass

class EmployeeNotFound(EmployeeException):
    pass

class EmployeeAlreadyExistError(EmployeeException):
    pass

class DatabaseError(EmployeeException):
    pass