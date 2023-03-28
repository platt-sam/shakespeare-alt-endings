import PySimpleGUI as sg
import textgen

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
        displaytext = textgen.textgeneration(values[0])
        print(displaytext) # prints what the user entered to the console

    window.close()