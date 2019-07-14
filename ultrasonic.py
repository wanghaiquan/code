# coding=utf-8
#!/usr/bin/env python
import RPi.GPIO as GPIO
import logging as LOG
import math
import time
TRIG = 11
ECHO = 12


def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)


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
        dis = distance()
        LOG.debug("距离还剩: %s" % dis)
        exactDis = int(dis)
        if (exactDis == 3):
            print '马上要装上了', dis, 'cm'
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
