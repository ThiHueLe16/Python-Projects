# This is a sample Python script.

import PySimpleGUI as sg


def create_window(theme):
    sg.theme(theme)
    smiley = [
        ["happy", [":)", ":>"]]
    ]

    menu_layout = [
        ['File', ["open", "Save", "close"]],
        ['Tools', ["world count"]],
        ['Icon', smiley]
    ]
    layout = [
        [sg.Menu(menu_layout, font="SYSTEM_DEFAULT", text_color="black", disabled_text_color="yellow", pad=(10, 10))],
        [sg.Text('Untitled ')],
        [sg.Multiline(no_scrollbar=True)]
    ]
    return sg.Window('Texteditor', layout, default_element_size =(50, 40), resizable=True, finalize=True)


window = create_window('LightBrown2')

while True:
    event, value = window.read()
    if event == sg.WIN_CLOSED:
        break

window.close()
