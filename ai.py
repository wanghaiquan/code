# -*- coding: utf-8 -*-
import time
from snowboy import snowboydecoder
from pixels import Pixels, pixels
from alexa_led_pattern import AlexaLedPattern
from google_home_led_pattern import GoogleHomeLedPattern


def detected_callback():
    print "收到了...."

    pixels.wakeup()
    time.sleep(3)
    pixels.off()


if __name__ == '__main__':
    pixels.pattern = GoogleHomeLedPattern(show=pixels.show)
    detector = snowboydecoder.HotwordDetector(
        "yingzi.pmdl", sensitivity=0.5, audio_gain=1)
    detector.start(detected_callback)
