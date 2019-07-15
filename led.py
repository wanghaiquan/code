# coding=utf-8
# 导入 GPIO 库
import RPi.GPIO as GPIO

# 定义用于 LED 的针脚 BCM 编号
LED_R = 16
LED_G = 19

# 设定针脚编号为 BCM 模式
GPIO.setmode(GPIO.BCM)

# 设定 LED 针脚可用于输出
GPIO.setup(LED_R, GPIO.OUT)
GPIO.setup(LED_G, GPIO.OUT)

# 关于 __name__ == "__main__"：
# 如果是直接运行本代码，而不是其他 Python 代码调用本文件的话，则会执行
if __name__ == "__main__":
    try:
        while True:
            # 给两个针脚电压
            GPIO.output(LED_R, GPIO.HIGH)
            GPIO.output(LED_G, GPIO.HIGH)
    except KeyboardInterrupt:
        # 检测到中断信号后，关闭 GPIO 通道以供下次使用
        GPIO.cleanup()
        # 退出返回状态代码 6
        exit(6)
