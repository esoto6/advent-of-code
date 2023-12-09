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

            # Get First item from first list
            first_val = mapped_list[0][0]
            print(f"First Val: {first_val}")
            
            next_item = 0
            
            for i, v in reversed(list(enumerate(mapped_list))):
                print(f"I: {i}, v: {v[0]}, Next_item: {next_item}")
                next_item = v[0] - next_item 
                print(f"Next item: {next_item}")
            print(f"Mapped List: {mapped_list}, Next: {next_item}")
            sum += next_item
        return sum



if __name__ == "__main__":
    isTest = False
    expected = 5

    if isTest:
        data_file = "data_day9_test_2.txt"
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