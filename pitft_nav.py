from pitft_setup import *
from PIL import Image, ImageDraw, ImageFont
import time

options = ["Time","Weather","Blog Gallery","Pi Status"]
count = 4
curr_idx = 0

def init():
    clear()
    for i in range(4):
        if i==0:
            draw.rectangle([0,135//5*(i+1)-15,width,135//5*(i+1)-15+20], fill="#FFFFFF")
            draw.text((20,135//5*(i+1)-15), options[i], font=font, fill="#000000")
        else:
            draw.text((20,135//5*(i+1)-15), options[i], font=font, fill="#FFFFFF")
    display.image(image)
    time.sleep(1)

def choose(index,prev_index):
    draw.text((20,135//5*(index+1)-15), options[index], font=font, fill="#0000FF")
    draw.text((20,135//5*(prev_index+1)-15), options[prev_index], font=font, fill="#FFFFFF")
    display.image(image)
    time.sleep(0.5)

init()
while 1:
    if btnUp.is_pressed:
        prev_idx = curr_idx
        curr_idx = curr_idx-1 if curr_idx!=0 else count-1
        choose(curr_idx,prev_idx)
    elif btnDown.is_pressed:
        prev_idx = curr_idx
        curr_idx = curr_idx+1 if curr_idx!=count-1 else 0
        choose(curr_idx,prev_idx)
