import configparser
import os
import urllib.request

def install_python(python_path: str) -> None:
    urlreq = urllib.request.urlopen(python_path)
    with open(r'files\install\install-python.exe', 'w') as file:
        file.buffer.write(urlreq.read())
#TODO Check to see that python is not installed

config = configparser.ConfigParser()
config.read(r'files\install\config.ini')

python_path = config['DEFAULT']['pythonInstallExeUrl']
install_python(python_path)