#modify /root/config.txt before using custom pitft

import digitalio
import board
import gpiozero
 
from adafruit_rgb_display.rgb import color565
import adafruit_rgb_display.st7789 as st7789
 
# Up and Down Buttons
btnUp = gpiozero.Button(23)
btnDown = gpiozero.Button(24)

# Configuration for CS and DC pins for Raspberry Pi
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = None
BAUDRATE = 24000000  # The pi can be very fast!
# Create the ST7789 display:
display = st7789.ST7789(
    board.SPI(),
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=BAUDRATE,
    width=135,
    height=240,
    x_offset=53,
    y_offset=40,
    rotation=90
)

width = 240
height = 135

def clear():
    draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
    display.image(image)
