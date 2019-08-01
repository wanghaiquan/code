# -*- coding: utf-8 -*-
from lib.google_home_led_pattern import GoogleHomeLedPattern
from lib.alexa_led_pattern import AlexaLedPattern
from lib.pixels import Pixels, pixels
from snowboy import snowboydecoder
import sys
import os
# __file__获取执行文件相对路径，整行为取上一级的上一级目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)


def detected_callback():
    print "收到了...."


detector = snowboydecoder.HotwordDetector(
    "yingzi.pmdl", sensitivity=0.5, audio_gain=1)
detector.start(detected_callback)
