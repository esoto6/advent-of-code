import os
from collections import defaultdict
from pprint import pprint

def solve_problem(file: str):
    with open(file, "r") as f:
        lines = f.read().split("\n")

        # Use Dictionary to store list
        cards_range_won = {}
        print(cards_range_won)
        # tally = 0
        
        values = [x for x in range(1, len(lines) + 1)]
        card_stack = defaultdict(int)
        for i, line in enumerate(lines):
            card_stack[i] += 1
            # print(line)
            card_game, details = line.split(":")
            idx = int(card_game.split()[1])
            print(f"idx: {idx}")
            details = details.strip(" ")

            # How can i imrpove this step?
            left, right = details.strip().split("|")

            winning_numbers = set([int(x) for x in left.split()])
            my_numbers = set([int(x) for x in right.split()])
            
            # print(f"Winning: {winning_numbers}, Mine: {my_numbers}")

            matching = winning_numbers.intersection(my_numbers)

            print(f"idx: {idx} has {len(matching)}")

            for match in range(len(matching)):
                print(f"Key: {i + 1 + match}")
                print(f"Card_stack before: {card_stack[i + 1 + match]}")
                card_stack[i + 1 + match] += card_stack[i]
                print(f"car stack after: {card_stack[i + 1 + match]}")
            


        print(f"Finished: {card_stack}")
        print(f"Total: {sum(card_stack.values())}")
        return sum(card_stack.values())
            # value = 0
            # if len(matching) > 0:
            #     value += 2 ** (len(matching) - 1)
            # print(f"IDX: {idx} ---- Current Value: {value}")

            
            # tally += value
        # return tally
    
if __name__ == "__main__":
    isTest = False
    expected = 30

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