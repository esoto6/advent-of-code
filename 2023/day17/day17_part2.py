import os
from pprint import pprint
import heapq
from collections import deque


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

        if r == EndR and c == EndC and steps >= 4:
            print(f"Finished!")
            return heat

        if (r, c, dirR, dirC, steps) in seen:
            continue

        seen.add((r, c, dirR, dirC, steps))

        # If steps is greater then three. Need to change directions.
        if steps < 10 and (dirR, dirC) != (0, 0):
            newR = r + dirR
            newC = c + dirC

            if 0 <= newR < len(grid) and 0 <= newC < len(grid[0]):
                heapq.heappush(
                    valid, (heat + grid[newR][newC], newR, newC, dirR, dirC, steps + 1)
                )

        # If steps within range check up, down, left, and right:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # An additional check that steps is greater then 4 and we are not moving.
        if steps >= 4 or (dirR, dirC) == (0, 0):
            for newDirRow, newDirCol in directions:
                if (newDirRow, newDirCol) != (dirR, dirC) and (
                    newDirRow,
                    newDirCol,
                ) != (
                    -dirR,
                    -dirC,
                ):
                    newR = r + newDirRow
                    newC = c + newDirCol
                    if 0 <= newR < len(grid) and 0 <= newC < len(grid[0]):
                        heapq.heappush(
                            valid,
                            (
                                heat + grid[newR][newC],
                                newR,
                                newC,
                                newDirRow,
                                newDirCol,
                                1,
                            ),
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
    expected = 94

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
