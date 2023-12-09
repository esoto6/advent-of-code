import os
from pprint import pprint
from collections import defaultdict

def solve_problem(file: str):
    with open(file, "r") as f:
        lines = f.read().split("\n")
        graph = [[c for c in line] for line in lines]
        # pprint(graph)

        #How do i go through my graph (list of lists)
        hasRows = len(graph)
        hasCols = len(graph[0])

        ans = 0

        # pprint(f"Row: {hasRows}, Col: {hasCols}")
        allGears = defaultdict(list)
        #Variable to hold answer 
        # ans = 0
        for row in range(len(graph)):
            # variable to keep track of numbers
            gearSet = set()

            # Variable to keep track if adjacent to part
            isAdjacent = False

            digits = 0

            # pprint(f"Row: {row}")
            for col in range(len(graph[row]) + 1):
                # print(f"Col: {col}")
                # pprint(f"Val: {graph[row][col]}")
                if col < hasCols and graph[row][col].isdigit():
                    digits = digits * 10 + int(graph[row][col])
                    #pprint(f"digits: {digits}")
                    
                    #Check values around current location
                    for rr in [-1, 0, 1]:
                        for cc in [-1, 0, 1]:
                            # pprint(graph[rr][cc])
                            # Check to make sure we dont go out of bounds
                            if 0 <= row + rr < hasRows and 0 <= col + cc < hasCols:
                                character = graph[row + rr][col + cc]
                                # pprint(f"Col: {character}")

                                if not character.isdigit() and character not in ['.']:
                                    # pprint(f"Col: {character}")
                                    isAdjacent = True
                                if character == "*":
                                    gearSet.add((row + rr, col + cc))
                                    pprint(f"GearSet: {gearSet}")
                elif digits > 0:
                    for gear in gearSet:
                        pprint(f"Gear is: {gear}")
                        allGears[gear].append(digits)
                    if isAdjacent:
                        ans += digits
                    digits = 0

                    isAdjacent = False
                    gearSet = set()

        print(ans)
        ans = 0
        for k, v in allGears.items():
            pprint(f"V: {v}")
            if len(v) == 2:
                ans += v[0] * v[1]
        print(ans)
        return ans

    
if __name__ == "__main__":

    isTest = False
    expected = 467835

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