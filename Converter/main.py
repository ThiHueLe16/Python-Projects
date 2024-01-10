import PySimpleGUI as sg
layout = [
            [sg.Text("Text"), sg.Input(key="-INPUT-"), sg.Spin(["km to dm", "hours to minutes"], key="-UNIT-"), sg.Button("Convert", key="-CONVERT-")],
            [sg.Text("Result",  key="-RESULT-")]
]
window = sg.Window("Converter", layout)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == "-CONVERT-":
        input_value = values["-INPUT-"]
        print(input_value)
        if input_value.isnumeric():
            if values["-UNIT-"] == "km to dm":
                output = float(input_value) * 10
                output_string = f'{input_value} km is {output} dm'
            if values["-UNIT-"] == "hours to minutes":
                output = float(input_value)*60
                output_string = f'{input_value} hours is {output} minutes'
            window["-RESULT-"].update(output_string)
        else:
            window["-RESULT-"].update("please enter a valid number ")


window.close()
