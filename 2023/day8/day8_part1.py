
import os


def create_network(diagrams):
    network = {}
    diagrams = diagrams.strip().split("\n")
    for map in diagrams:
        left, right = map.strip().split(" = ")
        left = left.strip()
        right = right.replace(" ","")
        right = right.replace("(", "").replace(")", "")
        right = right.split(",")
        # print(left, right)

        network[left] = (right[0], right[1])
    
    print(network)
    return network

def main(file):
    with open(file, "r") as f:
        sequence, diagram = f.read().strip().split("\n\n")
        # print(sequence)
        # print(diagram)
        # Need to store diagram into some structure
        diagram = create_network(diagram)

        steps_counter = 0
        current_location = "AAA"
        while not current_location == "ZZZ":
            steps_counter += 1

            # current_location = diagram[current_location][0]

            if sequence[0] == "L":
                current_location = diagram[current_location][0]
            else:
                current_location = diagram[current_location][1]

            sequence = sequence[1:] + sequence[0]


        return steps_counter

if __name__ == "__main__":
    isTest = False
    #Test 1 == 2, Test 2 == 6
    expected = 2
    
    if isTest:
        data_file = "data_day8_test_1.txt"
    else:
        data_file = "data_day8.txt"
    
    
    file = os.path.join(os.path.dirname(__file__), data_file)
    
    val = main(file)

    if isTest:
        if val == expected:
            print("Passed: True")
        else:
            print("Passed: False")
    else:
        print(f"Result: {val}")
