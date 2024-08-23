import csv
import PySimpleGUI as sg

datos: list = []

with open(file='dias_fichados.csv', mode='r') as archivo_datos:
    dato_leidos = csv.reader(archivo_datos)
    for d in dato_leidos:
        datos.append(d)

layout: list = [
    [sg.Table(
        key='-tabla-',
        headings=['NOMBRE', 'EDAD', 'PROFESION'],
        values=datos,
        text_color='#0566b5',
        header_text_color='green',
        background_color='#b3d9f5',
        cols_justification=['c', 'r', 'c'],
        auto_size_columns=True,
        expand_x=True,
        alternating_row_color='#e0d3ad',
        enable_events=True
    )],
    [
        sg.InputText(key='-nombre-', size=12),
        sg.InputText(key='-edad-', size=4),
        sg.InputText(key='-profesion-', size=12)
    ],
    [sg.Button(key='-botonaceptar-', button_text='ACEPTAR')]
]

window: sg.Window = sg.Window(
    title='',
    layout=layout,
    size=(500, 400),
    font='Monaco 14',
    element_padding=8,
    finalize=True
)

fila_seleccionada: int = 0
datos_seleccionados: list = []

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break

    if event == '-tabla-':
        fila_seleccionada = window['-tabla-'].get()[0]
        datos_seleccionados = datos[fila_seleccionada]
        window['-nombre-'].update(value=datos_seleccionados[0])
        window['-edad-'].update(value=datos_seleccionados[1])
        window['-profesion-'].update(value=datos_seleccionados[2])

    if event == '-botonaceptar-' and datos_seleccionados:
        datos[fila_seleccionada] = (
            window['-nombre-'].get(),
            window['-edad-'].get(),
            window['-profesion-'].get(),
        )
        window['-tabla-'].update(values=datos, select_rows=[fila_seleccionada])
        with open(file='dias_fichados.csv', mode='w') as archivo_datos:
            escritor = csv.writer(archivo_datos)
            for d in datos:
                escritor.writerow(d)

window.close()
