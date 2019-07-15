import RPi.GPIO as gpio
import time
gpio.setmode(gpio.BCM)
gpio.setup(18, gpio.OUT)
pwm_led = gpio.PWM(18, 500)
pwm_led.start(0)
print 'pwm start'
try:
    while True:
        for i in range(0, 100):
            pwm_led.ChangeDutyCycle(i)
            time.sleep(0.05)
        for i in range(100, 0):
            pwm_led.ChangeDutyCycle(i)
            time.sleep(0.05)
except KeyboardInterrupt:
    pwm_led.stop()
    gpio.cleanup()
    print 'pwm stop and gpio clean up by ctrl + c'
