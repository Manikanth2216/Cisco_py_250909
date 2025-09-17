'''
import requests
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.logger import logging
from app.exceptions import ProductNotFound,ProductAlreadyExistError,DatabaseError
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

BASE_URL = "http://127.0.0.1:5000"

def create_product(product):
    try:
        url=f'{BASE_URL}/products'
        response=requests.post(url, json=product)
        createdProduct_dict=response.json()
        # Logs
        logging.info("Product created.")
        return createdProduct_dict  
    except IntegrityError as ex:
        logging.error("Duplicate Product id:%s",ex)
        raise ProductAlreadyExistError(f"Product ID={createdProduct_dict['id']} exists already.")
    except SQLAlchemyError as ex:
        logging.error("Database error in creating product:%s",ex)
        raise DatabaseError("Error in creating product.")

def read_all_product():
    try:
        url=f'{BASE_URL}/products'
        response=requests.get(url)
        dict_products=response.json()
        # Logs
        logging.info("Read all products.")
        return dict_products
    except SQLAlchemyError as ex:
        logging.error("Database error in Reading Products:%s",ex)
        raise DatabaseError("Error in Reading all Products.")

def read_by_id(id):
    try:
        url=f'{BASE_URL}/products/{id}'
        response=requests.get(url)
        product_dict=response.json()
        # Logs
        logging.info("Read product by ID.")
        return product_dict
    except IntegrityError as ex:
        logging.error("Product is not found, ID:%s",ex)
        raise ProductNotFound(f"Product ID={product_dict['id']} not found.")
    except SQLAlchemyError as ex:
        logging.error("Database error in Reading Product by ID:%s",ex)
        raise DatabaseError("Error in Reading Product by ID.")

def update(id, new_product):
        url=f'{BASE_URL}/products/{id}'
        response=requests.put(url,json=new_product)
        updateProduct_dict=response.json()
        # Logs
        logging.info("Updated product by ID.")
        return updateProduct_dict

def delete_product(id):
    try:
        url = f'{BASE_URL}/products/{id}'
        response = requests.delete(url)
        message_dict = response.json()
        # Logs
        logging.info("Deleted product by ID.")
        return message_dict
    except SQLAlchemyError as ex:
        logging.error("Database error in Deleting Product by ID:%s",ex)
        raise DatabaseError("Error in Deleting Product by ID.")
'''
import requests
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.logger import logging
from app.exceptions import (
    ProductNotFoundError,
    ProductAlreadyExistError,
    DatabaseError
)
from requests.exceptions import RequestException, HTTPError

BASE_URL = "http://127.0.0.1:5000"


def create_product(product):
    try:
        url = f'{BASE_URL}/products'
        response = requests.post(url, json=product)
        response.raise_for_status()  # Raises HTTPError for 4xx/5xx

        created_product = response.json()
        logging.info("Product created: %s", created_product)
        return created_product

    except HTTPError as e:
        if response.status_code == 400:
            logging.error("Product already exists: %s", response.text)
            raise ProductAlreadyExistError("Product already exists.")
        else:
            logging.error("HTTP error during create: %s", e)
            raise DatabaseError("Unexpected error while creating product.")
    except RequestException as e:
        logging.error("Request failed during create: %s", e)
        raise DatabaseError("Request failed during product creation.")


def read_all_product():
    try:
        url = f'{BASE_URL}/products'
        response = requests.get(url)
        response.raise_for_status()

        products = response.json()
        logging.info("Fetched all products.")
        return products

    except RequestException as e:
        logging.error("Failed to read all products: %s", e)
        raise DatabaseError("Failed to read all products.")


def read_by_id(id):
    try:
        url = f'{BASE_URL}/products/{id}'
        response = requests.get(url)
        response.raise_for_status()

        product = response.json()
        logging.info("Fetched product by ID %s.", id)
        return product

    except HTTPError as e:
        if response.status_code == 404:
            logging.warning("Product ID %s not found.", id)
            raise ProductNotFoundError(f"Product ID={id} not found.")
        else:
            logging.error("HTTP error during read_by_id: %s", e)
            raise DatabaseError("Unexpected error while reading product by ID.")
    except RequestException as e:
        logging.error("Request failed during read_by_id: %s", e)
        raise DatabaseError("Request failed during reading product by ID.")


def update(id, new_product):
    try:
        url = f'{BASE_URL}/products/{id}'
        response = requests.put(url, json=new_product)
        response.raise_for_status()

        updated_product = response.json()
        logging.info("Updated product ID %s: %s", id, updated_product)
        return updated_product

    except HTTPError as e:
        if response.status_code == 404:
            raise ProductNotFoundError(f"Product ID={id} not found for update.")
        else:
            logging.error("HTTP error during update: %s", e)
            raise DatabaseError("Unexpected error while updating product.")
    except RequestException as e:
        logging.error("Request failed during update: %s", e)
        raise DatabaseError("Request failed during product update.")


def delete_product(id):
    try:
        url = f'{BASE_URL}/products/{id}'
        response = requests.delete(url)
        response.raise_for_status()

        message = response.json()
        logging.info("Deleted product ID %s", id)
        return message

    except HTTPError as e:
        if response.status_code == 404:
            raise ProductNotFoundError(f"Product ID={id} not found for deletion.")
        else:
            logging.error("HTTP error during delete: %s", e)
            raise DatabaseError("Unexpected error while deleting product.")
    except RequestException as e:
        logging.error("Request failed during delete: %s", e)
        raise DatabaseError("Request failed during product deletion.")

