import configparser
import os
import sys

def getConfig(filename):
	config = configparser.ConfigParser()
	config.read([filename, os.path.expanduser('~/.jarmanifest.cfg')])
	return config

config = getConfig(sys.exec_prefix + '/jarmanifest.cfg')
