#!/usr/bin/env python
# encoding: utf-8

import RPi.GPIO as GPIO
import time

# 指定GPIO口的选定模式为GPIO引脚编号模式（而非主板编号模式）
GPIO.setmode(GPIO.BCM)

# 指定GPIO14（就是LED长针连接的GPIO针脚）的模式为输出模式
# 如果上面GPIO口的选定模式指定为主板模式的话，这里就应该指定8号而不是14号。
GPIO.setup(17, GPIO.OUT)

# 让GPIO14输出低电平（风扇启动）
GPIO.output(17, False)

# 最后清理GPIO口,清理完毕后就没有电位了（不做也可以，建议每次程序结束时清理一下，好习惯）
# GPIO.cleanup()
