
from flask import Flask, request
from flask import render_template
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

app = Flask(__name__)

leds = {
        23: {'name' : 'Red LED', 'state' : GPIO.LOW},
        24: {'name' : 'Yellow LED', 'state' : GPIO.LOW},
        25: {'name' : 'Green LED', 'state' : GPIO.LOW},
}

for led in leds:
        GPIO.setup(led, GPIO.OUT)
        GPIO.output(led, GPIO.LOW)

def getGpioState():
        for led in leds:
                leds[led]['state'] = GPIO.input(led)

        return leds

@app.route("/")
def main():
        gpioState = {
                'leds' : getGpioState()
        }
        return render_template('main.html', **gpioState)

@app.route("/<led>/<act>")
def action(led, act):
        led = int(led)
        leds = getGpioState()
        dev = leds[led]['name']

        if act == "on":
                GPIO.output(led, GPIO.HIGH)
                msg = "Turned " + dev + " on."
        elif act == "off":
                GPIO.output(led, GPIO.LOW)
                msg = "Turned " + dev + " off."
        elif act == "toggle":
                GPIO.output(led, not GPIO.input(led))
                msg = "Toggled " + dev + "."
        else:
                msg = "Undefined action!"

        gpioState = {
                'msg' : msg,
                'leds' : getGpioState()
        }
        return render_template('main.html', **gpioState)

if __name__ == "__main__":
        app.run(host='192.168.0.13', port=8888, debug = True)
