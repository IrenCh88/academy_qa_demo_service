import pytest
from api import PetDemoProject
from context import valid_username, valid_password
from context import name_p, id_p, name_c, id_c, status_p

pdp = PetDemoProject()


# Получить список всех животных.
def test_get_api_Pet_List(limit='', offset=''):
    _, AuthToken = pdp.post_api_AuthToken(valid_username, valid_password)
    status, result = pdp.get_api_Pet_List(AuthToken, limit, offset)
    required_keys = ["count", "next", "previous", "results"]

    assert status == 200
    for key in required_keys:
        assert key in result, f"Key '{key}' is missing."

