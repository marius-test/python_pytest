import pytest
import requests
import urllib3


@pytest.fixture
def url():
    username = password = None
    return f"https://{username}:{password}@the-internet.herokuapp.com/basic_auth"


def test_valid_login(url):
    username = password = 'admin'
    response = requests.get(url, stream=True)
    # this website returns 401 when login is successful
    assert response.status_code == 401
