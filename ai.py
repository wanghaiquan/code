# -*- coding: utf-8 -*-
from snowboy import snowboydecoder
from lib.pixels import Pixels, pixels
from lib.alexa_led_pattern import AlexaLedPattern
from lib.google_home_led_pattern import GoogleHomeLedPattern


def detected_callback():
    print "收到了...."


detector = snowboydecoder.HotwordDetector(
    "yingzi.pmdl", sensitivity=0.5, audio_gain=1)
detector.start(detected_callback)
