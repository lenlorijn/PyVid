import sys
import yaml
import cv2 as cv
import datetime

def main():
  print "Running pyvid"
#CONFIG @TODO should become object
  configFile = open('config/main.yml')
  config = yaml.load(configFile);

#Subscribe events/load modules

  outputConfig = config['video']['output']
  inputConfig = config['video']['input']

#@TODO foreach input
#VIDEO CAPTURE
  capture = cv.VideoCapture(0)

#@TODO config
  fourcc = cv.cv.CV_FOURCC('X','V','I','D')

#@TODO config
  formated_date = datetime.datetime.now().strftime("%Y-%m-%d-%H%M-%f")

#@TODO config and on event? And should renew when finishing old file? Place in if statement?
  out = cv.VideoWriter(outputConfig['dir'] + formated_date + outputConfig['extension'], fourcc, 20.0, (640,480))

#@TODO fire appropriate events, construct/destruct?
  while(capture.isOpened()):

    ret, frame = capture.read() #@TODO frame object? olding time and id info?

    if ret==True:

      #@TODO config
      date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
      cv.putText(frame, date, (320,470), cv.FONT_HERSHEY_PLAIN, 1, 1855)

      #@TODO observe on frame event
      out.write(frame) 

      #observe frame event
      #cv.imshow('frame', frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
      break

if __name__ == "__main__":
  print "Running pyvid"
  main()
