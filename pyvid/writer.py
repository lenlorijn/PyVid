import cv2 as cv
      fourcc = cv.cv.CV_FOURCC('X','V','I','D')
#@TODO config
      formated_date = datetime.datetime.now().strftime("%Y-%m-%d-%H%M-%f")

#@TODO config and on event? And should renew when finishing old file? Place in if statement?
      out = cv.VideoWriter(outputConfig['dir'] + formated_date + outputConfig['extension'], fourcc, 20.0, (640,480))


