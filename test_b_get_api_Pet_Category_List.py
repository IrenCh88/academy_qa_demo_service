﻿import pytest
from api import PetDemoProject
from context import valid_username, valid_password
from context import name_p, id_p, name_c, id_c, status_p

pdp = PetDemoProject()

# Получить список категорий животных.

def test_get_api_Paginated_Pet_Category_List(limit='', offset=''):
    _, AuthToken = pdp.post_api_AuthToken(valid_username, valid_password)
    status, result = pdp.get_api_Paginated_Pet_Category_List(AuthToken, limit, offset)
    assert status == 200
    assert "count" in result
    assert "next" in result
    assert "previous" in result
    assert "results" in result
    for item in result["results"]:
        assert "id" in item
        assert "name" in item
