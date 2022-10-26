import requests
from pprint import pprint

URL = 'https://swapi.dev/api/people/?page=1'


# print(requests.get(URL).json())


class SwapiPeople:
    base_url = 'https://swapi.dev/api/people/'

    def __init__(self):
        pass

    def __iter__(self):
        self.next_page = self.base_url
        self.chunk = iter([])
        return self

    def __next__(self):
        if self.next_page is None:
            raise StopIteration
        try:
            character = next(self.chunk)
        except StopIteration:
            result = requests.get(self.next_page).json()
            self.next_page = result['next']
            self.chunk = iter(result['results'])
            character = next(self.chunk)
        return character


for item in SwapiPeople():
    print(item)
