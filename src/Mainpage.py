import PySimpleGUI as prac
import GamePage

layout = [[prac.Button(button_text = 'Start Game',size =(15, 1), key = "-START_GAME-")],
        [prac.Button(button_text = "Rules Page", size = (15,1), key = "-RULES_PAGE-")]]

window = prac.Window('Main Menu', layout, size = [650,700], resizable=True, element_justification = "center")

while True:  # Event Loop
    event, values = window.read()
    #print(event, values)
    if event == prac.WIN_CLOSED:
        break
    elif event == "-START_GAME-":
        gameWindow = GamePage.createGamePage()
        GamePage.gameLoop(gameWindow)
        print("Create a GamePAge")
    elif event == "-RULES_PAGE-":
        pass

window.close()
