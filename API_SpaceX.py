import requests
from pprint import pprint

def get_speesx_picture() :

    url = "https://api.spacexdata.com/v4/launches"

    response = requests.get(url)
    response.raise_for_status()
    for i in reversed(response.json()) :
        if i["links"]["flickr"]["original"] :
            text = f'Крайний запуск ракеты SpaceX. Cовершен {i["date_local"]} '
            list = [i["links"]["flickr"]["original"] , text]
            return list
