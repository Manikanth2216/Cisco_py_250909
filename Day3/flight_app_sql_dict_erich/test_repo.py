import pytest
from db import db_setup
from db import repo_sql_dict as repo

@pytest.fixture(autouse=True)
def setup():
    db_setup.Base.metadata.drop_all(db_setup.engine)
    db_setup.Base.metadata.create_all(db_setup.engine)
    yield
    db_setup.Base.metadata.drop_all(db_setup.engine)

def test_create_flight():
    flight = {'id':100, 'flight_number':'AZ0001', 'flight_model':'Airbus350',
                  'airline_name':'Air Newzeland', 'seats':350, 'price':1000, 'source':'Hyderabad', 'destination':'LosAngeles'}
    repo.create_flight(flight)
    savedFlight=repo.read_by_id(100)
    assert(savedFlight!=None)
    assert(savedFlight['id']==100)
    assert(savedFlight['flight_number']=='AZ0001')
    assert(savedFlight['flight_model']=='Airbus350')
    assert(savedFlight['airline_name']=='Air Newzeland')
    assert(savedFlight['seats']==350)
    assert(savedFlight['price']==1000)
    assert(savedFlight['source']=='Hyderabad')
    assert(savedFlight['destination']=='LosAngeles')