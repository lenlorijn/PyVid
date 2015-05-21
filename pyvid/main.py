import sys
import yaml
import config as config
import reader as reader
import multiprocessing

inputConfig = config.config("../config.yml").input()

def record(camera, name):
    reader.reader().capture(camera, name)

def main():

      cameras = inputConfig['cameras']
      print cameras

      for name, camera in cameras.items():
          print name
          print camera
          print "Making camera process for camera "+name
          recordingProcess = multiprocessing.Process(target=record , args=(camera,name,))
          recordingProcess.start()

if __name__ == "__main__":
  print "Running pyvid"
  main()
