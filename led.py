#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

REDPIN = 11
GREENPIN = 12
pins = (REDPIN, GREENPIN)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pins, GPIO.OUT)
GPIO.output(pins, GPIO.LOW)


def Red(duration):
    GPIO.output(REDPIN, GPIO.HIGH)
    time.sleep(duration)
    GPIO.output(REDPIN, GPIO.LOW)


def Green(duration):
    GPIO.output(GREENPIN, GPIO.HIGH)
    time.sleep(duration)
    GPIO.output(GREENPIN, GPIO.LOW)


Red(5)
Green(5)
GPIO.cleanup()
