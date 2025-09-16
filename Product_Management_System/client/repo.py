import requests
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app')))
from app.logger import logging

BASE_URL = "http://127.0.0.1:5000"

def create_product(product):
    url=f'{BASE_URL}/products'
    response=requests.post(url, json=product)
    createdProduct_dict=response.json()
    # Logs
    logging.info("Product created.")
    return createdProduct_dict  

def read_all_product():
    url=f'{BASE_URL}/products'
    response=requests.get(url)
    dict_products=response.json()
    # Logs
    logging.info("Read all products.")
    return dict_products

def read_by_id(id):
    url=f'{BASE_URL}/products/{id}'
    response=requests.get(url)
    product_dict=response.json()
    # Logs
    logging.info("Read product by ID.")
    return product_dict

def update(id, new_product):
    url=f'{BASE_URL}/products/{id}'
    response=requests.put(url,json=new_product)
    updateProduct_dict=response.json()
    # Logs
    logging.info("Updated product by ID.")
    return updateProduct_dict

def delete_product(id):
    url = f'{BASE_URL}/products/{id}'
    response = requests.delete(url)
    message_dict = response.json()
    # Logs
    logging.info("Deleted product by ID.")
    return message_dict
