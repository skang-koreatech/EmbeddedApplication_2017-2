import picamera
import time

with picamera.PiCamera() as camera: # the close() method is automatically called
	camera.resolution = (1024, 768)
        camera.start_preview()
        # Camera warm-up time
        time.sleep(2)
        #camera.capture('foo.jpg')
	camera.capture('foo.jpg', resize=(320,240)) # capturing resized images

#camera = picamera.PiCamera()
#try:
#	camera.resolution = (1024, 768)
#	camera.start_preview()
#	# Camera warm-up time
#	time.sleep(2)
#	camera.capture('foo.jpg')
#finally:
#	camera.close() # You should ensure you call the close() method to release the camera resources


