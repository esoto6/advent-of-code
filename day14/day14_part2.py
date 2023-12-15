import os
from pprint import pprint


def count(grid):
    val = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "O":
                val += len(grid) - i
    return val


def roll_rocks(grid):
    new_grid = list()
    for row in grid:
        row = [x for x in row.split("#")]
        row = [sorted(x, reverse=True) for x in row]
        row = ["".join(r) for r in row]
        row = "#".join(row)
        # row = tuple(row)
        new_grid.append(row)
    tuple(new_grid)
    return new_grid


def complete_cycle():
    global grid

    for i in range(4):
        grid = tuple(map("".join, zip(*grid)))
        grid = roll_rocks(grid)
        grid = tuple([row[::-1] for row in grid])
    tuple(grid)
    # pprint(grid)
    # return tuple(grid)


if __name__ == "__main__":
    isTest = False
    expected = 64

    if isTest:
        data_file = "data_day14_test.txt"
    else:
        data_file = "data_day14.txt"

    file = os.path.join(os.path.dirname(__file__), data_file)

    with open(file, "r") as f:
        grid = tuple(f.read().split("\n"))

    cnt = 0
    tgt = 1000000000

    seen = {grid}
    arr = [grid]

    while True:
        cnt += 1

        complete_cycle()
        if grid in seen:
            break
        seen.add(grid)
        arr.append(grid)

    first = arr.index(grid)
    grid_to_count = arr[(tgt - first) % (cnt - first) + first]

    val = count(grid_to_count)
    print(grid)

    if isTest:
        if val == expected:
            print(f"Passed: True")
        else:
            print("Passed: False")
            print(f"Results: {val}")
    else:
        print(f"Results: {val}")
