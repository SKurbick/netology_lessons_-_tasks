import requests


# вывод данных о персонажах
def get_swapi_people():
    next_page = 'https://swapi.dev/api/people/'  # api

    while next_page:  # пока "next" не является None
        result = requests.get(next_page).json()
        next_page = result['next']  # изменяет api по следующему ключу из предыдущего api
        for character in result['results']:
            yield character
        print("***************")


for item in get_swapi_people():
    print(item)


