import os 
from dotenv import load_dotenv
import requests
import NASA
import API_SpaceX
import random 
from time import sleep

def sendpicture(random_pic_tx) :

    load_dotenv()
    chat = os.getenv("chat")
    tg_bot1 = os.getenv("tg_bot")
    print(tg_bot1)

    url = f"https://api.telegram.org/bot{tg_bot1}/sendphoto"
    params = {
        "photo" : random_pic_tx[1] ,
        "chat_id" : chat ,
        "caption" : random_pic_tx[0]
    }

    respons = requests.post(url , params=params)
    print(respons.json())
    
def main() :
    for i in range(10) :
        try :
            nasa_pictures = NASA.get_nasa_picture()
        except :
            print("nasa.error")
        try :
            api_sepsex_picture = API_SpaceX.get_speesx_picture()
        except :
            print("API_SpaceX.error")
        nasa_speesx = nasa_pictures + api_sepsex_picture
        random_pic_tx = random.choice(nasa_speesx)
        try :
            sendpicture(random_pic_tx)
        except :
            print("telegram.error")
        sleep(3600)

if __name__ == "__main__":
    main()
    