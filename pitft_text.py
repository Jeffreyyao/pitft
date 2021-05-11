from pitft_setup import *
from PIL import Image, ImageDraw, ImageFont
import sys

font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf", 135//2)

image = Image.new("RGB", (width, height))
draw = ImageDraw.Draw(image)

draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
display.image(image)

if len(sys.argv)==2:
    text = sys.argv[1]
else:
    text = "Hello"

draw.text((0,135//4), text, font=font, fill="#FFFFFF")

display.image(image)
