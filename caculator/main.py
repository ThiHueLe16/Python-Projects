import PySimpleGUI as sg


def initiate_window(theme):
    sg.theme(theme)
    sg.set_options(font="Franklin 14", button_element_size=(6, 3))

    button_size = (6, 3)
    layout = [[sg.Text("Result", key="RESULT", font="Franklin 26", expand_x=True, justification="right", pad=(10, 10),
                       right_click_menu=theme_menu)],
              [sg.Button("clear", key="CLEAR", expand_x=True), sg.Button("calculate", key="CALCULATE", expand_x=True)],
              [sg.Button("7", key="7", size=button_size), sg.Button("8", key="8", size=button_size),
               sg.Button("9", key="9", size=button_size), sg.Button("*", key="*", size=button_size)],
              [sg.Button("4", key="4", size=button_size), sg.Button("5", key="5", size=button_size),
               sg.Button("6", key="6", size=button_size), sg.Button("/", key="/", size=button_size)],
              [sg.Button("1", key="1", size=button_size), sg.Button("2", key="2", size=button_size),
               sg.Button("3", key="3", size=button_size), sg.Button("+", key="+", size=button_size)],
              [sg.Button("0", key="0", expand_x=True), sg.Button(".", key="."), sg.Button("-", key="-")]
              ]
    return sg.Window('Calculator', layout)


theme_menu = ['menu', ["dark", "light", 'pink']]
window = initiate_window('Dark Amber 5')
current_number = []

while True:
    event, value = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == "CALCULATE ":
        print("calculate")
        window["RESULT"].update("hallo")
    if event in theme_menu[1]:
        print(event)
        window.close()
        window = initiate_window(event)
    if event in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]:
        current_number.append(event)
        num_string = "".join(current_number)
        print(num_string)
        window["RESULT"].update(num_string)
    if event in ["+", "-", "*", "/"]:
        current_number.append(event)
        num_string = "".join(current_number)
        print(num_string)
        window["RESULT"].update(num_string)
        print(event)
    if event == "CLEAR":
        print(event)
        current_number.pop()
        num_string = "".join(current_number)
        print(num_string)
        window["RESULT"].update(num_string)
    if event == "CALCULATE":
        print(event)
        result = eval("".join(current_number))
        window["RESULT"].update(result)
        current_number = [str(result)]

window.close()
