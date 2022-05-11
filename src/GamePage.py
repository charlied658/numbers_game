import PySimpleGUI as prac
from numpy import info
from NumbersGame import score_guess, generate_number, process_input


prac.theme('BluePurple')


user_guesses = []

#TODO In TKINter there is an entry widget
# entry = ttk.Entry(root, widht = 30).pack()
# Does not have a command option.  TODO has to be binded

#entry.get()  will return the contents
##When i config to show = "* " data inputted is not being shown

headings = ["Your Guesses", "Information Recieved"]
def createGamePage():
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
    return window

def gameLoop(window):
    global user_guesses
    numberToGuess = generate_number()
    while True:  # Event Loop
        event, values = window.read()
        #print(event, values)
        if event == prac.WIN_CLOSED or event == 'Exit':
            break
        if event == "Submit":
            input = values.get(0)
            result = process_input(input)
            print(result)
            information = score_guess(numberToGuess, result)
            print("info gotten", information)
            #Call a method to pass a string that does the check. 
            #result is going to be array of ints
            s = [str(i) for i in result] 
            # # Join list items using join()
            res = int("".join(s))
            list = [res, information]
            user_guesses.append(list)
            window.Element("-TABLE-").update(values = user_guesses)
            window.refresh()

    window.close()