import PySimpleGUI as sg

print(sg.theme_list())
sg.theme('BrownBlue')

layout = [
    [
        sg.InputText(key='--Nombre--', enable_events=True),
        sg.Button(
            key='--Boton--',
            button_text='',
            image_filename='buscar_copia.png',
            button_color=(sg.theme_background_color(), sg.theme_background_color()),
            border_width=0,
            image_size=(1, 1),
            auto_size_button=True
        )
    ],
    [sg.Text(key='--Salida--')]
]

window = sg.Window(layout=layout, font='Monaco 14', title='Pruebas', finalize=True)
window['--Nombre--'].bind('<Return>', ' ENTER')


def saludar():
    if values['--Nombre--']:
        window['--Salida--'].update(f'Hola {values["--Nombre--"].capitalize()}')
        window['--Nombre--'].update(value='')
        values['--Nombre--'] = ''


while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    if event == '--Boton--' or event == '--Nombre-- ENTER':
        saludar()

window.close()
