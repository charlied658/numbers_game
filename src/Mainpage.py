import PySimpleGUI as prac


layout = [[prac.Button(button_text = 'Start Game',size =(15, 1), key = "-START_GAME-")]]

window = prac.Window('Main Menu', layout, size = [650,700], resizable=True, element_justification = "center")

while True:  # Event Loop
    event, values = window.read()
    #print(event, values)
    if event == prac.WIN_CLOSED:
        break

window.close()
