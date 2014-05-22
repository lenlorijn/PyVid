import sys
import cv2 as cv
import datetime

capture = cv.VideoCapture(1)
capture.set(4,1080)
capture.set(5,1920)

if not capture:
  print "Error opening capture device"
  sys.exit(1)

while 1:
  ret,frame = capture.read()
  if frame is None:
    break 
  
  formated_string = datetime.datetime.now().strftime("%Y-%m-%d-%H%MZ-%f")

  cv.imwrite("pics/"+formated_string+".jpg", frame, [int(cv.IMWRITE_JPEG_QUALITY), 80])


