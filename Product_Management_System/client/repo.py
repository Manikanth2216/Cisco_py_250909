import requests

BASE_URL = "http://127.0.0.1:5000"

def create_product(product):
    url=f'{BASE_URL}/products'
    response=requests.post(url, json=product)
    createdProduct_dict=response.json()
    return createdProduct_dict  

def read_all_product():
    url=f'{BASE_URL}/products'
    response=requests.get(url)
    dict_products=response.json()
    return dict_products

def read_by_id(id):
    url=f'{BASE_URL}/products/{id}'
    response=requests.get(url)
    product_dict=response.json()
    return product_dict

def update(id, new_product):
    url=f'{BASE_URL}/products/{id}'
    response=requests.put(url,json=new_product)
    updateProduct_dict=response.json()
    return updateProduct_dict

def delete_product(id):
    url = f'{BASE_URL}/products/{id}'
    response = requests.delete(url)
    message_dict = response.json() 
    return message_dict
