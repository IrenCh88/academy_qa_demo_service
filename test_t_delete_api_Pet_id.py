import pytest
from api import PetDemoProject
from context import valid_username, valid_password
from context import id_p, id_stat_p

pdp = PetDemoProject()


# Удалить  животного по Id
def test_delete_api_Pet_Category_id(id=id_stat_p):
    _, AuthToken = pdp.post_api_AuthToken(valid_username, valid_password)

    status, result = pdp.delete_api_Pet_id(AuthToken, id)
    assert status == 204

