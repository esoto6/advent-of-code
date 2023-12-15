import os
import pprint


def compare(rows_up, rows_below):
    print(f"Rows Up: {rows_up}")
    print(f"Rows Below: {rows_below}")

    zipped = list(zip(rows_up, rows_below))
    print(zipped)

    total_diff = 0
    for i in range(0, len(zipped)):
        print(zipped[i])
        diff = [x for x, y in zip(list(zipped[i][0]), list(zipped[i][1])) if x != y]

        total_diff += len(diff)

    return total_diff


def find_mirror(block):
    for r in range(1, len(block)):
        rows_up = block[:r][::-1]
        rows_below = block[r:]

        print(len(rows_up))
        print(len(rows_below))

        row_num_min = min(len(rows_up), len(rows_below))

        rows_up = rows_up[:row_num_min]
        rows_below = rows_below[:row_num_min]

        print(rows_up)
        print(rows_below)

        val = compare(rows_up, rows_below)
        if val == 1:
            return r
    else:
        return 0


def main(file):
    with open(file, "r") as f:
        blocks = f.read().split("\n\n")

        total = 0
        for block in blocks:
            block = block.splitlines()
            print(block)

            row = find_mirror(block)

            total += row * 100

            block = list(zip(*block))
            col = find_mirror(block)

            total += col

        return total


if __name__ == "__main__":
    isTest = False
    expected = 400

    if isTest:
        data_file = "data_day13_test.txt"
    else:
        data_file = "data_day13.txt"

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
