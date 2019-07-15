import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)

p1 = GPIO.PWM(11, 100)
p2 = GPIO.PWM(12, 100)
p1.start(0)
p2.start(0)

try:
    while True:
        for dc in range(0, 101, 5):
            p1.ChangeDutyCycle(dc)
            p2.ChangeDutyCycle(dc)
            time.sleep(0.1)
        for dc in range(100, -1, -5):
            p1.ChangeDutyCycle(dc)
            p2.ChangeDutyCycle(dc)
            time.sleep(0.1)
except KeyboardInterrupt:
    pass

p1.stop()
p2.stop()
GPIO.cleanup()
