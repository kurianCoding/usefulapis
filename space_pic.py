import requests
from PIL import Image
import json
import io
from datetime import datetime,timedelta

API_KEY= "kUkGiCxLXwQzP6wtuTkxx2ggpyHJg8swHuHv8jye"

def test_api():
    res = requests.get(f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}")
    if res.status_code!=200:
        return False
    return True

def get_pic_of_day():
    today = datetime.today()    
    start_date = today - timedelta(days=1)
    start_date = start_date.strftime("%Y-%m-%d")
    end_date = today.strftime("%Y-%m-%d")
    res = requests.get(f"https://api.nasa.gov/planetary/apod?&start_date={start_date}&end_date={end_date}&api_key={API_KEY}")
    return res

if __name__ == "__main__":
    for pic in get_pic_of_day().json():
        res = requests.get(pic["url"])
        ext = pic["url"].split(".")[-1]
        file_name = pic["title"] 
        with open(f"{file_name}.{ext}","wb+") as imagefile:
            imagefile.write(res.content)
