# -*- coding: utf-8 -*-
from snowboy import snowboydecoder


def detected_callback():
    print "收到了...."


detector = snowboydecoder.HotwordDetector(
    "yingzi.pmdl", sensitivity=0.5, audio_gain=1)
detector.start(detected_callback)
