import PySimpleGUI as sg


layout = [
    [sg.Button(button_text='hola')]
]


window = sg.Window(layout=layout, title='Pruebas Qt')


while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED():
        break


window.close()
