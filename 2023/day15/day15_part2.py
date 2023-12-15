import os


def calculate_total(boxes, focals):
    #   rn: 1 (box 0) * 1 (first slot) * 1 (focal length) = 1
    #   cm: 1 (box 0) * 2 (second slot) * 2 (focal length) = 4

    total = 0
    for idx, box in enumerate(boxes):
        print(idx, box)
        for i, v in enumerate(box):
            print(f"Box Row #: {idx + 1}, Lens Pos: {i + 1}, Focal Length: {focals[v]}")
            sum = ((idx + 1) * (i + 1)) * focals[v]
            print(f"Sum: {sum}")

            total += sum
    return total


def calulate_hash(chars):
    val = 0
    for char in chars:
        val = (val + ord(char)) * 17 % 256
    # sum += val
    # return su
    return val


def main(file):
    boxes = [[] for i in range(256)]
    focals = {}
    with open(file, "r") as f:
        lines = f.read().split(",")

    # sum = 0
    for line in lines:
        # Split by = or -
        if "=" in line:
            isAdd = True
            chars, focal_length = line.split("=")
        else:
            isAdd = False
            chars, focal_length = line.split("-")

        box_index = calulate_hash(chars)

        if isAdd:
            # Add to list
            if chars not in boxes[box_index]:
                boxes[box_index].append(chars)

            focals[chars] = int(focal_length)
        else:
            # Remove from list
            if chars in boxes[box_index]:
                boxes[box_index].remove(chars)

    # print(boxes)
    # Calculate total
    sum = calculate_total(boxes, focals)

    # Process line

    print(sum)
    return sum


if __name__ == "__main__":
    isTest = False
    expected = 145

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
