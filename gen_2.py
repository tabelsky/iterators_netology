
import requests


def get_swapi_people():
    next_page = 'https://swapi.dev/api/people/'

    while next_page:
        result = requests.get(next_page).json()
        next_page = result['next']
        for character in result['results']:
            yield character


if __name__ == '__main__':
    for item in get_swapi_people():
        print(item)
