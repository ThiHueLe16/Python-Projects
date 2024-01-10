# This is a sample Python script.

import PySimpleGUI as sg
smiley = [
    ["happy", [";)", "xD", "<3"]],
    ["sad", [":(", ":/"]],
    ["love", [":3"]]
]
menu_layout = [
    ["File",  ['open', "save", "---", "exit"]],
    ["Tools", ["World count "]],
    ["Icon", smiley]



]
layout = [
    [sg.Menu(menu_layout)],
    [sg.Text("Untitled", key=' -DOCNAME- ' )],
    [sg.Multiline()]
]
window = sg.Window("Text Editor", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

window.close()

