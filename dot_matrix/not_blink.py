#-*- coding: utf-8 -*-
import max7219.led as led
import time

device = led.matrix()

for i in range(8):
    for j in range(8):
        device.pixel(j, i, 1)
        time.sleep(0.2)
