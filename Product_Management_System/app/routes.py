from flask import Flask,request,jsonify
from datetime import datetime
import app.crud as crud
from app.config import config
import app.emailer as mail

application=Flask(__name__)
# db coonection string
application.config['SQLALCHEMY_DATABASE_URI'] = config['DB_URL']
application.config['SQLALCHEMY_ECHO'] = True

crud.db.init_app(application) # app to db configuration update

# create tables
with application.app_context():
    crud.db.create_all()

@application.route("/products",methods=['POST'])
def create():
    product_dict = request.json
    crud.create_product(product_dict)
    prod_id=product_dict['id']
    savedProduct_dict = crud.read_by_id(prod_id)
    # send the mail
    now=datetime.now()
    date_time_str = now.strftime("%Y-%m-%d %H:%M:%S")
    prod_id= product_dict["id"]
    name= product_dict["name"]
    qty=product_dict["qty"]
    price=product_dict["price"]

    subject=f'{date_time_str} Product {name} Created.'
    mail_body=f''' Product created successfully
    id:{prod_id}
    name:{name}
    qty:{qty}
    price:{price}'''
    result = mail.send_gmail(mail.to_address, subject, mail_body)
    print(f'email sent?{result}')
    # end send the mail
    return jsonify(savedProduct_dict)

@application.route("/products",methods=['GET'])
def read_all():
    products_dict=crud.read_all_products()
    return jsonify(products_dict)

@application.route('/products/<product_id>', methods = ['GET'])
def read_by_id(product_id):
    product_id=int(product_id)
    product_dict=crud.read_by_id(product_id)
    return jsonify(product_dict)

@application.route('/products/<product_id>', methods = ['PUT'])
def update(product_id):
    product_id=int(product_id)
    product_dict = request.json
    crud.update(product_id, product_dict)
    updated_product = crud.read_by_id(product_id)
    return jsonify(updated_product)

@application.route('/products/<product_id>', methods = ['DELETE'])
def delete(product_id):
    product_id=int(product_id)
    crud.delete_product(product_id)
    return jsonify({'message': 'Product deleted successfully'}), 200