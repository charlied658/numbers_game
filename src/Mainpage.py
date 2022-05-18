
import PySimpleGUI as prac
import GamePage
from RulesPage import createRulesPage
from tkinter import *
from tkinter import ttk


root = Tk(screenName = "MainPage")
logo = PhotoImage(file = "../Images/code.gif")
frame = ttk.Frame(root, height= 1800, width=1800)
frame.pack()
label = ttk.Label(frame, text = "Welcome! I am glad you took the challenge to play the game of numbers that only few have mastered...!!", 
                justify = CENTER, 
                foreground = "blue", 
                font = ("Courier", 12, "bold"),image = logo, compound= "top")
label.pack()
startGameButton = ttk.Button(frame, text = 'Start Game')
startGameButton.pack()
rulesPageButton = ttk.Button(frame, text = "Rules")
rulesPageButton.pack()

def gameStart():
    window = GamePage.createGamePage()
    GamePage.gameLoop(window)

def openRulesPAge():
    createRulesPage()

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

