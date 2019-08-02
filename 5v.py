#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
from google_home_led_pattern import GoogleHomeLedPattern
from alexa_led_pattern import AlexaLedPattern
from pixels import Pixels, pixels
import RPi.GPIO as GPIO
import Adafruit_DHT

# set BCM_GPIO 17 as relay pin
RelayPin = 17
HumidityPin = 26
# print message at the begining ---custom function


def print_message():
    print ('Program is running...')
    print ('Please press Ctrl+C to end the program...')
    print ('\n')


def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(RelayPin, GPIO.OUT)

# 求当前温湿度


def get_humidity():
    sensor = Adafruit_DHT.DHT11
    humidity, temperature = Adafruit_DHT.read_retry(sensor, HumidityPin)
    return humidity, temperature


def main():
    #print info
    print_message()
    while True:
        humidity, temperature = get_humidity()
        print humidity, temperature
    # while True:
    #     print ('|******************|')
    #     print ('|  ...关闭电源  |')
    #     print ('|******************|\n')
    #     humidity, temperature = get_humidity()
    #     print('温度={0:0.1f}°C  湿度={1:0.1f}%'.format(temperature, humidity))
    #     # disconnect
    #     pixels.off()
    #     # GPIO.output(RelayPin, GPIO.LOW)
    #     GPIO.output(RelayPin, False)
    #     time.sleep(2)
    #
    #     print ('|*****************|')
    #     print ('|  打开电源...  |')
    #     print ('|*****************|\n')
    #     print ('')
    #     # connect
    #     pixels.think()
    #     # GPIO.output(RelayPin, GPIO.HIGH)
    #     GPIO.output(RelayPin, True)
    #     time.sleep(1)


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
