import os
from pprint import pprint

def solve_problem(file: str):
    with open(file, "r") as f:
        lines = f.read().split("\n")
        graph = [[c for c in line] for line in lines]
        # pprint(graph)

        #How do i go through my graph (list of lists)
        hasRows = len(graph)
        hasCols = len(graph[0])

        # pprint(f"Row: {hasRows}, Col: {hasCols}")

        #Variable to hold answer 
        ans = 0

        for row in range(len(graph)):
            # variable to keep track of numbers
            digits = 0
            # Variable to keep track if adjacent to part
            isAdjacent = False

            # pprint(f"Row: {row}")
            for col in range(len(graph[row]) + 1):
                # print(f"Col: {col}")
                # pprint(f"Val: {graph[row][col]}")
                if col < hasCols and graph[row][col].isdigit():
                    # To make a multi digit number we multiply the value by 10 since we start with 0
                    digits = digits * 10 + int(graph[row][col])
                    #pprint(f"digits: {digits}")

                    #Check values around current location
                    for subRow in [-1, 0, 1]:
                        for subCol in [-1, 0, 1]:
                            # pprint(graph[rr][cc])
                            # Check to make sure we dont go out of bounds
                            if 0 <= row + subRow < hasRows and 0 <= col + subCol < hasCols:
                                character = graph[row + subRow][col + subCol]
                                # pprint(f"Col: {character}")

                                if not character.isdigit() and character not in ['.']:
                                    # pprint(f"Col: {character}")
                                    isAdjacent = True
                elif digits > 0:
                    if isAdjacent:
                        pprint(f"Final Digits: {digits} and {isAdjacent}")

                        ans += digits
                    else:
                        pprint(f"Final Digits: {digits} is {isAdjacent}")
                    digits = 0
                    isAdjacent = False

        pprint(f"The Answer is: {ans}")
        return ans

    
if __name__ == "__main__":

    isTest = False
    expected = 4361

    if isTest:
        data_file = "data_day3_test.txt"
    else:
        data_file = "data_day3.txt"
        
    file = os.path.join(os.path.dirname(__file__), data_file)
    val = solve_problem(file)

    if isTest:
        if val == expected:
            print("Passed: True")
        else:
            print("Passed: False")
    else:
        print(f"Value: {val}")