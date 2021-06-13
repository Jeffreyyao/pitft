from pitft_setup import display,image,draw,font,btnUp,btnDown,clear,width,height
from PIL import Image, ImageDraw, ImageFont
import time
from signal import pause
import os

options = ["Time","Weather","Blog Gallery","Pi Stats"]
scripts = ["pitft_time.py","pitft_weather.py","pitft_blog_gallery.py","pitft_stats.py"]
count = 4
curr_idx = 0
prev_idx = 0
prev_time = 0

def init():
    clear()
    global curr_idx
    global prev_idx
    curr_idx = 0
    prev_idx = 0
    for i in range(4):
        if i==0:
            draw.rectangle([0,135//5*(i+1)-15,width,135//5*(i+1)-15+20], fill="#FFFFFF")
            draw.text((20,135//5*(i+1)-15), options[i], font=font, fill="#000000")
        else:
            draw.text((20,135//5*(i+1)-15), options[i], font=font, fill="#FFFFFF")
    display.image(image)
    time.sleep(0.5)

def choose(index,prev_index):
    draw.rectangle([0,135//5*(index+1)-15,width,135//5*(index+1)-15+20], fill="#FFFFFF")
    draw.text((20,135//5*(index+1)-15), options[index], font=font, fill="#000000")
    draw.rectangle([0,135//5*(prev_index+1)-15,width,135//5*(prev_index+1)-15+20], fill="#000000")
    draw.text((20,135//5*(prev_index+1)-15), options[prev_index], font=font, fill="#FFFFFF")
    display.image(image)
    time.sleep(0.2)
    
def pressed():
    global prev_time
    prev_time = time.time()
    
def btnUp_released():
    global prev_idx
    global curr_idx
    if time.time()-prev_time < 2:
        prev_idx = curr_idx
        curr_idx = curr_idx-1 if curr_idx!=0 else count-1
        choose(curr_idx,prev_idx)
    else:
        if curr_idx == 0:
            import pitft_time
        elif curr_idx == 1:
            from pitft_weather import weather_update
            clear()
            weather_update(display,image,draw,font)
            btnUp.when_pressed = ret
            btnDown.when_pressed = ret
        elif curr_idx == 2:
            import pitft_blog_gallery
        else:
            import pitft_stats
            

def btnDown_released():
    global prev_idx
    global curr_idx
    prev_idx = curr_idx
    curr_idx = curr_idx+1 if curr_idx!=count-1 else 0
    choose(curr_idx,prev_idx)
    
def ret():
    init()
    btnUp.when_pressed = pressed
    btnUp.when_released = btnUp_released
    btnDown.when_pressed = None
    btnDown.when_released = btnDown_released
    print("returned")
    
init()

btnUp.when_pressed = pressed
btnUp.when_released = btnUp_released
btnDown.when_released = btnDown_released

pause()
