import PySimpleGUI as sg
import datetime

layout = [
    [
        sg.Text(text='Hora entrada:'),
        sg.Input(key='-HORAENTRADA-', size=2, enable_events=True, pad=(0, 0)),
        sg.Text(text=':', size=1, pad=(0, 0)),
        sg.Input(key='-MINUTOENTRADA-', size=2, enable_events=True, pad=(0, 0))
    ],
    [
        sg.Text(text='Hora salida:'),
        sg.Input(key='-HORASALIDA-', size=2, enable_events=True, pad=(0, 0)),
        sg.Text(text=':', size=1, pad=(0, 0)),
        sg.Input(key='-MINUTOSALIDA-', size=2, enable_events=True, pad=(0, 0))
    ],
    [sg.Button(key='-BOTONACEPTAR-', button_text='ESTABLECER HORA')],
    [sg.Text(key='-TEXTO-', text='')],
    [sg.Button('Salir')]
]

window = sg.Window('Validar hora', layout, font='Monaco 14')


def validar_hora_minuto(hora_minuto: str, key: str, maximo: int):
    if len(hora_minuto) > 0:
        if hora_minuto[-1].isdigit() and int(hora_minuto) <= maximo:
            return
        else:
            window[key].update(hora_minuto[:-1])
            return


while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Salir'):
        break

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
