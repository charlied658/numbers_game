def format_results(good, regular):
    if good == 0:
        if regular == 0:
            return "0"
        else:
            return str(regular) + "R"
    else:
        if regular == 0:
            return str(good) + "G"
        else:
            return str(good) + "G " + str(regular) + "R"


def find_possible_solutions(guess_list, guess_results, print_results):

    possible_solutions = []
    num_solutions = 0

    for i in range(10):
        for j in range(9):
            for k in range(8):
                for n in range(7):
                    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
                    solution = [digits.pop(i), digits.pop(j), digits.pop(k), digits.pop(n)]

                    isSolution = True

                    for g in range(len(guess_list)):
                        good = 0
                        regular = 0

                        for p in range(4):
                            if guess_list[g][p] in solution:
                                if p == solution.index(guess_list[g][p]):
                                    good += 1
                                else:
                                    regular += 1

                        if good != guess_results[g][0] or regular != guess_results[g][1]:
                            isSolution = False

                    if isSolution:
                        if print_results:
                            print(solution)
                        num_solutions += 1
                        possible_solutions.append(solution)

    print("Possible solutions = " + str(num_solutions))
    return num_solutions
