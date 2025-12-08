
from typing import List

def calculate_joltage(bank: List[str]) -> int:
    curr_max = 0
    highest_value = 0
    for i in range(0, len(bank)):
        if i == len(bank)-1:
            pass
        else:
            vals_to_check = bank[i+1:]
            highest_possible = max(vals_to_check)
            
            print(f"{i=}, value={bank[i]}, {vals_to_check=}, {highest_possible=}")
            highest_value = max(highest_value, int(str(bank[i]) + str(highest_possible)))
    print(f"{highest_value=}")
    return highest_value

def run():

    total = 0
    with open("input.txt", "r") as file:
        banks = [line.strip() for line in file]
        
        for bank in banks:
            print(f"Processing {bank=}")
            
            battery_bank = [x for x in bank]
            print(battery_bank)
            joltage = calculate_joltage(battery_bank)
            print(joltage)
            total += joltage
    return total


if __name__ == "__main__":
    result = run()
    print(f"{result=}")
