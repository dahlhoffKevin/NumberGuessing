import pytest
from main import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    # testen aller methoden
    # login test, landet das ergebnis in der datenbank
    #assert response.get_json() == {'message': 'Hello, World!'}
