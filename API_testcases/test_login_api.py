import pytest
from utilities.config_reader import Config


@pytest.mark.api
@pytest.mark.regression
def test_valid_login(api_client):

    response = api_client.get(
        "/login.htm",
        params={
            "username": Config.PARABANK_USERNAME,
            "password": Config.PARABANK_PASSWORD
        }
    )

    print("STATUS:", response.status_code)
    print("URL:", response.url)
    print("RESPONSE:", response.text)

    assert response.status_code == 200