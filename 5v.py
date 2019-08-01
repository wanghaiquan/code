# coding=utf-8
# 导入 GPIO 库
import RPi.GPIO as GPIO

import time

PORT = 26


def reset():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(PORT, GPIO.IN)


def initcontroller():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(PORT, GPIO.OUT)
    GPIO.output(PORT, True)


def opendoor():
    GPIO.setup(PORT, GPIO.OUT)
    GPIO.output(PORT, False)
    time.sleep(2)
    GPIO.output(PORT, True)


def destroy():
    pass


if __name__ == "__main__":
    try:
        initcontroller()
        opendoor()
        while True:
            pass
    except KeyboardInterrupt:
        destroy()
