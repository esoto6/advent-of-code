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


def count_steps(sr, sc, steps):
    NORTH = (-1, 0)
    EAST = (0, +1)
    SOUTH = (+1, 0)
    WEST = (0, -1)

    valid_plots = set()
    visited = {(sr, sc)}

    plots = deque([(sr, sc, steps)])

    while plots:
        row, col, idx = plots.popleft()
        # print(f"Row: {row}, Col: {col}")

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

    return len(valid_plots)


def extrapolate():
    size = len(grid)

    sr, sc = start
    grid_width = steps // size - 1

    # Create Odd Grids
    odd = (grid_width // 2 * 2 + 1) ** 2
    # Create Even Grids
    even = ((grid_width + 1) // 2 * 2) ** 2

    # Number of points that can be reached on Odd and Even grids
    odd_points = count_steps(sr, sc, size * 2 + 1)
    even_points = count_steps(sr, sc, size * 2)

    # Handle all Corner Cases
    corner_t = count_steps(size - 1, sc, size - 1)
    corner_r = count_steps(sr, 0, size - 1)
    corner_b = count_steps(0, sc, size - 1)
    corner_l = count_steps(sr, size - 1, size - 1)

    # Handle all small cases
    small_tr = count_steps(size - 1, 0, size // 2 - 1)
    small_tl = count_steps(size - 1, size - 1, size // 2 - 1)
    small_br = count_steps(0, 0, size // 2 - 1)
    small_bl = count_steps(0, size - 1, size // 2 - 1)

    # Handle all Large Blocks
    large_tr = count_steps(size - 1, 0, size * 3 // 2 - 1)
    large_tl = count_steps(size - 1, size - 1, size * 3 // 2 - 1)
    large_br = count_steps(0, 0, size * 3 // 2 - 1)
    large_bl = count_steps(0, size - 1, size * 3 // 2 - 1)

    odd_even = odd * odd_points + even * even_points
    corner_cases = corner_t + corner_r + corner_b + corner_l
    small_cases = (grid_width + 1) * (small_tr + small_tl + small_br + small_bl)
    large_cases = grid_width * (large_tr + large_tl + large_br + large_bl)

    print(
        f"Odd_Even: {odd_even}, Corners: {corner_cases}, Small: {small_cases}, Large: {large_cases}"
    )
    val = odd_even + corner_cases + small_cases + large_cases
    return val


if __name__ == "__main__":
    isTest = True
    expected = 16733044

    if isTest:
        steps = 50
    else:
        steps = 26501365

    if isTest:
        data_file = "data_day21_test.txt"
    else:
        data_file = "data_day21.txt"

    file = os.path.join(os.path.dirname(__file__), data_file)

    grid, start = read_file(file)

    val = extrapolate()

    if isTest:
        if val == expected:
            print(f"Passed: True")
        else:
            print("Passed: False")
            print(f"Results: {val}")
    else:
        print(f"Results: {val}")
