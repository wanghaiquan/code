#!/usr/bin/env python
import lcd1602 as LCD1602
import time


def setup():
    LCD1602.init(0x27, 1)  # init(slave address, background light)
    LCD1602.write(0, 0, '    haiquan     ')
    LCD1602.write(1, 1, 'Hello, World!')
    time.sleep(2)


def loop():
    space = '                '
    greetings = 'i love u li gui ying! thank u for your company.^_^'
    greetings = space + greetings
    while True:
        tmp = greetings
        for i in range(0, len(greetings)):
            LCD1602.write(0, 0, tmp)
            tmp = tmp[1:]
            time.sleep(0.3)
            LCD1602.clear()


def destroy():
    pass


if __name__ == "__main__":
    try:
        setup()
        loop()
        while True:
            pass
    except KeyboardInterrupt:
        destroy()
