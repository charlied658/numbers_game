
import PySimpleGUI as prac
import GamePage
from tkinter import *
from tkinter import ttk


root = Tk(screenName = "MainPage", baseName = "MainPage")
logo = PhotoImage(file = "../Images/code.gif")
label = ttk.Label(root, text = "Welcome! I am glad you took the challenge to play the game of numbers that only few have mastered...!!", 
                wraplength=200, justify = CENTER, 
                foreground = "blue", background = "yellow", 
                font = ("Courier", 12, "bold"), image = logo, compound= "top")
label.pack()
startGameButton = ttk.Button(root, text = 'Start Game')
startGameButton.pack()
rulesPageButton = ttk.Button(root, text = "Rules")
rulesPageButton.pack()

def gameStart():
    window = GamePage.createGamePage()
    GamePage.gameLoop(window)

def openRulesPAge():
    pass

startGameButton.config(command = gameStart)
rulesPageButton.config(command = openRulesPAge)

# startGameButton.state(["disabled"])
root.mainloop()
# while True:  # Event Loop
#     event, values = root.read()
#     #print(event, values)
#     if event == prac.WIN_CLOSED:
#         break
#     elif event == "-START_GAME-":
#         gameWindow = GamePage.createGamePage()
#         GamePage.gameLoop(gameWindow)
#         print("Create a GamePAge")
#     elif event == "-RULES_PAGE-":
#         pass
# window.close()

