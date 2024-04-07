#!/usr/bin/python3
# File name   : findline.py
# Description : line tracking 
# Website     : www.adeept.com
# E-mail      : support@adeept.com
# Author      : William
# Date        : 2019/02/23
import RPi.GPIO as GPIO
import time
import move
import LED
from rpi_ws281x import *

'''
status     = 1          #Motor rotation
forward    = 1          #Motor forward
backward   = 0          #Motor backward

left_spd   = num_import_int('E_M1:')         #Speed of the car
right_spd  = num_import_int('E_M2:')         #Speed of the car
left       = num_import_int('E_T1:')         #Motor Left
right      = num_import_int('E_T2:')         #Motor Right
'''
line_pin_right = 19
line_pin_middle = 16
line_pin_left = 20
'''
left_R = 15
left_G = 16
left_B = 18

right_R = 19
right_G = 21
right_B = 22

on  = GPIO.LOW
off = GPIO.HIGH

spd_ad_1 = 1
spd_ad_2 = 1
'''
def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(line_pin_right,GPIO.IN)
    GPIO.setup(line_pin_middle,GPIO.IN)
    GPIO.setup(line_pin_left,GPIO.IN)
    #motor.setup()

def run():
    status_right = GPIO.input(line_pin_right)
    status_middle = GPIO.input(line_pin_middle)
    status_left = GPIO.input(line_pin_left)
    print('R%d   M%d   L%d\r'%(status_right,status_middle,status_left))
    if status_middle == 1:
        move.move(70, 'forward', 'no', 1)
    elif status_left == 1:
        move.move(70, 'no', 'right', 1)
    elif status_right == 1:
        move.move(70, 'no', 'left', 1)
    else:
        move.move(70, 'backward', 'no', 1)

    time.sleep(0.2)

if __name__ == '__main__':
    led = LED.LED()
    try:
        led.colorWipe(Color(0,0,0))
#        led.colorWipe(Color(255,255,255))
    except:
        led.colorWipe(Color(0,0,0))

    try:
        setup()
        move.setup()
        while 1:
            run()
#            time.sleep(1.0)
        pass
    except KeyboardInterrupt:
        move.destroy()
