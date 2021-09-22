import pytest
from test_data.specimen_data import specimen_good_data

import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017')
db = client['dispimdb']

@pytest.fixture(scope="function")
def mongo_delete_documents(request):
    specimens = db.specimens

    def teardown():
        print('Tearing down db')
        for specimen in specimen_good_data:
            specimens.delete_one({'specimen_id': specimen['specimen_id']})
    
    request.addfinalizer(teardown)

@pytest.fixture(scope="session")
def mongo_insert_documents(request):
    specimens = db.specimens
    specimens.insert_many(specimen_good_data)

    def teardown():
        print('Tearing down db')
        for specimen in specimen_good_data:
            specimens.delete_one({'specimen_id': specimen['specimen_id']})
    
    request.addfinalizer(teardown)

@pytest.fixture()
def my_name():
    return "Sam Kinn".upper()

@pytest.fixture()
def list_of_numbers():
    return [1, 2, 3, 4]

@pytest.fixture()
def good_specimens():
    return specimen_good_data