from pitft import *
from PIL import Image, ImageDraw, ImageFont
import time
from datetime import datetime
import urllib.request as req
import re
import requests
from signal import pause
import os

def weather_update():
    req_url = "http://api.weatherapi.com/v1/current.json?key=c5fbb5f073b64c74ad651622211105&q=Boulder&aqi=no"
    res = req.urlopen(req_url).read()

    weather = re.findall('text":".+?"',str(res))[0].replace('text":"','').replace('"','')
    temp = re.findall('temp_c":.+?,',str(res))[0].replace('temp_c":','').replace(',','')+" C"
    icon = "https://"+re.findall('icon":"//.+?png',str(res))[0].replace('icon":"//',"")

    clear()
    draw.text((20,135//5), weather, font=font, fill="#FFFFFF")
    draw.text((20,135//5*2), temp, font=font, fill="#FFFFFF")
    draw.bitmap((100,135//5*2),Image.open(requests.get(icon, stream=True).raw))
    display.image(image)
    time.sleep(2)

if __name__=="__main__":
    weather_update()
