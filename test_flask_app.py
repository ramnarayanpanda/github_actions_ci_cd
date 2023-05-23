import pytest
from app import app
import json


# here we will create one client and 
# using this client we will be able to send, get and post requests 
@pytest.fixture
def client():
    return app.test_client()

# all the functions starting with test_ only will be tested bu pytest
def test_ping(client):
    resp = client.get('/ping')
    assert resp.status_code == 200
    assert resp.json == {"message": "Hi there, I'm working with the new API!!"}

def test_predict(client):
    test_data = {"Gender":"Male", 
    "Married":"Unmarried",
    "Credit_History" : "Unclear Debts",
    "ApplicantIncome":100000,
    "LoanAmount":2000000}
    resp = client.post("/predict", json=test_data)
    assert resp.status_code == 200
    assert resp.json == {'loan_approval_status': 'Rejected'}

# to test all the test functions inside this file run:  pytest test_flask_app.py
