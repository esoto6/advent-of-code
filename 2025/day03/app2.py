
from typing import List


def calculate_joltage(bank: List[str], max_on: int) -> int:
    
    stack = []
    to_remove = len(bank) - max_on

    for i in bank:

        while stack and to_remove > 0 and stack[-1] < i:
            print(f"Starting STack: {stack}")
            print(f"{stack[-1]}, {i=}")
            print(f"{stack}")
            stack.pop()
            to_remove -= 1
            print(f"{stack=}, {to_remove=}")
        stack.append(i)

    stack = "".join(stack)
    print(f"Stack={stack}")
    stack = stack[:max_on]
    
    print(f"Stack={stack}")
    return int(stack)

def run():

    total = 0
    with open("sample.txt", "r") as file:
        banks = [line.strip() for line in file]
        
        for bank in banks:
            print(f"Processing {bank=}")
            
            battery_bank = [x for x in bank]
            for i in battery_bank:
                print(type(i))
            print(battery_bank)
            
            joltage = calculate_joltage(battery_bank, 12)
            print(joltage)
            total += joltage
    return total


if __name__ == "__main__":
    result = run()
    print(f"{result=}")
