from PIL import Image, ImageDraw, ImageFont
import time
from datetime import datetime

font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf", 135//2)

def time_update(display,image,draw):
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    draw.text((20,135//5), current_time, font=font, fill="#FFFFFF")
    display.image(image)
