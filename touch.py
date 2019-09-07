#!/usr/bin/python
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time
import os

# sensor pin define
touch = 18



def init():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(touch, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    pass

# read digital touch sensor


def read_touchsensor():
    touchstatus = GPIO.input(touch)
    if (touchstatus == True):
        print"Turn on relay"

    else:
        print"Turn off relay"
    pass


# main loop
def main():
    print"...................................................................System initializing..."
    init()
    # buzzer_off()
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
