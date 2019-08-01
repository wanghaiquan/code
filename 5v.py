#!/usr/bin/python
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time
from pixels import Pixels, pixels
from alexa_led_pattern import AlexaLedPattern
from google_home_led_pattern import GoogleHomeLedPattern
# set BCM_GPIO 17 as relay pin
RelayPin = 17
# print message at the begining ---custom function


def print_message():
    print ('Program is running...')
    print ('Please press Ctrl+C to end the program...')
    print ('\n')


def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(RelayPin, GPIO.OUT)


def main():
    #print info
    print_message()
    while True:
        print ('|******************|')
        print ('|  ...关闭电源  |')
        print ('|******************|\n')

        # disconnect
        pixels.off()
        # GPIO.output(RelayPin, GPIO.LOW)
        GPIO.output(RelayPin, False)
        time.sleep(10)

        print ('|*****************|')
        print ('|  打开电源...  |')
        print ('|*****************|\n')
        print ('')
        # connect
        pixels.think()
        # GPIO.output(RelayPin, GPIO.HIGH)
        GPIO.output(RelayPin, True)
        time.sleep(2)


def destroy():
    # turn off relay
    # GPIO.output(RelayPin, GPIO.LOW)
    GPIO.output(RelayPin, False)
    # release resource
    GPIO.cleanup()


#
# if run this script directly ,do:
if __name__ == '__main__':
    setup()
    try:
        main()
    except KeyboardInterrupt:
        destroy()
