import os
import sys
import configparser

class configuration():
    def __init__(self, path):
        self.path = path

    def getconfig(self, key, value):
        config = configparser.ConfigParser()
        configPath = os.path.join(self.path, "config", "config.conf")
        config.read(configPath)
        return config[key][value]
