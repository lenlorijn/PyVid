import sys
import cv2 as cv
import datetime

capture = cv.VideoCapture(0)

fourcc = cv.cv.CV_FOURCC('X','V','I','D')


formated_date = datetime.datetime.now().strftime("%Y-%m-%d-%H%M-%f")


out = cv.VideoWriter(formated_date + '.avi', fourcc, 20.0, (640,480))

while(capture.isOpened()):
  ret, frame = capture.read()
  if ret==True:

    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    cv.putText(frame, date, (320,480), cv.FONT_HERSHEY_PLAIN, 1, 255)

    out.write(frame) 

    cv.imshow('frame', frame)

  if cv.waitKey(1) & 0xFF == ord('q'):
    break
