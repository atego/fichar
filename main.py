import PySimpleGUI as sg
import datetime
import locale

locale.setlocale(locale.LC_ALL, 'es_ES')

# VARIABLES GLOBALES ---------------------------------------------------------------------------------------------------
hoyYear: int = datetime.datetime.now().year
hoyMes: int = datetime.datetime.now().month
hoyDia: int = datetime.datetime.now().day

fecha: datetime = datetime.datetime.today()
fecha_texto = datetime.datetime.strftime(fecha, '%d/%m/%Y')
nombres_meses: list = [
    'enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio',
    'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre'
]


# FUNCIONES ------------------------------------------------------------------------------------------------------------
def actualizar_fecha():
    global fecha, fecha_texto
    nueva_fecha: tuple = sg.popup_get_date(
        day_font='Monaco 14', start_day=1,
        mon_year_font='Monaco 14', begin_at_sunday_plus=True, arrow_font='Monaco 14',
        no_titlebar=False, modal=True, close_when_chosen=True, title='Elige fecha'
    )
    if nueva_fecha:
        fecha = datetime.date(day=nueva_fecha[1], month=nueva_fecha[0], year=nueva_fecha[2])
        fecha_texto = datetime.datetime.strftime(fecha, '%d/%m/%Y')
        window['-FechaTexto-'].update(value=fecha_texto)


def validar_hora_minuto(hora_minuto: str, key: str, maximo: int) -> None:
    if len(hora_minuto) > 0:
        if not hora_minuto[-1].isdigit() or int(hora_minuto) > maximo:
            window[key].update(hora_minuto[:-1])


# INTERFAZ -------------------------------------------------------------------------------------------------------------
marco_entrada_datos: list = [
    [
        sg.Text(key='-FechaTexto-', text=fecha_texto),
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
    [
        sg.Text(text='Anotación'),
        sg.InputText(key='-ANOTACION-', expand_x=True)
    ],
    [sg.Button(key='-BOTONACEPTARDATOS-', button_text='GUARDAR DATOS')]
]

layout: list = [
    [sg.Frame(
        title='Entrada de datos', layout=marco_entrada_datos,
        expand_x=True, border_width=2,
        vertical_alignment='center'
    )],
    [sg.Text(key='-TEXTO-', text='')]
]

window: sg.Window = sg.Window(
    title='',
    layout=layout,
    font='Monaco 14',
    element_padding=8,
    size=(550, 400),
    resizable=True,
    finalize=True
)

# CICLO DE LA APLICACIÓN -----------------------------------------------------------------------------------------------
while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break

    if event == '-Calendario-':
        actualizar_fecha()

    if event == '-HORAENTRADA-' or event == '-HORASALIDA-':
        validar_hora_minuto(hora_minuto=values[event], key=event, maximo=23)

    if event == '-MINUTOENTRADA-' or event == '-MINUTOSALIDA-':
        validar_hora_minuto(hora_minuto=values[event], key=event, maximo=59)

    if event == '-BOTONACEPTARDATOS-':
        if values['-HORAENTRADA-'] and values['-HORASALIDA-'] and values['-MINUTOENTRADA-'] and values['-MINUTOSALIDA-']:
            hora_entrada = datetime.time(hour=int(values['-HORAENTRADA-']), minute=int(values['-MINUTOENTRADA-']))
            hora_salida = datetime.time(hour=int(values['-HORASALIDA-']), minute=int(values['-MINUTOSALIDA-']))
            window['-TEXTO-'].update(
                value=f'Entrada: {hora_entrada.strftime('%H:%M')}, Salida: {hora_salida.strftime('%H:%M')}')
            entrada = datetime.timedelta(hours=hora_entrada.hour, minutes=hora_entrada.minute)
            salida = datetime.timedelta(hours=hora_salida.hour, minutes=hora_salida.minute)
            tiempo_trabajado = salida - entrada
            anotacion = values['-ANOTACION-']
            print(f'Fecha: {fecha}\nHora entrada: {hora_entrada}\nHora salida: {hora_salida}'
                  f'\nTiempo trabajado: {tiempo_trabajado}'
                  f'\nAnotación: {anotacion}')

window.close()
