import os
from collections import deque


def read_file(file):
    with open(file, "r") as f:
        grid = f.read().strip().split("\n")

    grid = [[x for x in row] for row in grid]
    print(grid)

    # Get Starting location
    start = (0, 0)
    for idx, row in enumerate(grid):
        if "S" in row:
            for i, col in enumerate(row):
                if col == "S":
                    start = (idx, i)

    return grid, start


def count_steps(grid, start, steps):
    NORTH = (-1, 0)
    EAST = (0, +1)
    SOUTH = (+1, 0)
    WEST = (0, -1)

    valid_plots = set()
    visited = {(start)}

    plots = deque([(start[0], start[1], steps)])

    while plots:
        row, col, idx = plots.popleft()
        print(f"Row: {row}, Col: {col}")

        # If even record:
        if idx % 2 == 0:
            valid_plots.add((row, col))

        if idx == 0:
            continue

        for dir in [NORTH, EAST, SOUTH, WEST]:
            nr = row + dir[0]
            nc = col + dir[1]

            if (nr < 0) or (nr > len(grid) - 1) or (nc < 0) or (nc > len(grid[0]) - 1):
                continue

            if grid[nr][nc] == "#":
                continue
            else:
                if (nr, nc) not in visited:
                    visited.add((nr, nc))
                    plots.append((nr, nc, idx - 1))

    # last_key = list(seen.keys())[-1]
    # print(f"Last Steps: {len(seen[last_key])}")
    # print(f"Visited: {len(visited)}")
    return len(valid_plots)


if __name__ == "__main__":
    isTest = False
    expected = 16

    if isTest:
        steps = 6
    else:
        steps = 64

    if isTest:
        data_file = "data_day21_test.txt"
    else:
        data_file = "data_day21.txt"

    file = os.path.join(os.path.dirname(__file__), data_file)

    grid, start = read_file(file)

    val = count_steps(grid, start, steps=steps)

    if isTest:
        if val == expected:
            print(f"Passed: True")
        else:
            print("Passed: False")
            print(f"Results: {val}")
    else:
        print(f"Results: {val}")
