import PySimpleGUI as sg

print(sg.theme_list())
lista_temas: list = sg.theme_list()


marco_entrada: list = [
    [sg.InputText()],
    [sg.Button(button_text='Hola')]
]

layout: list = [
    [sg.Frame(
        key='-MarcoEntrada-', title='Prueba',
        layout=marco_entrada, border_width=2,
    )],
    [sg.Combo(
        key='-ComboTemas-', values=lista_temas,
        default_value='BluePurple',
        enable_events=True
    )]
]

window: sg.Window = sg.Window(
    title='',
    layout=layout,
    font='Monaco 14',
    element_padding=8,
    size=(600, 400),
)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break

    if event == '-ComboTemas-':
        print(values['-ComboTemas-'])


window.close()
