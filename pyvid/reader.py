import cv2 as cv
import config as config
import datetime

class reader:

    def capture(self, camera, name):
        print "Recording " + name

        outputConfig = config.config("../config.yml").output()
        capture = cv.VideoCapture(camera)

        fourcc = cv.cv.CV_FOURCC('X','V','I','D')
        #@TODO config
        formated_date = datetime.datetime.now().strftime("%Y-%m-%d-%H%M-%f")

        #@TODO config and on event? And should renew when finishing old file? Place in if statement?
        out = cv.VideoWriter(outputConfig['dir'] + formated_date + outputConfig['extension'], fourcc, 20.0, (640,480))

        while(capture.isOpened()):

            ret, frame = capture.read() #@TODO frame object? olding time and id info?

            if ret==True:

                #@TODO config
                date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
                cv.putText(frame, date, (320,470), cv.FONT_HERSHEY_PLAIN, 1, 1855)

                #@TODO observe on frame event
                out.write(frame) 

                cv.imshow('frame', frame)
                cv.waitKey(10);
                #observe frame event
