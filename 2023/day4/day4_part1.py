import os
from pprint import pprint

def solve_problem(file: str):
    with open(file, "r") as f:
        lines = f.read().split("\n")

        tally = 0

        for line in lines:
            # print(line)
            idx, details = line.split(":")
            print(f"idx: {idx}")
            details = details.strip(" ")

            # How can i imrpove this step?
            left, right = details.strip().split("|")

            winning_numbers = set([int(x) for x in left.split()])
            my_numbers = set([int(x) for x in right.split()])
            
            print(f"Winning: {winning_numbers}, Mine: {my_numbers}")

            matching = winning_numbers.intersection(my_numbers)

            print(f"Matches: {matching}")

            # value = 1
            # for i in range(1, len(matching)):
            #     print(f"I: {i}, {len(matching)}")
            #     if i == 1:
            #         pass
            #     else:
            #         value = value * i

            value = 0
            if len(matching) > 0:
                value += 2** (len(matching) - 1)
            print(f"IDX: {idx} ---- Current Value: {value}")

            
            tally += value
        return tally
    
if __name__ == "__main__":

    isTest = False
    expected = 13

    if isTest:
        data_file = "data_day4_test.txt"
    else:
        data_file = "data_day4.txt"

    file = os.path.join(os.path.dirname(__file__), data_file)
    result = solve_problem(file)

    if isTest:
        if result == expected:
            print("Passed: True")
        else:
            print("Passed: False")
    else:
        print(f"Result: {result}")