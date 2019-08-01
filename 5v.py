#!/usr/bin/env python
# encoding: utf-8

import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

num = 17  # 树莓派针脚编号

GPIO.setup(num, GPIO.OUT)
id = GPIO.input(num)

if (id == 1):
    GPIO.output(num, GPIO.LOW)
    print "已打开设备"
if (id == 0):
    GPIO.output(num, GPIO.HIGH)
    print "已关闭设备"
GPIO.cleanup()
