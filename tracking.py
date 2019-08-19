# -*- coding:UTF-8 -*-
import RPi.GPIO as GPIO
from lib.steering import Steering
import time

# 小车电机引脚定义
IN1 = 20
IN2 = 21
IN3 = 19
IN4 = 26
ENA = 16
ENB = 13

# 超声波感应器
TRIG = 23
ECHO = 22
# 小车按键定义
key = 8

# 循迹红外引脚定义
# TrackSensorLeftPin1 TrackSensorLeftPin2 TrackSensorRightPin1 TrackSensorRightPin2
#      3                 5                  4                   18
TrackSensorLeftPin1 = 3  # 定义左边第一个循迹红外传感器引脚为3口
TrackSensorLeftPin2 = 5  # 定义左边第二个循迹红外传感器引脚为5口
TrackSensorRightPin1 = 4  # 定义右边第一个循迹红外传感器引脚为4口
TrackSensorRightPin2 = 18  # 定义右边第二个循迹红外传感器引脚为18口

# 设置GPIO口为BCM编码方式
GPIO.setmode(GPIO.BCM)

# 忽略警告信息
GPIO.setwarnings(False)

# 电机引脚初始化为输出模式
# 按键引脚初始化为输入模式
# 寻迹引脚初始化为输入模式


def init():
    global pwm_ENA
    global pwm_ENB
    global steering
    GPIO.setup(ENA, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(IN1, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(IN2, GPIO.OUT, initial=GPIO.LOW)
    # GPIO.setup(ENB, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(IN3, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(IN4, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(key, GPIO.IN)
    GPIO.setup(TrackSensorLeftPin1, GPIO.IN)
    GPIO.setup(TrackSensorLeftPin2, GPIO.IN)
    GPIO.setup(TrackSensorRightPin1, GPIO.IN)
    GPIO.setup(TrackSensorRightPin2, GPIO.IN)
    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)
    # 设置pwm引脚和频率为50hz
    pwm_ENA = GPIO.PWM(ENA, 50)
    # 舵机
    steering = Steering(ENB,20,20)
    steering.setup()

    # pwm_ENB = GPIO.PWM(ENB, 50)
    pwm_ENA.start(0)
    # pwm_ENB.start(0)

# 测距


def send_trigger_pulse():
    GPIO.output(TRIG, True)
    time.sleep(0.0001)
    GPIO.output(TRIG, False)


def wait_for_echo(value, timeout):
    count = timeout
    while GPIO.input(ECHO) != value and count > 0:
        count = count - 1


def distance():
    send_trigger_pulse()
    wait_for_echo(True, 10000)
    start = time.time()
    wait_for_echo(False, 10000)
    finish = time.time()
    pulse_len = finish - start
    distance_cm = pulse_len / 0.000058
    return distance_cm


# 小车前进


def run(leftspeed, rightspeed):
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    # pwm_frequency(leftspeed,rightspeed)
    pwm_ENA.ChangeDutyCycle(leftspeed)
    # pwm_ENB.ChangeDutyCycle(rightspeed)
# 小车后退


def back(leftspeed, rightspeed):
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)
    pwm_ENA.ChangeDutyCycle(leftspeed)
    # pwm_ENB.ChangeDutyCycle(rightspeed)

# 小车左转


def left(leftspeed, rightspeed):
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    pwm_ENA.ChangeDutyCycle(leftspeed)
    steering.left()
    time.sleep(0.2)
    # steering.cleanup()
    # pwm_ENB.ChangeDutyCycle(rightspeed)

# 小车右转


def right(leftspeed, rightspeed):
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)
    pwm_ENA.ChangeDutyCycle(leftspeed)
    steering.right()
    time.sleep(0.2)
    # steering.cleanup()
    # pwm_ENB.ChangeDutyCycle(rightspeed)

# 小车原地左转


def spin_left(leftspeed, rightspeed):
    # GPIO.output(IN1, GPIO.LOW)
    # GPIO.output(IN2, GPIO.HIGH)
    # GPIO.output(IN3, GPIO.HIGH)
    # GPIO.output(IN4, GPIO.LOW)
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)
    pwm_ENA.ChangeDutyCycle(leftspeed)
    # pwm_ENB.ChangeDutyCycle(rightspeed)

# 小车原地右转


def spin_right(leftspeed, rightspeed):
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)
    pwm_ENA.ChangeDutyCycle(leftspeed)
    # pwm_ENB.ChangeDutyCycle(rightspeed)

# 小车停止


def brake():
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.LOW)

# 按键检测


def key_scan():
    while GPIO.input(key):
        pass
    while not GPIO.input(key):
        time.sleep(0.01)
        if not GPIO.input(key):
            time.sleep(0.01)
            while not GPIO.input(key):
                pass


# 延时2s
time.sleep(2)

# try/except语句用来检测try语句块中的错误，
# 从而让except语句捕获异常信息并处理。
try:
    init()
    # key_scan()
    while True:
        print("cm = %f" % distance())
        dis = int(distance())

        # 检测到黑线时循迹模块相应的指示灯亮，端口电平为LOW
        # 未检测到黑线时循迹模块相应的指示灯灭，端口电平为HIGH
        TrackSensorLeftValue1 = GPIO.input(TrackSensorLeftPin1)
        TrackSensorLeftValue2 = GPIO.input(TrackSensorLeftPin2)
        TrackSensorRightValue1 = GPIO.input(TrackSensorRightPin1)
        TrackSensorRightValue2 = GPIO.input(TrackSensorRightPin2)

        print TrackSensorLeftValue1, TrackSensorLeftValue2, TrackSensorRightValue1, TrackSensorRightValue2
        # 处理未发现黑线
        # 1 1 1 1
        if TrackSensorLeftValue1 == True and TrackSensorLeftValue2 == True and TrackSensorRightValue1 == True and  TrackSensorRightValue2 == True :
            print 'stop'
            brake()
        # 处理距离 小车后退
        elif dis < 10:
            print 'back'
            back(50, 0)
        # 右拐
        # 0 0 1 0

        elif TrackSensorLeftValue1 == False and TrackSensorLeftValue2 == False and TrackSensorRightValue1 == True and TrackSensorRightValue2 == False:
            print 'right'
            right(0,75)
        # 左拐
        # 0 1 0 0
        elif TrackSensorLeftValue1 == False and TrackSensorLeftValue2 == True and TrackSensorRightValue1 == False and TrackSensorRightValue2 == False:
            print 'left'
            left(0,75)
        # 处理电机前进
        # 0 1 1 0
        elif TrackSensorLeftValue2 == True and TrackSensorRightValue1 == True:
            print 'run'
            run(50, 0)

except KeyboardInterrupt:
    pass
pwm_ENA.stop()
# pwm_ENB.stop()
GPIO.cleanup()
