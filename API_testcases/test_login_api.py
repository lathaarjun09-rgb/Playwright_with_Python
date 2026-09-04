import pytest
from utils.config_reader import Config

@pytest.mark.api
@pytest.mark.regression
def test_valid_login(api_client):
    response = api_client.get(
        f"/login"
        f"{Config.PARABANK_USERNAME}"
        F"{Config.PARABANK_PASSWORD}"
    )
    
    assert response.status_code == 200
    
# def test_invalid_login(api_client):
#         response = api_client.get(
#         f"/login/invalid/invalidpassword"
#         )
#         assert response.status_code in [400,401,404]
