import sys
import yaml
import cv2 as cv
import datetime

#CONFIG
configFile = open('config/main.yml')
config = yaml.load(configFile);

outputConfig = config['video']['output']
inputConfig = config['video']['input']

#VIDEO CAPTURE
capture = cv.VideoCapture(0)

#config
fourcc = cv.cv.CV_FOURCC('X','V','I','D')

#config
formated_date = datetime.datetime.now().strftime("%Y-%m-%d-%H%M-%f")

#config and on event?
out = cv.VideoWriter(outputConfig['dir'] + formated_date + outputConfig['extension'], fourcc, 20.0, (640,480))

#Make foreach camera input
while(capture.isOpened()):

  ret, frame = capture.read()

  if ret==True:

    #config
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    cv.putText(frame, date, (320,470), cv.FONT_HERSHEY_PLAIN, 1, 1855)

#observe on frame event
    out.write(frame) 

#observe frame event
    cv.imshow('frame', frame)

  if cv.waitKey(1) & 0xFF == ord('q'):
    break
