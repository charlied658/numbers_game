# Numbers game simulation

import random

from src.StringFormatting import format_results, find_possible_solutions

digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
number_instance = []

for i in range(4):
    digit = random.choice(digits)
    digits.remove(digit)
    number_instance.append(digit)

guess_list = []
guess_results = []

running = True

while running:

    input_string = input("Guess a number:").split()

    if len(input_string) == 0:
        user_input = ""
    else:
        user_input = input_string[0]
    validGuess = False

    if user_input == "quit":
        print("> Quitting...")
        quit()
    elif user_input == "help":
        print("> quit - Quit the game" +
            "\n> help - List commands" +
            "\n> list - List previous guesses" +
            "\n> solutions - Count the number of possible solutions remaining" +
            "\n> print_solutions - List the remaining possible solutions")
    elif user_input == "list":
        if len(guess_list) == 0:
            print("> No guesses")
        else:
            for i in range(len(guess_list)):
                print(str(guess_list[i]) + " " + format_results(guess_results[i][0], guess_results[i][1]))
    elif user_input == "solutions":
        find_possible_solutions(guess_list, guess_results, False)
    elif user_input == "print_solutions":
        find_possible_solutions(guess_list, guess_results, True)

    else:
        nonNumeric = False
        for i in range(len(user_input)):
            if not user_input[i].isnumeric():
                nonNumeric = True
                break

        if len(user_input) == 0:
            nonNumeric = True

        if nonNumeric:
            print("> Not a valid command. Type 'help' for list of commands")
        else:
            if len(user_input) != 4:
                print("> Number must be length 4")
            else:
                validGuess = True

    guess = []

    if validGuess:
        for i in range(4):
            digit = int(user_input[i])
            if digit in guess:
                print("> No repeated digits")
                validGuess = False
                break
            guess.append(digit)

    if validGuess:
        if guess in guess_list:
            print("> Already guessed")
            validGuess = False

    if validGuess:
        good = 0
        regular = 0

        for i in range(4):
            if guess[i] in number_instance:
                if i == number_instance.index(guess[i]):
                    good += 1
                else:
                    regular += 1

        guess_results.append([good, regular])
        guess_list.append(guess)

        if good == 4:
            print("YOU WIN!")
            print("Solution = " + str(number_instance))
            print("Guesses = " + str(len(guess_list)))
            print("------------------------------")
            for i in range(len(guess_list)):
                print(str(guess_list[i]) + " " + format_results(guess_results[i][0], guess_results[i][1]))
            quit()

        print(str(guess) + " " + format_results(good, regular))
