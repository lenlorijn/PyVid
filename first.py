import sys
import cv
import datetime

capture = cv.CaptureFromCAM(1)
cv.SetCaptureProperty(capture, cv.CV_CAP_PROP_FRAME_WIDTH, 1080)
cv.SetCaptureProperty(capture, cv.CV_CAP_PROP_FRAME_HEIGHT, 1920)

if not capture:
  print "Error opening capture device"
  sys.exit(1)

while 1:
  frame = cv.QueryFrame(capture)
  if frame is None:
    break

  
  formated_string = datetime.datetime.now().strftime("%Y-%m-%d-%H%MZ-%f")

  cv.SaveImage("pics/"+formated_string+".jpg",frame)


