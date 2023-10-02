import requests
import json
import uuid


class PetDemoProject:
    def __init__(self):
        self.base_url = "http://91.210.171.73:8080/api/"

    # Получение токена
    def post_api_AuthToken(self, username, password):
        data = {
            "username": username,
            "password": password
        }

        res = requests.post(f"{self.base_url}token/auth/", data=data)

        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        print(res.text)
        return status, result

    # Получить список всех категорий животных.
    def get_api_Paginated_Pet_Category_List(self, AuthToken, limit, offset):
        headers = {'Authorization': f"Token {AuthToken['token']}"}
        params = {
            "limit": limit,
            "offset": offset
        }

        res = requests.get(f"{self.base_url}category/", headers=headers, params=params)

        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        print(res.text)
        return status, result

    # Создать категорию животного.
    def post_add_new_Pet_Category(self, AuthToken, category_name):
        headers = {'Authorization': f"Token {AuthToken['token']}"}

        data = {"name": category_name}
        res = requests.post(f"{self.base_url}category/", headers=headers, data=data)

        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    # Получить категорию животного по Id
    def get_api_id_Pet_Category_List(self, AuthToken, id):
        headers = {'Authorization': f"Token {AuthToken['token']}"}
        res = requests.get(f"{self.base_url}category/{id}/", headers=headers)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
            print(res.text)
        return status, result

    # Обновить категорию животного.
    def put_api_id_Pet_Category_name(self, AuthToken, id, category_name):
        headers = {'Authorization': f"Token {AuthToken['token']}"}

        data = {"name": category_name}

        res = requests.put(f"{self.base_url}category/{id}/", headers=headers, data=data)

        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
            print(res.text)
        return status, result

    # Удалить категорию животного по Id
    def delete_api_Pet_Category_id(self, AuthToken, id):

        headers = {'Authorization': f"Token {AuthToken['token']}"}

        res = requests.delete(f"{self.base_url}category/{id}/", headers=headers)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
            print(res.text)
        return status, result

    # Получить список всех животных

    def get_api_Pet_List(self, AuthToken, limit, offset):
        headers = {'Authorization': f"Token {AuthToken['token']}"}
        params = {
            "limit": limit,
            "offset": offset
        }

        res = requests.get(f"{self.base_url}pet/", headers=headers, params=params)

        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    # Создать нового животного.
    def post_api_add_new_Pet(self, token, name, p_photo_url, c_name, status):
        headers = {'Authorization': f"Token {token['token']}", "Content-Type": "application/json"}
        data = {
            "name": name,
            "photo_url": p_photo_url,
            "category": {
                "name": c_name
            },
            "status": status
        }
        res = requests.post(f"{self.base_url}pet/", headers=headers, json=data)

        status = res.status_code
        try:
            result = res.json()
        except ValueError:
            result = res.text
            print(res.text)
        return status, result

    # Получить животное по Id.
    def get_api_id_Pet(self, AuthToken, id):
        headers = {'Authorization': f"Token {AuthToken['token']}"}
        res = requests.get(f"{self.base_url}pet/{id}/", headers=headers)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
            print(res.text)
        return status, result

    # Обновить данные животного по id
    def put_api_Pet_id(self, AuthToken, id, name_upd, c_name_upd, p_photo_url_upd, pet_status):
        headers = {'Authorization': f"Token {AuthToken['token']}"}
        data = {
            "name": name_upd,
            "photo_url": p_photo_url_upd,
            "category": {
                "name": c_name_upd
            },
            "status": pet_status
        }
        res = requests.put(f"{self.base_url}pet/{id}/", headers=headers, json=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
            print(res.text)
        return status, result


    # Удалить животного по Id
    def delete_api_Pet_id(self, AuthToken, id):

        headers = {'Authorization': f"Token {AuthToken['token']}"}

        res = requests.delete(f"{self.base_url}pet/{id}/", headers=headers)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
            print(res.text)
        return status, result
