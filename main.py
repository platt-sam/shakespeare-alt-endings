import argparse
import os
import PySimpleGUI as sg
import sys

from transformers import pipeline

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

def textgeneration(prompt):
    if len(prompt) == 0:
        exit("A prompt was not entered.")
    classifier = pipeline("text-generation")
    result = str(classifier(prompt, max_length=250)[0]['generated_text'])
    txt = "{0}\n\n{1}"
    return txt.format(prompt,result)

def app():
    # All the stuff inside your window
    layout = [  [sg.Text('some text')],
                [sg.Text('Prompt:'), sg.InputText()],
                [sg.Button('Generate'), sg.Button('Cancel')] ]

    # Create the Window
    window = sg.Window('Shakespeare Alternate Endings', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            break
        displaytext = textgeneration(values[0])
        print(displaytext) # prints what the user entered to the console

    window.close()

def main():
    setup()
    app()

if __name__ == "__main__":
    main()