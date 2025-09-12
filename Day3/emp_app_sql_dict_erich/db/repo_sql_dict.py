from .db_setup import session, Employee 
from .log import logging 
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from .exc import EmployeeNotFound,EmployeeAlreadyExistError,DatabaseError
#CRUD (Create, Read All | Read One, Update, Delete)
#Employee App - SQL DB - dict element

def create_employee(employee):
    try:
        employee_model = Employee(id = employee['id'],
            name = employee['name'],
            age = employee['age'],
            salary = employee['salary'],
            is_active = employee['is_active'] )
        session.add(employee_model) #INSERT stmt db 
        session.commit() 
        logging.info("employee created.")
    except IntegrityError as ex:
        session.rollback()
        logging.error("Duplicate employee id:%s",ex)
        raise EmployeeAlreadyExistError(f"Employee ID={employee['id']} exists already.")
    except SQLAlchemyError as ex:
        session.rollback()
        logging.error("Database error in creating emoployee:%s",ex)
        raise DatabaseError("Error in creating employee.")

def read_all_employee():
    try:
        employees = session.query(Employee).all()
        dict_employees = []
        for employee in employees:
            employee_dict = {'id':employee.id, 
                'name':employee.name,
                'age':employee.age, 'salary':employee.salary,'is_active':employee.is_active}
            dict_employees.append(employee_dict)
        logging.info("read all employees.")
        return dict_employees
    except SQLAlchemyError as ex:
        session.rollback()
        logging.error("Database error in Reading emoployees:%s",ex)
        raise DatabaseError("Error in Reading all employees.") 
def read_model_by_id(id):
    try:
        employee = session.query(Employee).filter_by(id = id).first()
        logging.info("read employee model by ID.")
        return employee
    except IntegrityError as ex:
        session.rollback()
        logging.error("Employee model is not found, ID:%s",ex)
        raise EmployeeNotFound(f"Employee model ID={employee['id']} not found.")
    except SQLAlchemyError as ex:
        session.rollback()
        logging.error("Database error in Reading emoployee model by ID:%s",ex)
        raise DatabaseError("Error in Reading employee model by ID.")

def read_by_id(id):
    try:
        employee = read_model_by_id(id)
        if not employee: #if employee == None:
            logging.error("Employee not found, ID: %s", id)
            raise EmployeeNotFound(f"Employee ID={id} not found.")
        employee_dict = {'id':employee.id,
            'name':employee.name,
            'age':employee.age,'salary':employee.salary,'is_active':employee.is_active} 
        logging.info("read employee for given id.")
        return employee_dict
    except SQLAlchemyError as ex:
        session.rollback()
        logging.error("Database error in Reading emoployee  by ID:%s",ex)
        raise DatabaseError("Error in Reading employee  by ID.")

def update(id, new_employee):
    try:
        employee = read_model_by_id(id)
        if not employee:
            logging.error("Employee not found, ID:%s",id)
            raise EmployeeNotFound(f"Employee ID={id} not found.")
        employee.salary = new_employee['salary']
        session.commit()
        logging.info("employee salary updated.")
    except SQLAlchemyError as ex:
        session.rollback()
        logging.error("Database error in Updating employee by ID:%s",ex)
        raise DatabaseError("Error in Updating employee  by ID.")
    
def delete_employee(id):
    try:
        employee = read_model_by_id(id)
        if not employee:
            logging.error("Employee not found, ID:%s",id)
            raise EmployeeNotFound(f"Employee ID={id} not found.")
        session.delete(employee)
        session.commit()
        logging.info("employee deleted.")
    except SQLAlchemyError as ex:
        session.rollback()
        logging.error("Database error in Deleting employee by ID:%s",ex)
        raise DatabaseError("Error in Deleting employee m by ID.")