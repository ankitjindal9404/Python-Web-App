import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_hello_world(client):
    """Test the / route"""
    response = client.get('/')
    assert response.data == b'Hello, CI/CD!'
    assert response.status_code == 200
