import pytest
from api import PetDemoProject
from context import valid_username, valid_password
from context import name_p, id_stat_p, name_stat_c, status_p, photo_url_p

pdp = PetDemoProject()


# Обновить данные животного по id.
def test_put_api_id_Pet_valid_name(id=id_stat_p):
    _, AuthToken = pdp.post_api_AuthToken(valid_username, valid_password)
    name_upd = name_p
    p_photo_url_upd = photo_url_p
    c_name_upd = name_stat_c
    pet_status = status_p
    status, result = pdp.put_api_Pet_id(AuthToken, id, name_upd, c_name_upd, p_photo_url_upd, pet_status)
    assert status == 200


