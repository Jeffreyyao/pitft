from pitft_setup import *
from PIL import Image, ImageDraw, ImageFont

options = ["Time","Weather","Blog Gallery","Pi Status"]
count = 4
curr_idx = 0

def choose(index):
    clear()
    for i in range(4):
        if i==index:
            draw.text((20,135//5*(i+1)), options[i], font=font, fill="#0000FF")
        else:
            draw.text((20,135//5*(i+1)), options[i], font=font, fill="#FFFFFF")
    display.image(image)
    sleep(1)

choose(0)
while 1:
    if btnUp.is_pressed:
        curr_idx = curr_idx-1 if curr_idx!=0 else count-1
        choose(curr_idx)
    elif btnDown.is_pressed:
        curr_idx = curr_idx+1 if curr_idx!=count-1 else 0
        choose(curr_idx)
