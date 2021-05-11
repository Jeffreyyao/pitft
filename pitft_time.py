from pitft_setup import *
from PIL import Image, ImageDraw, ImageFont
import time
from datetime import datetime

font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf", 135//2)

image = Image.new("RGB", (width, height))
draw = ImageDraw.Draw(image)

def clear():
    draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
    display.image(image)

while 1:
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    clear()
    draw.text((20,135//5), current_time, font=font, fill="#FFFFFF")
    display.image(image)
    time.sleep(60)
