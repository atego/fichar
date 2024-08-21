import PySimpleGUI as sg
import datetime
import locale

locale.setlocale(locale.LC_ALL, 'es_ES')

hoyYear: int = datetime.datetime.now().year
hoyMes: int = datetime.datetime.now().month
hoyDia: int = datetime.datetime.now().day

fecha: tuple = (hoyMes, hoyDia, hoyYear)


def fecha_texto(fecha_tupla: tuple) -> str:
    nombres_meses: list = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio',
                           'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']
    return f'{fecha_tupla[1]}/{nombres_meses[fecha_tupla[0] - 1]}/{fecha_tupla[2]}'


layout: list = [
    [
        sg.Text(key='-FechaTexto-', text=fecha_texto(fecha_tupla=fecha)),
        sg.Button(button_text='Elegir fecha', key='-Calendario-')
    ],
    [

        sg.Text(text='Hora entrada'),
        sg.Input(key='-HORAENTRADA-', size=2, enable_events=True, pad=(0, 0)),
        sg.Text(text=':', size=1, pad=(0, 0)),
        sg.Input(key='-MINUTOENTRADA-', size=2, enable_events=True, pad=(0, 0)),
        sg.Text(' '),
        sg.Text(text='Hora salida'),
        sg.Input(key='-HORASALIDA-', size=2, enable_events=True, pad=(0, 0)),
        sg.Text(text=':', size=1, pad=(0, 0)),
        sg.Input(key='-MINUTOSALIDA-', size=2, enable_events=True, pad=(0, 0))

    ],
    [sg.Button(key='-BOTONACEPTAR-', button_text='ESTABLECER HORA')],
    [sg.Text(key='-TEXTO-', text='')],
    [sg.Button('Salir')]
]

window: sg.Window = sg.Window(
    title='',
    layout=layout,
    font='Monaco 14',
    element_padding=8,
    size=(400, 200),
    resizable=True
)


def validar_hora_minuto(hora_minuto: str, key: str, maximo: int) -> None:
    if len(hora_minuto) > 0:
        if hora_minuto[-1].isdigit() and int(hora_minuto) <= maximo:
            return
        else:
            window[key].update(hora_minuto[:-1])
            return


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

    if event == '-HORAENTRADA-' or event == '-HORASALIDA-':
        validar_hora_minuto(hora_minuto=values[event], key=event, maximo=23)

    if event == '-MINUTOENTRADA-' or event == '-MINUTOSALIDA-':
        validar_hora_minuto(hora_minuto=values[event], key=event, maximo=59)

    if event == '-BOTONACEPTAR-':
        if values['-HORAENTRADA-'] and values['-HORASALIDA-'] and values['-MINUTOENTRADA-'] and values['-MINUTOSALIDA-']:
            hora_entrada = datetime.time(hour=int(values['-HORAENTRADA-']), minute=int(values['-MINUTOENTRADA-']))
            hora_salida = datetime.time(hour=int(values['-HORASALIDA-']), minute=int(values['-MINUTOSALIDA-']))
            window['-TEXTO-'].update(
                value=f'Entrada: {hora_entrada.strftime('%H:%M')}, Salida: {hora_salida.strftime('%H:%M')}')
            entrada = datetime.timedelta(hours=hora_entrada.hour, minutes=hora_entrada.minute)
            salida = datetime.timedelta(hours=hora_salida.hour, minutes=hora_salida.minute)
            print(salida - entrada)

window.close()
