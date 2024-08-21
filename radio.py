import PySimpleGUI as sg
from pyradios import RadioBrowser
from ffpyplayer.player import MediaPlayer
from time import sleep

# VARIABLES ############################################################################################################
# key: str = 'egyqJrMiagWtNYlPbgn8NzlIVYH5l9wqZWSOIf69IVkeRQlLdXmrVXs3bL3oBqlec4i9IKs2IukZxppoYv2sVhujcF2mVkJLRJCKIN6qMOTycKw0ODT2ghy3NhjaUN3oMkiQwlifTkGYlwjTZIWD5wzJZoUZRQlYccGqxKvkeZWk1UlmbHnmRyWpZPXGJfzgaLW99PuOI'

lista_emisoras: list = []
player = MediaPlayer('nada.mp3')


# FUNCIONES ------------------------------------------------------------------------------------------------------------
def buscar_emisoras(nombre_emisora: str) -> list:
    rb = RadioBrowser()
    resultado: list = []
    try:
        resultado = rb.search(name=nombre_emisora.capitalize(), name_exact=False)
        return resultado
    except ValueError:
        print('Error')


def actualizar_nombres(emisoras: list) -> list:
    nombres: list = []
    for emisora in emisoras:
        nombres.append(emisora['name'])
    return nombres


def reproducir_audio(url: str) -> None:
    global player
    parar_audio()
    try:
        player = MediaPlayer(url)
        player.get_frame()
        window['-btPausarAudio-'].update('Pausar', visible=True)
    except:
        player.close_player()


def parar_audio() -> None:
    global player
    player.close_player()


def pausar_audio() -> None:
    player.toggle_pause()


def continuar_audio(url: str) -> None:
    player.toggle_pause()


def cambiar_volumen(valor: float) -> None:
    global player
    volumen: float = round(valor / 10, 1)
    # print(volumen)
    # player.set_volume(volume=volumen)
    player.set_volume(volumen)


# INTERFAZ *************************************************************************************************************
marco_botones: list = [
    [
        sg.Button(key='-btBuscarEmisoras-', button_text='Buscar'),
        sg.Button(key='-btPausarAudio-', button_text='Pausar', visible=False)
    ]
]

layout: list = [
    [sg.Text(text='Emisora:'), sg.InputText(key='-entEmisora-')],
    [sg.Frame(title='Acciones', layout=marco_botones, element_justification='center', expand_x=True)],
    [sg.Listbox(key='-listaEmisoras-', values=[], size=(0, 10), expand_x=True, enable_events=True)],
    [sg.Slider(key='-slVolumen-', range=(0, 10), default_value=10, orientation='horizontal', enable_events=True)]
]

window = sg.Window(
    title='Emisoras internet',
    layout=layout,
    font='Monaco 14',
    element_padding=8,
    finalize=True
)

# BUCLE PRINCIPAL ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        parar_audio()
        break
    if event == '-btBuscarEmisoras-' and values['-entEmisora-']:
        lista_emisoras = buscar_emisoras(nombre_emisora=values['-entEmisora-'])
        if lista_emisoras:
            window['-listaEmisoras-'].update(values=actualizar_nombres(emisoras=lista_emisoras))
    if event == '-listaEmisoras-':
        url_audio: str = lista_emisoras[window['-listaEmisoras-'].get_indexes()[0]]['url']
        reproducir_audio(url=url_audio)
    if event == '-btPausarAudio-':
        if window['-btPausarAudio-'].ButtonText == 'Pausar':
            window['-btPausarAudio-'].update('Continuar')
            pausar_audio()
        else:
            url_audio: str = lista_emisoras[window['-listaEmisoras-'].get_indexes()[0]]['url']
            window['-btPausarAudio-'].update('Pausar')
            continuar_audio(url=url_audio)
    if event == '-slVolumen-':
        cambiar_volumen(valor=values['-slVolumen-'])


window.close()
