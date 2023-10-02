from api import PetDemoProject
from context import valid_username, valid_password


pdp = PetDemoProject()

# Получение токена
def test_post_AuthToken_valid_admin(username=valid_username, password=valid_password):
    status, result = pdp.post_api_AuthToken(username, password)
    assert status == 200

    assert "token" in result

    token = result["token"]
