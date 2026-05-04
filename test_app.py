from models import get_welcome_message

def test_welcome_message():
    expected_message = "Joni is running this from GitHub Actions with MVC structure!"
    assert get_welcome_message() == expected_message
def test_always_passes():
    assert True
