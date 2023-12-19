import os

# This did not work....
# def calculate_area(locs):
# locs = sorted(locs)
# area = 0

# l = 0
# r = 1
# isEnd = False
# isLastRow = False

# while r < len(locs):
#     if r == len(locs) - 1:
#         # Calulate The Remaining
#         isLastRow = True
#         r += 1

#     else:
#         if locs[l][0] == locs[r][0]:
#             r += 1
#         else:
#             isEnd = True

#     # Calculate Sum For Row
#     if isLastRow or isEnd:
#         sum = abs(locs[r - 1][1] - locs[l][1]) + 1
#         print(f"Left: {locs[l]}, Right: {locs[r-1]}, Caclulated: {sum}")
#         area += sum


#         isEnd = False
#         isLastRow = False
#         l = r
#         r += 1
# print(area)
# return area
def calculate_area(locs, distance):
    area = 0
    total = 0
    length = 0
    print(locs[:-1])
    print(locs[1:])
    for (x1, y1), (x2, y2) in zip(locs[:-1], locs[1:]):
        print(x1, y1), (x2, y2)

        area += (x2 - x1) * (y2 + y1)

        print(area)

    total = abs(int(area) // 2 + distance // 2) + 1
    return total


def create_map(instructions):
    dir_mapping = {"U": [-1, 0], "D": [1, 0], "L": [0, -1], "R": [0, +1]}

    locs = [(0, 0)]
    current_R = 0
    current_C = 0

    distance = 0
    for inst in instructions:
        dir, steps, color = inst

        dirR, dirC = dir_mapping.get(dir)
        distance += int(steps)
        current_R = int(steps) * dirR + current_R
        current_C = int(steps) * dirC + current_C

        # print(current_R, current_C)
        locs.append((current_R, current_C))
    count = calculate_area(locs, distance)

    return count


def main(file):
    with open(file, "r") as f:
        instructions = f.read().split("\n")

        # for row in instructions:
        instructions = [[x for x in row.split()] for row in instructions]

        count = create_map(instructions)
    return count


if __name__ == "__main__":
    isTest = False
    expected = 62

    if isTest:
        data_file = "data_day18_test.txt"
    else:
        data_file = "data_day18.txt"

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
