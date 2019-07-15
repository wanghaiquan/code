import RPi.GPIO as GPIO
import time

LED_R = 21
LED_G = 12

GPIO.setmode(GPIO.BCM)

GPIO.setup(LED_R, GPIO.OUT)
GPIO.setup(LED_G, GPIO.OUT)

pwm_r = GPIO.PWM(LED_R, 2000)
pwm_g = GPIO.PWM(LED_G, 2000)

GPIO.output(LED_R, GPIO.LOW)
GPIO.output(LED_G, GPIO.LOW)

pwm_r.start(0)
pwm_g.start(100)


if __name__ == "__main__":
    try:
        while True:
            for i in range(100):
                pwm_r.ChangeDutyCycle(i)
                pwm_g.ChangeDutyCycle(100 - i)
                time.sleep(.25)

            for i in range(100):
                pwm_r.ChangeDutyCycle(100 - i)
                pwm_g.ChangeDutyCycle(i)
                time.sleep(.25)
    except KeyboardInterrupt:
        pwm_r.stop()
        pwm_g.stop()
        GPIO.cleanup()
        exit(6)
