import os
from collections import defaultdict, deque
import queue
from math import lcm, prod


def create_modules(file):
    with open(file, "r") as f:
        contents = f.read().split("\n")
        print(contents)

        modules = defaultdict(lambda: {"dest": [], "type": None, "state": dict()})

        for line in contents:
            print(f"Line: {line}")
            name, destiantions = line.strip().split(" -> ")
            print(f"Name: {name}, Destinations: {destiantions}")

            type, state = None, False
            if name[0] in ["%", "&"]:
                type, name = name[0], name[1:]
                print(f"Type: {type}, Name: {name}")

            module = modules[name]

            module["dest"] = destiantions.split(", ")
            module["type"] = type

            if type == "%":
                module["state"] = False

            for d in module["dest"]:
                if isinstance(modules[d]["state"], dict):
                    modules[d]["state"][name] = False
    print(modules)
    return modules


def count_buttons(modules):
    # counter = {False: 0, True: 0}
    cycles = {}

    # Low is False, High is True
    for i in range(1, 5000):
        pulses = queue.Queue()

        pulses.put(("button", False, "broadcaster"))

        while not pulses.empty():
            (
                sender,
                pulse,
                receiver,
            ) = pulses.get()

            # counter[pulse] += 1

            if modules[receiver]["type"] == "&":
                # Update state in memory
                modules[receiver]["state"][sender] = pulse
                pulse = not all(modules[receiver]["state"].values())

                if pulse == False and receiver not in cycles:
                    cycles[receiver] = i

            elif modules[receiver]["type"] == "%":
                if pulse == True:
                    continue
                pulse = modules[receiver]["state"] = not modules[receiver]["state"]

            for d in modules[receiver]["dest"]:
                pulses.put((receiver, pulse, d))

    print(prod(cycles.values()))
    return prod(cycles.values())


if __name__ == "__main__":
    isTest = False
    # expected = 32000000
    expected = 856482136

    if isTest:
        data_file = "data_day20_test.txt"
    else:
        data_file = "data_day20.txt"

    file = os.path.join(os.path.dirname(__file__), data_file)

    modules = create_modules(file)

    val = count_buttons(modules)

    if isTest:
        if val == expected:
            print(f"Passed: True")
        else:
            print("Passed: False")
            print(f"Results: {val}")
    else:
        print(f"Results: {val}")
