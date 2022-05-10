import PySimpleGUI as prac
import tkinter as tk
from tkinter import ttk


prac.theme('BluePurple')

user_guesses = [
    [1205, "2R"],
    [4567, "3R"]]




headings = ["Your Guesses", "Information Recieved"]

layout = [[prac.Table(values = user_guesses, headings = headings,
        max_col_width = 25,
        auto_size_columns =True,
        display_row_numbers = False,
        justification = "center",
        num_rows = 10,
        key = "-TABLE-",
        row_height = 35,
        size = (50,50))], 
        [prac.Text('Your Guess', size =(15, 1)), prac.InputText()],
        [prac.Submit(), prac.Cancel()]]
window = prac.Window('Number game table', layout, size = [650,700], resizable=True)

while True:  # Event Loop
    event, values = window.read()
    #print(event, values)
    if event == prac.WIN_CLOSED or event == 'Exit':
        break
    if event == "Submit":
        input = values.get(0)
        
        list = [input, "1R"]
        user_guesses.append(list)
        window.Element("-TABLE-").update(values = user_guesses)
        window.refresh()

window.close()