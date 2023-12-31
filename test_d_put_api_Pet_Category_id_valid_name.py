import pytest
from api import PetDemoProject
from context import valid_username, valid_password
from context import name_p, id_p, name_c, id_c, status_p

pdp = PetDemoProject()


# Обновить категорию животного.
def test_put_api_id_Pet_Category_valid_name(c_id = id_c):
    _, AuthToken = pdp.post_api_AuthToken(valid_username, valid_password)

    category_name = name_c
    status, result = pdp.put_api_id_Pet_Category_name(AuthToken, c_id, category_name)
    assert status == 200
    assert "id" in result
    assert "name" in result
