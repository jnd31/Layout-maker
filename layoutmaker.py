import PySimpleGUI as sg

sg.theme('BluePurple')

layout = [[sg.Text('Enter text to appear in the new window:'), sg.Text(size=(15,1))],
          [sg.Input(key='-IN-')],
          [sg.Push(), sg.Text('Line number: '), sg.Input(key='-Line-')],
          [sg.Button('Add'), sg.Button('Show'), sg.Button('Print Layout'), sg.Button('Exit')]]

window = sg.Window('Layout Maker', layout)

constructed_layout = [[]]
construct_active = False
while True:  # Event Loop
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Add':
        constructed_layout[int(values['-Line-'])] = [sg.Text(values['-IN-'])]
    if event == 'Show' and not construct_active:
        construct_active = True
        construct_window = sg.Window('New Layout', constructed_layout)
        while True:
            ev2, vals2 = construct_window.read()
            if ev2 == sg.WIN_CLOSED:
                construct_window.close()
                construct_active = False
                break

window.close()