import PySimpleGUI as sg
from subprocess import run

layout: list = [
    [sg.Button(key='-bt_aiserver-', button_text='AIServer', size=20)],
    [sg.Button(key='-bt_buildserver-', button_text='BuildServer', size=20)]
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

    if event == '-bt_aiserver-':
        run(['sh', '/ilde/Downloads/AI2Offline6.2/startAIServer.sh'])

    if event == '-bt_buildserver-':
        run(['sh', '/ilde/Downloads/AI2Offline6.2/startBuildServer.sh'])


window.close()
