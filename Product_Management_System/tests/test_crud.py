import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from client import repo

Base= declarative_base() 

class Product(Base):
    __tablename__ = "products"
    id=Column(Integer, primary_key=True)
    name=Column(String(255), nullable=False)
    qty=Column(Integer, nullable=False)
    price=Column(Float, nullable=False)

    def __repr__(self):
        return f'[id={self.id}, name={self.name}, qty={self.qty}, price={self.price}]'

    def to_dict(self):
        return {'id' : self.id,
                'name' : self.name,
                'qty' : self.qty, 'price' : self.price}

engine = create_engine("sqlite:///product_app_db.db", echo=True)
Base.metadata.create_all(engine) # creates tables
# session for sql operations
SessionLocal=sessionmaker(bind=engine)
session=SessionLocal()

def test_create_product():
    product = Product(id=100, name='Laptop', qty=10, price=50000)
    created_product = repo.create_product(product)
    assert created_product['id'] == product.id
    assert created_product['name'] == product.name
    assert created_product['qty'] == product.qty
    assert created_product['price'] == product.price
