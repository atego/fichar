import PySimpleGUI as sg
from random import randint


def generar_lista_aleatorios() -> list:
    aleatorios: list = []
    while len(aleatorios) < 6:
        num_aleatorio = randint(1, 49)
        if num_aleatorio not in aleatorios:
            aleatorios.append(num_aleatorio)
    return aleatorios


lista_aleatorios: list = generar_lista_aleatorios()
lista_aleatorios.sort()
lista_aleatorios_texto: str = ", ".join(map(str, lista_aleatorios))

layout: list = [
    [sg.Text(text='Combinación Bonoloto:')],
    [sg.Text(text=lista_aleatorios_texto)]
]

window: sg.Window = sg.Window(
    title='',
    layout=layout,
    font='Monaco 14',
    element_padding=8
)


while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break

window.close()
