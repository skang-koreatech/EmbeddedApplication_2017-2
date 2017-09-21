import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)
gpio.setup(4, gpio.IN)

def motionSensing():
    while True:
        try:
            print("...")
            if gpio.input(4) == 1:
                print("motion detected!!")
                time.sleep(0.5)
            else:
                print("nobody here")
                time.sleep(0.5)
        except KeyboardInterrupt:
            gpio.cleanup()

print("motion detector ready")
motionSensing()
