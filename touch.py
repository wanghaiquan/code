#!/usr/bin/python
# -*- coding: utf-8 -*-
import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import time
import os
import json

# sensor pin define
touch = 18
buzzer = 24



def init():


    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(buzzer, GPIO.OUT)
    GPIO.setup(touch, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    pass

# turn on buzzer


def buzzer_on():
    GPIO.output(buzzer, GPIO.HIGH)
    time.sleep(0.2)
    pass
# turn off buzzer


def buzzer_off():
    GPIO.output(buzzer, GPIO.LOW)
    pass


# read digital touch sensor

def read_touchsensor():
    touchstatus = GPIO.input(touch)  #   按住  0  不按 1
    if (touchstatus == False):
        buzzer_on()
        print "已触摸"


    else:
        buzzer_off()
        print "未触摸"

    pass

# mqtt function

def on_connect(mqttc, obj, flags, rc):
    print("rc: "+str(rc))

def on_message(mqttc, obj, msg):
    print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))
    message = json.loads(msg.payload)

    if(message['button'] == 'on'):
        buzzer_on()
    else:
        buzzer_off()

    print(message['button'])

def on_publish(mqttc, obj, mid):
    print("mid: "+str(mid))

def on_subscribe(mqttc, obj, mid, granted_qos):
    print("Subscribed: "+str(mid)+" "+str(granted_qos))

def on_log(mqttc, obj, level, string):
    print(string)
# end



# main loop
def main():
    init()
    print"...................................................................System initializing..."

    mqttc = mqtt.Client(transport="websockets")
    mqttc.on_message = on_message
    mqttc.on_connect = on_connect
    mqttc.on_publish = on_publish
    mqttc.on_subscribe = on_subscribe
    # Uncomment to enable debug messages
    mqttc.on_log = on_log


    mqttc.connect("192.144.190.105", 8083, 60)
    mqttc.subscribe("mqtt/light", 0)



    buzzer_off()
    # relay_off()
    print"...................................................................Ok"
    print"...................................................................Please touch"
    print"\n"

    while True:
        read_touchsensor()
        
    mqttc.loop_forever()

if __name__ == '__main__':
    try:
        main()
        pass
    except KeyboardInterrupt:
        pass
    pass
GPIO.cleanup()
