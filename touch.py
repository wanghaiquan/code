#!/usr/bin/python
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time
import os

# sensor pin define
touch   = 18
buzzer  = 24


def init():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(buzzer, GPIO.OUT)
    GPIO.setup(touch, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    pass


# turn on buzzer
def buzzer_on():
    GPIO.output(buzzer, GPIO.HIGH)
    time.sleep(0.2)
    pass
# turn off buzzer


def buzzer_off():
    GPIO.output(buzzer, GPIO.LOW)
    pass


# read digital touch sensor
button_touch = False

def read_touchsensor():
    touchstatus = GPIO.input(touch)  #   按住  0  不按 1

    if (touchstatus == False ):
        if (button_touch == False):
            buzzer_on()
            button_touch == True
        else:
            buzzer_off()
            button_touch == False


    pass
    #
    # if (button_touch == True):
    #     buzzer_on()
    #     button_touch  = True
    #     print "已触摸"
    #
    #
    # else:
    #     buzzer_off()
    #     button_touch = False
    #     print "未触摸"



# main loop
def main():
    print"...................................................................System initializing..."
    init()
    buzzer_off()
    # relay_off()
    print"...................................................................Ok"
    print"...................................................................Please touch"
    print"\n"
    while True:
        read_touchsensor()


if __name__ == '__main__':
    try:
        main()
        pass
    except KeyboardInterrupt:
        pass
    pass
GPIO.cleanup()
