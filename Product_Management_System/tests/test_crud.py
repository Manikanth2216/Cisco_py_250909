import pytest
from unittest.mock import patch
import client.repo as repo
from app.models import Product

@pytest.fixture(autouse=True)
def setup():
    # Placeholder for any setup/teardown logic (optional for now)
    yield

@patch('client.repo.requests.post')
def test_create_product(mock_post):
    # Create a SQLAlchemy model instance (not persisted to any DB)
    product = Product(id=1, name='Laptop', qty=10, price=50000)
    product_data = product.to_dict()

    # Mock the API response
    mock_response = mock_post.return_value
    mock_response.status_code = 201
    mock_response.json.return_value = product_data

    # Call the function under test
    created_product = repo.create_product(product_data)

    # Assertions to verify correct behavior
    assert created_product['id'] == product.id
    assert created_product['name'] == product.name
    assert created_product['qty'] == product.qty
    assert created_product['price'] == product.price

    # Ensure the POST request was made exactly once
    mock_post.assert_called_once()
