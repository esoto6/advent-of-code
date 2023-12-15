
import logging
from typing import List
import os
#  https://adventofcode.com/2023/day/1


def calculate_sum(validList: List[int]):
    sum = 0
    for i, v in enumerate(validList):
        sum += v
    return sum

def troubleshoot(x: str) -> List[int]:
    numberMap = {"one": "1", "two": "2", "three": "3", "four":"4", "five":"5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
    numbers = []
    
    for i, c in enumerate(x):
        if c.isdigit():
            numbers.append(c)
        for d, val in enumerate(numberMap.keys()):
            if x[i:].startswith(val):
                numbers.append(str(d+1))
    # print(numbers)
    return numbers


def trebuchet_calculation(example) -> int:
    validList = []

    for i, v in enumerate(example):
        numbers = troubleshoot(v)
        
        print(numbers)


        val = 0
        if len(numbers) == 1:
            val = int(numbers[0] + numbers[0])
            validList.append(val)
        elif len(numbers) == 2:
            val = int(numbers[0] + numbers[1])
            validList.append(val)
        else:
            val = int(numbers[0] + numbers[-1])
            validList.append(val)
        

    sum = calculate_sum(validList)

    return sum

def read_file(fileName:str) -> List:
    file = open(fileName, "r")
    content = file.read().split("\n")
    return content

if __name__ == "__main__":
    isTest = False
    expected = 281

    if isTest:
        data_file = "data_day1_pt2_test.txt"
    else:
        data_file = "data_day1.txt"

    fileName = os.path.join(os.path.dirname(__file__), data_file)
    data = read_file(fileName)
    sum = trebuchet_calculation(data)
    
    if isTest:
        if sum == expected:
            print(f"Passed: True")
        else:
            print("Passed: False")
    else:
        print(f"Value: {sum}")