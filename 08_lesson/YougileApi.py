import requests


class YougileApi:
    def __init__(self, url):
        self.url = url

    # получение ключа
    def get_api_key(self, login='***', password='***',
                    companyId='***'):
        # здесь для удобства кэшируем ключ
        if hasattr(self, "token_cache") and self.token_cache:
            return {"key": self.token_cache}

        creds = {
            "login": login,
            "password": password,
            "companyId": companyId
        }
        resp = requests.post(self.url + '/api-v2/auth/keys', json=creds)

        data = resp.json()
        if "key" in data:
            self.token_cache = data["key"]

        return data

    # создание нового проекта
    def create_new_project(self, title):
        auth = self.get_api_key()
        token = auth["key"]
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}"
        }
        project_name = {"title": title}
        resp = requests.post(self.url + '/api-v2/projects', json=project_name,
                             headers=headers)
        return resp

    # изменение проекта
    def update_project(self, id, new_title):
        auth = self.get_api_key()
        token = auth["key"]
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}"
        }
        update_title = {"title": new_title}
        resp = requests.put(self.url + f'/api-v2/projects/{id}',
                            json=update_title, headers=headers)
        return resp

    # пoлучение проект по ID
    def get_project_id(self, id):
        auth = self.get_api_key()
        token = auth["key"]
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}"
        }
        resp = requests.get(self.url + f'/api-v2/projects/{id}',
                            headers=headers)
        return resp
