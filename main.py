import configparser
import os
import urllib.request

#TODO Ensure this works in Pyinstaller
def system_has_python() -> bool:
    try:
        out = os.system('python --version')
        return out == 0
    except:
        return False

def install_python_exe(python_path: str) -> None:
    urlreq = urllib.request.urlopen(python_path)
    with open(r'files\install\install-python.exe', 'w') as file:
        file.buffer.write(urlreq.read())

def run_python_exe() -> None:
    os.system(r'files\install\install-python.exe')

def pip_installation() -> None:
    os.system(r'pip install -r files\install\requirements.txt --trusted-host=files.pythonhosted.org')

config = configparser.ConfigParser()
config.read(r'files\install\config.ini')

if not system_has_python():
    print('Installing Python')
    python_path = config['DEFAULT']['pythonInstallExeUrl']
    install_python_exe(python_path)
    run_python_exe()
else:
    print('Python already installed, continuing to pip')

print('Installing pip requirements')
pip_installation()