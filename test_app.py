from models import get_welcome_message
from app import app

def test_welcome_message():
    expected_message = "Joni is running this from GitHub Actions with MVC structure!"
    assert get_welcome_message() == expected_message
def test_always_passes():
    assert True

def test_home_route():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b'Hello DevOps World!' in response.data
