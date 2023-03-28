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
    if len(prompt) == 0: # Ensure a prompt was entered
        exit("A prompt was not entered.")

    if len(prompt) > 1024: # Ensure input length is less than the maximum accepted by model
        prompt = prompt[0:1023]

    classifier = pipeline("text-generation")
    result = str(classifier(prompt, max_length=1024)[0]['generated_text'])
    return result

def app():
    # All the stuff inside your window
    layout = [  [sg.Text('Choose a play for the AI to finish for you')],
                [sg.Text('Play:'), sg.Combo(["Hamlet", "King Lear", "Macbeth", "Romeo and Juliet", "Twelfth Night"], expand_x=True, enable_events=True,  readonly=False, key='-PLAYS-')],
                [sg.Button('Generate'), sg.Button('Cancel')] ]

    # Create the Window
    window = sg.Window('Shakespeare Alternate Ending Generator', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            break
        prompt = values['-PLAYS-']
        print(textgeneration(prompt))

    window.close()

def main():
    setup()
    app()

if __name__ == "__main__":
    main()