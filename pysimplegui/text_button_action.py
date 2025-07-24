import PySimpleGUI as sg

layout = [ [sg.Text('Teste action ?', key='-TEXT-')],
           [sg.Button('1 - Yes')],
           [sg.Button('2 - No !!!')]]


window = sg.Window('Window teste', layout)

while True:             # Event Loop
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    window['-TEXT-'].update('Testando')

# import PySimpleGUI as sg

# layout = [[sg.Text("Hello from PySimpleGUI")], [sg.Button("OK")]]

# #sg.

# # Create the window
# window = sg.Window("Demo", layout)

# # Create an event loop
# while True:
#     event, values = window.read()
#     # End program if user closes window or
#     # presses the OK button
#     if event == "OK" or event == sg.WIN_CLOSED:
#         window.Refresh()

# window.close()