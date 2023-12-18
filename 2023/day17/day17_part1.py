import os
from pprint import pprint
import heapq
from collections import deque


## Initial Try:
#### Didn't work ###

# seen.add((heat, r, c, dir))
#     # Check up to three spaces up, down, left and right
#     if dir in ["lr", "rl"]:
#         # If direction == "r" we can only go up and down
#         new_dir = "c"
#         options = [(0, +1), (0, +2), (0, +3), (0, -1), (0, -2), (0, -3)]
#     if dir == "c":
#         # If we are traversing columns we can only go left or right
#         new_dir = "r"
#         options = [(-1, 0), (-2, 0), (-3, 0), (+1, 0), (+2, 0), (+3, 0)]

#     # best_option = None
#     for option in options:
#         # New Row, New Col
#         nr = r + option[0]
#         nc = c + option[1]

#         # print(nr, nc)

#         if nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[0]):
#             continue
#         # else:
#         #     heat = grid[nr][nc]

#         # if best_option is None:
#         #     best_option = (heat, nr, nc, new_dir)
#         # else:
#         #     if heat < best_option[0]:
#         #         best_option = (heat, nr, nc, new_dir)

#         # seen.add(best_option)
#         heapq.heappush(valid, (heat + grid[nr][nc], nr, nc, new_dir))

# print(seen)


def shortest_path(grid):
    # Starting Point: (heat, r, c, dirC, dirR, steps)
    valid = [(0, 0, 0, 0, 0, 0)]

    # End Location of Grid
    EndR = len(grid) - 1
    EndC = len(grid[0]) - 1

    seen = set()
    heapq.heapify(valid)

    while valid:
        # Heat, Row, Column, Direction Row, Direction Column, Steps
        heat, r, c, dirR, dirC, steps = heapq.heappop(valid)
        # print(f"Heat: {heat}, Row: {r}, Col: {c}, Direction: {dir}")

        if r == EndR and c == EndC:
            print(f"Finished!")
            return heat

        if (r, c, dirR, dirC, steps) in seen:
            continue

        seen.add((r, c, dirR, dirC, steps))

        # If steps is greater then three. Need to change directions.
        if steps < 3 and (dirR, dirC) != (0, 0):
            newR = r + dirR
            newC = c + dirC

            if 0 <= newR < len(grid) and 0 <= newC < len(grid[0]):
                heapq.heappush(
                    valid, (heat + grid[newR][newC], newR, newC, dirR, dirC, steps + 1)
                )

        # If steps within range check up, down, left, and right:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for newDirRow, newDirCol in directions:
            if (newDirRow, newDirCol) != (dirR, dirC) and (newDirRow, newDirCol) != (
                -dirR,
                -dirC,
            ):
                newR = r + newDirRow
                newC = c + newDirCol
                if 0 <= newR < len(grid) and 0 <= newC < len(grid[0]):
                    heapq.heappush(
                        valid,
                        (heat + grid[newR][newC], newR, newC, newDirRow, newDirCol, 1),
                    )


def main(file):
    with open(file, "r") as f:
        grid = f.read().split("\n")
        grid = [[int(x) for x in row] for row in grid]
        # pprint(grid)

    val = shortest_path(grid)

    return val


if __name__ == "__main__":
    isTest = False
    expected = 102

    if isTest:
        data_file = "data_day17_test.txt"
    else:
        data_file = "data_day17.txt"

    file = os.path.join(os.path.dirname(__file__), data_file)

    val = main(file)

    if isTest:
        if val == expected:
            print(f"Passed: True")
        else:
            print("Passed: False")
            print(f"Results: {val}")
    else:
        print(f"Results: {val}")
