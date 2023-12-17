import os
from collections import deque


def create_energy(grid, start):
    seen = set()
    valid = deque(start)

    while valid:
        dir_map = {"l": (0, -1), "r": (0, 1), "u": (-1, 0), "d": (1, 0)}

        r, c, direction = valid.popleft()

        if direction in dir_map.keys():
            nr, nc = dir_map.get(direction)
            r += nr
            c += nc

            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
                continue

            char = grid[r][c]
            # print(f"Char: {char}, Row: {r}, Col: {c}, Direction: {direction}")

            if (
                char == "."
                or (char == "-" and direction in ["l", "r"])
                or (char == "|" and direction in ["u", "d"])
            ):
                if (r, c, direction) not in seen:
                    seen.add((r, c, direction))
                    valid.append((r, c, direction))
            elif char == "\\":
                if direction == "l":
                    if (r, c, "u") not in seen:
                        seen.add((r, c, "u"))
                        valid.append((r, c, "u"))
                if direction == "r":
                    if (r, c, "d") not in seen:
                        seen.add((r, c, "d"))
                        valid.append((r, c, "d"))
                if direction == "u":
                    if (r, c, "l") not in seen:
                        seen.add((r, c, "l"))
                        valid.append((r, c, "l"))
                if direction == "d":
                    if (r, c, "r") not in seen:
                        seen.add((r, c, "r"))
                        valid.append((r, c, "r"))
                if direction == "l":
                    if (r, c, "u") not in seen:
                        seen.add((r, c, "u"))
                        valid.append((r, c, "u"))
            elif char == "/":
                if direction == "r":
                    if (r, c, "u") not in seen:
                        seen.add((r, c, "u"))
                        valid.append((r, c, "u"))
                if direction == "l":
                    if (r, c, "d") not in seen:
                        seen.add((r, c, "d"))
                        valid.append((r, c, "d"))
                if direction == "u":
                    if (r, c, "r") not in seen:
                        seen.add((r, c, "r"))
                        valid.append((r, c, "r"))
                if direction == "d":
                    if (r, c, "l") not in seen:
                        seen.add((r, c, "l"))
                        valid.append((r, c, "l"))
            else:
                if char == "|" and direction in ["l", "r"]:
                    if (r, c, "u") not in seen:
                        seen.add((r, c, "u"))
                        valid.append((r, c, "u"))
                    if (r, c, "d") not in seen:
                        seen.add((r, c, "d"))
                        valid.append((r, c, "d"))

                if char == "-" and direction in ["u", "d"]:
                    if (r, c, "r") not in seen:
                        seen.add((r, c, "r"))
                        valid.append((r, c, "r"))
                    if (r, c, "l") not in seen:
                        seen.add((r, c, "l"))
                        valid.append((r, c, "l"))

    coordinates = {(r, c) for (r, c, dir) in seen}
    # print(f"Start: {start}, Energy: {len(coordinates)}")
    return len(coordinates)


def main(file):
    with open(file, "r") as f:
        grid = f.read().split("\n")

    max_value = 0
    # Check Rows
    for i in range(0, len(grid)):
        # Left to Right
        if i == 51:
            print("here")
        max_value = max(max_value, create_energy(grid, [(i, -1, "r")]))
        # Right To Left
        max_value = max(max_value, create_energy(grid, [(i, len(grid), "l")]))
    # Check Cols
    for i in range(0, len(grid[0])):
        #     # Up to Down
        max_value = max(max_value, create_energy(grid, [(-1, i, "d")]))
        #     # Down to Up
        max_value = max(max_value, create_energy(grid, [(len(grid), i, "u")]))

    return max_value


if __name__ == "__main__":
    isTest = False
    expected = 51

    if isTest:
        data_file = "data_day16_test.txt"
    else:
        data_file = "data_day16.txt"

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
