import PySimpleGUI as sg

fnt = 'Arial 12'


sg.popup_get_date(day_font='Monaco 14', start_day=1)

layout = [
    [
        sg.In(key='-INCAL1-', enable_events=True, visible=False),
        sg.Col(
            [
                [sg.CalendarButton('Change date', target='-INCAL1-',
                                   pad=None, key='-CAL1-', font=fnt, format='%Y-%m-%d', begin_at_sunday_plus=False)]
            ]
        )
    ]
]

window = sg.Window('Calendar', size=(400, 400), resizable=True).Layout(layout).finalize()

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break


window.close()
