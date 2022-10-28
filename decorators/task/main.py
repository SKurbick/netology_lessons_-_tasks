import requests
from utils import logger


@logger(path="log_info.txt")
def get_personage(id_personage):
    return requests.get(f'https://swapi.dev/api/people/{id_personage}').json()


print(get_personage(1))
