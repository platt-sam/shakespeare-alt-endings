import app
import os
import sys
from os import path

def setup():
    if len(sys.argv) <= 1:
        print("User has not specified an operating system. Please rerun program as:\tpython3 main.py [linux / mac / windows]\n")
        exit()
    operatingsystem = sys.argv[1]
    cmd = ""
    if operatingsystem == 'linux':
        cmd = "pip3 install -r requirements-linux.txt"
    elif operatingsystem in ['mac', 'windows']:
        cmd = "pip3 install -r requirements.txt"
    else:
        print("Operating System not recognized")
        exit()
    print("Installing required packages...")
    os.system(cmd)

def main():
    setup()
    app.app()

if __name__ == "__main__":
    main()