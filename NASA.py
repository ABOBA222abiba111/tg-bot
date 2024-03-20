import requests
from dotenv import load_dotenv 
import os 
from pprint import pprint

def get_nasa_picture() : 

    load_dotenv()
    key1 = os.getenv("key")

    params = {
        "api_key" : key1,
        "count" : 10
    }

    url = "https://api.nasa.gov/planetary/apod"

    list = []
    response = requests.get(url , params=params)
    response.raise_for_status()
    for i in response.json() :
        text_nasa = i["explanation"]
        element = i["url"]
        list_text = [text_nasa , element]
        list.append(list_text)
    return list