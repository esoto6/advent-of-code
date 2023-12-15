import os
import pprint


# This passes the test case but can't figure out what im doing wrong here.
# def find_mirror(block):
#     for i in range(1, len(block)):
#         if i + 1 <= len(block) - 1:
#             if block[i] == block[i + 1]:
#                 isMatch = True
#                 idx_u_found = i
#                 idx_d_found = i + 1

#                 idx_u = idx_u_found
#                 idx_d = idx_d_found

#                 # Find longest side
#                 for j in range(1, len(block) - 1):
#                     try:
#                         if block[idx_u - 1] == block[idx_d + 1]:
#                             if (idx_u - 1 == 0) or (idx_d + 1 == len(block) - 1):
#                                 print(f"Idx_U: {idx_u}")
#                                 print(f"i: {idx_u_found}")

#                                 if idx_u == 0:
#                                     # If it is equal to zero get original + 1
#                                     return idx_u_found

#                                 else:
#                                     return idx_u_found + 1
#                             else:
#                                 idx_u -= 1
#                                 idx_d += 1
#                         else:
#                             isMatch = False
#                             break
#                     except:
#                         isMatch = False
#                         break
#                 if isMatch == False:
#                     continue
#     return 0


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

        if rows_up == rows_below:
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
    expected = 405

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
