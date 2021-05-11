from pitft_setup import *
import gpiozero
import os
import time

pixel_size = 10

width = 135
height = 240
x = 0
y = 0

btnUp = gpiozero.Button(23)
btnDown = gpiozero.Button(24)

black = color565(0,0,0)
white = color565(255,255,255)

def drawPixel(x,y,color):
    display.fill_rectangle(x,y,pixel_size,pixel_size,color)

display.fill(black)
drawPixel(x,y,white)

while 1:
    if btnUp.is_pressed:
        drawPixel(x,y,black)
        if btnDown.is_pressed:
            print("left")
            y = y+pixel_size if y<height-pixel_size else 0
            drawPixel(x,y,white)
        else:
            print("up")
            x = x-pixel_size if x>0 else width-pixel_size
            drawPixel(x,y,white)
    elif btnDown.is_pressed:
        drawPixel(x,y,black)
        if btnUp.is_pressed:
            print("right")
        else:
            print("down")
            x = x+pixel_size if x<width-pixel_size else 0
            drawPixel(x,y,white)
