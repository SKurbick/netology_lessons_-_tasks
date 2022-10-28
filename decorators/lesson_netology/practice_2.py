import requests
from test_utils import cached
import datetime


@cached(cache_size=10)  # cached_size_10 = cached(10)
def get_personage(id_personage):
    return requests.get(f'https://swapi.dev/api/people/{id_personage}').json()


start = datetime.datetime.now()
print(get_personage(1))
print('время работы:', datetime.datetime.now() - start)

for i in range(1, 15):
    get_personage(i)

