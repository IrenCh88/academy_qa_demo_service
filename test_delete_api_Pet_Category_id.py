import pytest
from api import PetDemoProject
from context import valid_username, valid_password
from context import id_stat_c, id_c

pdp = PetDemoProject()


# Удалить категорию животного по Id
def test_delete_api_Pet_Category_id(id=id_stat_c):
    _, AuthToken = pdp.post_api_AuthToken(valid_username, valid_password)

    status, result = pdp.delete_api_Pet_Category_id(AuthToken, id)
    assert status == 204

