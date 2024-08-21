import PySimpleGUI as sg

"""
    Restrict the characters allowed in an input element to digits and . or -
    Accomplished by removing last character input if not a valid character
"""

layout = [[sg.Text('Input only floating point numbers')],
          [sg.Input(key='-IN-', enable_events=True)],
          [sg.Input(key='-HORA-', enable_events=True)],
          [sg.Text(key='-texto-', text='hora')],
          [sg.Button('Exit')]]

window = sg.Window('Floating point input validation', layout, font='Monaco 14')

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    # if last character in input element is invalid, remove it
    if event == '-IN-' and values['-IN-'] and values['-IN-'][-1] not in '0123456789.-':
        window['-IN-'].update(values['-IN-'][:-1])
    if event == '-HORA-' and values['-HORA-']:
        try:
            hora = int(values['-HORA-'])
            if hora > 24:
                window['-HORA-'].update(values['-HORA-'][:-1])
        except:
            if len(values['-HORA-']) == 1 and values['-HORA-'][-1].isdigit():
                continue
            window['-HORA-'].update(values['-HORA-'][:-1])

window.close()
