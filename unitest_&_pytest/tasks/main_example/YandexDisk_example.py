import requests
import json

path_token = "/home/malkolmz/Рабочий стол/python_work/project_cloud_storage/tokens/token_YD.txt"


class YandexDisk:
    def __init__(self, token_path, folder='folder_test'):
        self.folder = folder
        # self.token_ya = token_ya
        self.token_path = token_path

    def token(self):
        with open(self.token_path, 'r') as file:
            token = file.read().strip()
            file.close()
        return token

    def get_headers(self):
        token = self.token()
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {token}'
        }

    def create_folder(self):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources"
        params = {'path': f'/{self.folder}'}
        headers = self.get_headers()
        response = requests.put(upload_url, headers=headers, params=params)
        create_folder_status_code = response.status_code

        return create_folder_status_code, self.folder


YD = YandexDisk(path_token)
statu_scode, folder = YD.create_folder()
if statu_scode == 201:
    print(f"Folder '{folder}' successfully created on Yandex Disk")

elif statu_scode == 409:
    print(f"The folder '{folder}' already exists on Yandex Disk")
