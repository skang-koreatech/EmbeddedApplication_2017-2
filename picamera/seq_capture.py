import time
import picamera

i = 0
with picamera.PiCamera() as camera:
	camera.resolution = (1024, 768)
	camera.start_preview()
	time.sleep(2)
	for filename in camera.capture_continuous('img{counter:03d}.jpg'):
		print("Captured %s" % filename)
		time.sleep(5)
		i = i + 1
		if i == 10:
			break

