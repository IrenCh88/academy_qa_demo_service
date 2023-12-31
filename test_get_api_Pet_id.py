import pytest
from api import PetDemoProject
from context import valid_username, valid_password
from context import name_p, id_p, name_c, id_c, status_p, id_stat_p

pdp = PetDemoProject()

# Получить животного по Id
def test_get_api_id_Pet(p_id = id_stat_p):
    _, AuthToken = pdp.post_api_AuthToken(valid_username, valid_password)

    status, result = pdp.get_api_id_Pet(AuthToken, p_id)

    assert status == 200
    assert "id" in result
    assert "name" in result
    assert "photo_url" in result
    assert "category" in result
    assert "status" in result
