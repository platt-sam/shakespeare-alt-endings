import os

print("Installing required packages...")
os.system("pip3 install -r requirements.txt")

import app # must be imported after requirements are installed

app.app()