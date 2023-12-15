import os


def main(file):
    with open(file, "r") as f:
        lines = f.read().split(",")

    sum = 0
    for line in lines:
        # Process line
        val = 0
        for char in line:
            val = (val + ord(char)) * 17 % 256
        sum += val
    # print(sum)
    return sum


if __name__ == "__main__":
    isTest = True
    expected = 1320

    if isTest:
        data_file = "data_day15_test.txt"
    else:
        data_file = "data_day15.txt"

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
