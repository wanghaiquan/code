# coding=utf-8
#!/usr/bin/env python
import RPi.GPIO as GPIO
import logging as LOG
import lcd1602 as LCD1602
from datetime import *
import math
import time
TRIG = 11
ECHO = 12


def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)
    LCD1602.init(0x27, 1)  # init(slave address, background light)
    LCD1602.write(0, 0, '    haiquan     ')
    LCD1602.write(1, 1, '   distance')


def distance():
    GPIO.output(TRIG, 0)
    time.sleep(0.000002)
    GPIO.output(TRIG, 1)
    time.sleep(0.00001)
    GPIO.output(TRIG, 0)
    while GPIO.input(ECHO) == 0:
        a = 0
        time1 = time.time()
    while GPIO.input(ECHO) == 1:
        a = 1
        time2 = time.time()
        during = time2 - time1
    return during * 340 / 2 * 100

# 当距离在2cm范围内，发送一条短信，告知垃圾满了


def loop():
    while True:
        LCD1602.clear()
        get_time_now = datetime.now().strftime('   %H:%M:%S')

        dis = distance()
        LOG.debug("距离还剩: %s" % dis)
        exactDis = int(dis)
        if (exactDis == 2):
            print '马上要撞上了', dis, 'cm'
            LCD1602.write(0, 0,  str(dis))
            LCD1602.write(1, 1, get_time_now)
        else:
            LCD1602.write(0, 0,  str(dis))
            LCD1602.write(1, 1, get_time_now)
        print '目标距离还剩', dis, 'cm'
        print ''

        time.sleep(0.3)


def destroy():

    GPIO.cleanup()


if __name__ == "__main__":
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
