import requests
from PIL import Image
import json
import io
from datetime import datetime,timedelta

API_KEY= "kUkGiCxLXwQzP6wtuTkxx2ggpyHJg8swHuHv8jye"

def test_api():
    res = requests.get("https://api.nasa.gov/planetary/apod?api_key=kUkGiCxLXwQzP6wtuTkxx2ggpyHJg8swHuHv8jye")
    if res.status_code!=200:
        return False
    return True

def get_pic_of_day():
    today = datetime.today()
    start_date = today - timedelta(days=1)
    start_date = start_date.strftime("%Y-%m-%d")
    end_date = today.strftime("%Y-%m-%d")
    res = requests.get("https://api.nasa.gov/planetary/apod?&start_date={}&end_date={}&api_key={}".format(start_date,end_date,API_KEY))
    return res

if __name__ == "__main__":
    for pic in get_pic_of_day().json():
        res = requests.get(pic["url"])
        ext = pic["url"].split(".")[-1]
        with open(pic["title"]+"."+ext,"wb+") as imagefile:
            imagefile.write(res.content)
