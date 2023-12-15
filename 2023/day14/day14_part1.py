import os


def count(grid):
    val = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "O":
                val += len(grid) - i
    return val


def roll_rocks(row):
    row = [x for x in row.split("#")]
    # print(rows)

    row = [sorted(x, reverse=True) for x in row]
    row = ["".join(r) for r in row]
    row = "#".join(row)
    print(row)
    return row


def main(file):
    with open(file, "r") as f:
        grid = f.read().split("\n")

        # Transpose Rows
        grid = list(map("".join, zip(*grid)))
        print(grid)

        final_grid = list()
        sum = 0
        for row in grid:
            new = roll_rocks(row)
            final_grid.append(new)
        print(grid)
        print(final_grid)
        final_grid = list(map("".join, zip(*final_grid)))
        val = count(final_grid)
        sum += val
    return sum


if __name__ == "__main__":
    isTest = False
    expected = 136

    if isTest:
        data_file = "data_day14_test.txt"
    else:
        data_file = "data_day14.txt"

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
