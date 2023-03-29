import app
import os
import sys
from os import path

def setup():
    if len(sys.argv) <= 1:
        print("User has not specified an operating system. Please rerun program as:\tpython3 main.py [linux / mac / windows]\n")
        exit()
    operatingsystem = sys.argv[1]
    match operatingsystem:
        case "linux":
            # install linux version of pytorch
            os.system("pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu")
        case "mac":
            # install mac version of pytorch
            os.system("pip3 install torch torchvision torchaudio")
        case "windows":
            # install windows version of pytorch
            print("pip3 install torch torchvision torchaudio")
        case _:
            exit("Operating system not recognized. Please rerun program as:\tpython3 main.py [linux / mac / windows]\n")

    print("Installing required packages...")
    os.system("pip3 install -r requirements.txt")

def main():
    setup()
    app.app()

if __name__ == "__main__":
    main()