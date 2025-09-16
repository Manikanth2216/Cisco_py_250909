from app.models import db, Product

def create_product(product):
    product_model = Product(
        id=product['id'],
        name=product['name'],
        qty=product['qty'],
        price=product['price'])
    db.session.add(product_model)
    db.session.commit()

def read_all_products():
    products=db.session.query(Product).all()
    dict_products=[]
    for product in products:
        product_dict=product.to_dict()
        dict_products.append(product_dict)
    return dict_products 

def read_model_by_id(id):
    product=db.session.query(Product).filter_by(id=id).first()
    return product

def read_by_id(id):
    product=read_model_by_id(id)
    if not product:
        return None
    product_dict=product.to_dict()
    return product_dict

def update(id, new_product):
    product=read_model_by_id(id)
    if not product:
        return
    product.price=new_product['price']
    db.session.commit()
    
    
def delete_product(id):
    product = read_model_by_id(id)
    if not product:
        return
    db.session.delete(product)
    db.session.commit()