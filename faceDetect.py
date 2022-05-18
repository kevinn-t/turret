import cv2 as cv
import numpy
import pyfirmata as ard
import time

# arduino setup
board = ard.Arduino('COM3')
it = ard.util.Iterator(board)
it.start()
servox = board.get_pin('d:3:s')
servoy = board.get_pin('d:5:s')
servox.write(90)
servox.write(0)
# opencv setup
capture = cv.VideoCapture(0)
haar_cascade = cv.CascadeClassifier('haarFace.xml')

while True:
    # face detection
    isTrue, frame = capture.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=6)
    # face labeling
    for (x, y, w, h) in faces_rect:
        cv.rectangle(gray, (x,y), (x+w,y+h), (255,0,0), thickness=2)
        if  x+w/2 > 400:
            servox.write(60)
            break
        elif (x+w/2 < 400) & (x+w/2 > 200):
            servox.write(90)
            break
        else:
            servox.write(135)
            break

        if y+h/2 < 167:
            servoy.write(45)
        elif (y+h/2 > 167) & (y+h/2 < 334):
            servoy.write(0)
        else:
            servoy.write(-45)
    cv.imshow('faces', gray)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()
cv.waitKey(0)