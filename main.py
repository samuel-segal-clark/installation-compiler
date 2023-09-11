import configparser
import os

config = configparser.ConfigParser()
config.read(u'files\install\config.ini')

python_path = config['DEFAULT']['pythonInstallExeUrl']

