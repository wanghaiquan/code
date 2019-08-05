#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
import RPi.GPIO as GPIO
import Adafruit_DHT
import lcd1602 as LCD1602
import redis
# set BCM_GPIO 17 as relay pin
RelayPin = 17
# 温控 pin
HumidityPin = 26
# print message at the begining ---custom function
r = redis.Redis(host='192.168.1.4', port=6379, db=0)


def print_message():
    print ('Program is running...')
    print ('Please press Ctrl+C to end the program...')
    print ('\n')


def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(RelayPin, GPIO.OUT)
    LCD1602.init(0x27, 1)  # init(slave address, background light)
    LCD1602.write(0, 0, '       HI       ')
    LCD1602.write(1, 1, '  wanghaiquan  ')
    time.sleep(2)

# 求当前温湿度


def get_humidity():
    sensor = Adafruit_DHT.DHT11
    humidity, temperature = Adafruit_DHT.read_retry(sensor, HumidityPin)
    return humidity, temperature


def main():
    # print info
    print_message()
    while True:
        queue = r.brpop('button', 1)
        humidity, temperature = get_humidity()
        LCD1602.clear()
        # print humidity, temperature
        LCD1602.write(0, 0, ' F:{0:0.1f} C'.format(temperature))
        LCD1602.write(1, 1, 'H:{0:0.1f} %'.format(humidity))
        if queue is not None:
            GPIO.output(RelayPin, True)
            print int(humidity)
            time.sleep(5)
        # 温度大于90给电压
        # if int(humidity) >= 80 or queue is not None:
        #     GPIO.output(RelayPin, True)
        #     print int(humidity)
        #
        # else:
        #     GPIO.output(RelayPin, False)
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
