import RPi.GPIO as GPIO
import time
import cv2
import datetime
import io

from google.cloud import vision
from google.cloud.vision import types

GPIO.setmode(GPIO.BCM)

GPIO.setup(12, GPIO.IN, GPIO.PUD_UP)

cam = cv2.VideoCapture(0)

def button():
    state = False
    if GPIO.input(12) == 0:
        state = True
        print("button press")
    return state

def camera():
    try:
        while True:
            ret, img = cam.read()
            cv2.imshow('Cam', img)
            
            key = cv2.waitKey(10)
            if key == 27:
            	cam.release()
            	cv2.destroyAllWindows()
            	GPIO.cleanup()
            	break

            if button() == True:
                filename = getDatetime() + '.jpg'
                cv2.imwrite(filename , img)
                time.sleep(0.5)
                detect_label(filename)
		
    except KeyboardInterrupt:
        cam.release()
        cv2.destroyAllWindows()
        GPIO.cleanup()

def getDatetime():
    date = datetime.datetime.now()
    year = str(date.year)
    month = str(date.month)
    day = str(date.day)
    hour = str(date.hour)
    min = str(date.minute)
    sec = str(date.second)

    if int(month) < 10:
        month = '0' + month
    if int(day) < 10:
        day = '0' + day
    if int(hour) < 10:
        hour = '0' + hour
    if int(min) < 10:
        min = '0' + min

    t =  year + month + day + hour + min + sec

    return t

def detect_label(path):
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    response = client.label_detection(image=image)
    labels = response.label_annotations
    print("Labels: ")

    for label in labels:
        print(label.description)


if __name__ == '__main__':
    camera()
