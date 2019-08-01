#!/usr/bin/env python
# encoding: utf-8

import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

num = 17  # 树莓派针脚编号

GPIO.setup(num, GPIO.OUT)
id = GPIO.input(num)

GPIO.output(num, GPIO.LOW)

time.sleep(10)

GPIO.output(num, GPIO.HIGH)

GPIO.cleanup()
