import PySimpleGUI as sg

sg.theme('BrownBlue')

layout = []

window = sg.Window(layout=layout, font='Monaco 14', title='', finalize=True)
# window['--Nombre--'].bind('<Return>', ' ENTER')


while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break


window.close()
