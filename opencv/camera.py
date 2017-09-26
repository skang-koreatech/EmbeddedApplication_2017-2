import cv2

cam = cv2.VideoCapture(0)

while True:
    ret,im = cam.read()
    cv2.imshow('video test',im)
    key = cv2.waitKey(10)
    if key == 120: # ascii code for letter 'x'
        break
    if key == ord(' '):
        cv2.imwrite('capture.jpg',im)
cam.release()
cv2.destroyAllWindows()
