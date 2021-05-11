from pitft_setup import *
from PIL import Image, ImageDraw, ImageFont
import time
from datetime import datetime
import urllib.request as req
import re
import requests

font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf", 20)

image = Image.new("RGB", (width, height))
draw = ImageDraw.Draw(image)

def clear():
    draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
    display.image(image)

def update():
    req_url = "http://api.weatherapi.com/v1/current.json?key=c5fbb5f073b64c74ad651622211105&q=Boulder&aqi=no"
    res = req.urlopen(req_url).read()

    weather = re.findall('text":".+?"',str(res))[0].replace('text":"','').replace('"','')
    temp = re.findall('temp_c":.+?,',str(res))[0].replace('temp_c":','').replace(',','')+" C"
    icon = "https://"+re.findall('icon":"//.+?png',str(res))[0].replace('icon":"//',"")

    clear()
    draw.bitmap((20,135//5*3),Image.open(requests.get(icon, stream=True).raw))
    draw.text((20,135//5), weather, font=font, fill="#FFFFFF")
    draw.text((20,135//5*2), temp, font=font, fill="#FFFFFF")
    display.image(image)

update()

while 1:
    if btnUp.is_pressed or btnDown.is_pressed:
        update()
