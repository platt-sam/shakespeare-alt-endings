import PySimpleGUI as sg
from transformers import pipeline
import os

def setup():
    print("Installing required packages...")
    os.system("pip3 install -r requirements.txt")

def app():
    # All the stuff inside your window.
    layout = [  [sg.Text('Some text on Row 1')],
                [sg.Text('Filename:'), sg.InputText()],
                [sg.Button('Generate'), sg.Button('Cancel')] ]

    # Create the Window
    window = sg.Window('Window Title', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            break
        print('You entered ', values[0]) # prints what the user entered to the console

    window.close()

def main():
    setup()
    app()

if __name__ == "__main__":
    main()