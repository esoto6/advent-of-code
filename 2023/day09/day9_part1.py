import os

# Example 1:
# [ 0, 3, 6, 9, 12, 15 ]
# [   3, 3, 3, 3, 3    ]
# [    0, 0, 0, 0      ]

def main(file):
    with open(file, "r") as f:
        contents = f.read().strip().split("\n")

        sum = 0
        for line in contents:
            numbers = line.split(" ")
            numbers = [int(x) for x in numbers]
            mapped_list = []
            mapped_list.append(numbers)

            # Generate Successive Numbers
            while not all([x == 0 for x in mapped_list[-1]]):
                last_list = mapped_list[-1]

                differences = []
                for i in range(len(last_list)-1):
                    differences.append(last_list[i+1] - last_list[i])
                print(f"Differences: {differences}")

                mapped_list.append(differences)
                del differences
            # print(mapped_list)

            # Get Last item from first list
            last_val = mapped_list[0][-1]
            print(f"Last Val: {last_val}")
            
            next_item = 0
            for i, v in reversed(list(enumerate(mapped_list))):
                next_item += v[-1]
            print(f"Mapped List: {mapped_list}, Next: {next_item}")
            sum += next_item
        return sum



if __name__ == "__main__":
    isTest = True
    expected = 114

    if isTest:
        data_file = "data_day9_test.txt"
    else:
        data_file = "data_day9.txt"
    
    file = os.path.join(os.path.dirname(__file__), data_file)

    val = main(file)

    if isTest:
        if val == expected:
            print("Passed: True")
        else:
            print("Passed: False")
    else:
        print(f"Results: {val}")