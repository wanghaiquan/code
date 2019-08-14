#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'code')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from waveshare_epd import epd2in9bc
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

logging.basicConfig(level=logging.DEBUG)

try:

    logging.info(picdir)
    logging.info("epd2in9bc Demo")

    epd = epd2in9bc.EPD()
    logging.info("init and Clear")
    epd.init()
    epd.Clear()
    time.sleep(1)

    # Drawing on the image
    logging.info("Drawing")
    font24 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 24)
    font18 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 14)
    font16 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 16)
    # Drawing on the Horizontal image
    logging.info("1.Drawing on the Horizontal image...")
    HBlackimage = Image.new('1', (epd.height, epd.width), 255)  # 298*126
    HRYimage = Image.new('1', (epd.height, epd.width), 255)  # 298*126  ryimage: red or yellow image
    drawblack = ImageDraw.Draw(HBlackimage)
    drawry = ImageDraw.Draw(HRYimage)
    drawblack.text((10, 30), u'makers space', font = font16, fill = 0)
    drawblack.text((180, 10), u'想法、行动、创造', font = font18, fill = 0)
    drawblack.text((10, 0), u'少儿创客空间', font = font24, fill = 0)
    drawblack.line((20, 50, 70, 100), fill = 0)
    drawblack.line((70, 50, 20, 100), fill = 0)
    drawblack.rectangle((20, 50, 70, 100), outline = 0)
    drawry.line((165, 50, 165, 100), fill = 0)
    drawry.line((140, 75, 190, 75), fill = 0)
    drawry.arc((140, 50, 190, 100), 0, 360, fill = 0)
    drawry.rectangle((80, 50, 130, 100), fill = 0)
    drawry.chord((200, 50, 250, 100), 0, 360, fill = 0)
    epd.display(epd.getbuffer(HBlackimage), epd.getbuffer(HRYimage))
    time.sleep(2)
    logging.info("Goto Sleep...")
    epd.sleep()

except IOError as e:
    logging.info(e)

except KeyboardInterrupt:
    logging.info("ctrl + c:")
    epd2in9bc.epdconfig.module_exit()
    exit()
