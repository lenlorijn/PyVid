import sys
import cv2 as cv
import datetime

capture = cv.VideoCapture(1)

fourcc = cv.cv.CV_FOURCC('X','V','I','D')


formated_string = datetime.datetime.now().strftime("%Y-%m-%d-%H%M-%f")


out = cv.VideoWriter(formated_string + '.avi', fourcc, 20.0, (640,480))

while(capture.isOpened()):
  ret, frame = capture.read()
  if ret==True:
    out.write(frame)
  else:
    break
