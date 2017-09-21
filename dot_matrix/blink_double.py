#-*- coding: utf-8 -*-

import max7219.led as led
import time

device = led.matrix(2)
device.show_message("Hello world")

for i in range(16):
    for j in range(16):
        device.pixel(j, i, 1)
        time.sleep(0.2)
        device.pixel(j, i, 0)
        time.sleep(0.2)
