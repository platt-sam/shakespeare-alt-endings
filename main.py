import os
import PySimpleGUI as sg
import sys
from datetime import date, datetime
from os import path
from transformers import pipeline

plays = {
    "Hamlet":"hamlet.txt",
    "King Lear":"king_lear.txt",
    "Macbeth":"macbeth.txt",
    "Romeo and Juliet":"romeo_and_juliet.txt",
    "Twelfth Night":"twelfth_night.txt",
}

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

def textgeneration(name):
    if len(name) == 0: # Ensure a prompt was entered
        exit("A prompt was not entered.")
    
    filename = plays[name]
    f = open("scripts/" + filename, "r")
    prompt = f.read()
    f.close()

    if len(prompt) > 1024: # Ensure input length is less than the maximum accepted by model
        prompt = prompt[0:1023]

    classifier = pipeline("text-generation")
    result = str(classifier(prompt, max_length=1024)[0]['generated_text'])

    fname = ('alternate ending_' + name + '_' + str(date.today()) + '_' + datetime.now().strftime('%H-%M-%S') + '.txt')
    outputfile = open(fname, "w")
    outputfile.write(result)
    outputfile.close()

    return result, fname

def app():
    # All the stuff inside your window
    playnames = list(plays.keys())

    layoutcontent = [
        [sg.Text('Choose a Play:'), sg.Combo(playnames, enable_events=True, readonly=False, key='-PLAYS-')],
        [sg.Text('', key='-RESULT-')],
        #[sg.Column(layout='', key='-RESULT-', size=(300,None), scrollable=True)],
    ]

    # Create the Window
    window = sg.Window(title='Shakespeare Alternate Ending Generator', layout=layoutcontent, size=(400,100))
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            break
        playname = values['-PLAYS-']

        res = textgeneration(playname)
        generatedresult = res[0]
        filename = res[1]
        
        window['-RESULT-'].update("Results saved to " + filename)

    window.close()

def main():
    setup()
    app()

if __name__ == "__main__":
    main()