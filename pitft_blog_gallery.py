from pitft_setup import *
from PIL import Image
from gpiozero import Button
import os
import time

btn_prev = Button(23)
btn_next = Button(24)

path = "/home/pi/JJ/jeffreyyao.github.io/images/"
files = os.listdir(path)
files.remove(".DS_Store")
i = 0;

def displayImage(i):
    display.fill(color565(0,0,0))
    image = Image.open(path+files[i])
    image.thumbnail((240,135),Image.ANTIALIAS)
    display.image(image)
    time.sleep(1)

displayImage(0)

while True:
    if btn_prev.is_pressed:
        i = i-1 if i>0 else len(files)-1
        displayImage(i)
    if btn_next.is_pressed:
        i = i+1 if i<len(files) else 0
        displayImage(i)