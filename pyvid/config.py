import yaml

class config:
    def __init__(self, path):
          configFile = open(path)
          self.config = yaml.load(configFile);

    def input(self):

          return self.config['video']['input']

    def output(self):
          return self.config['video']['output']
