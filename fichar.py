import PySimpleGUI as sg
from datetime import datetime
import locale

locale.setlocale(locale.LC_ALL, 'es_ES')

hoyYear: int = datetime.now().year
hoyMes: int = datetime.now().month
hoyDia: int = datetime.now().day

fecha: tuple = (hoyMes, hoyDia, hoyYear)


def fecha_texto(fecha_tupla: tuple) -> str:
    nombres_meses: list = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio',
                           'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']
    return f'{fecha_tupla[1]}/{nombres_meses[fecha_tupla[0] - 1]}/{fecha_tupla[2]}'


layout: list = [
    [
        sg.Text(key='-FechaTexto-', text=fecha_texto(fecha_tupla=fecha)),
        sg.Button(button_text='Elegir fecha', key='-Calendario-')
    ]
]

window: sg.Window = sg.Window(
    title='',
    layout=layout,
    font='Monaco 14',
    element_padding=8,
    size=(400, 200),
    resizable=True
)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break

    if event == '-Calendario-':
        fecha_elegida: tuple = sg.popup_get_date(
            day_font='Monaco 14', start_day=1,
            mon_year_font='Monaco 14', begin_at_sunday_plus=True, arrow_font='Monaco 14',
            no_titlebar=False, modal=True, close_when_chosen=True
        )
        window['-FechaTexto-'].update(value=fecha_texto(fecha_tupla=fecha_elegida))

window.close()
