
import os
from math import gcd


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
    
    # print(network)
    return network

def main(file):
    with open(file, "r") as f:
        sequence, diagram = f.read().strip().split("\n\n")
        # print(sequence)
        # print(diagram)
        # Need to store diagram into some structure
        diagram = create_network(diagram)


        # Find all Starting Points:
        positions = [x for x in diagram.keys() if x.endswith("A")]
        print(f"Starting Locations: {len(positions)}")

        cycles = []
        # https://www.youtube.com/watch?v=_nnxLcrwO_U minute 7:37
        for current in positions:
            cycle = []

            current_steps = sequence
            step_count = 0
            first_z = None

            while True:
                while step_count == 0 or not current.endswith("Z"):
                    step_count += 1
                    
                    if current_steps[0] == "L":
                        current = diagram[current][0]
                    else:
                        current = diagram[current][1]

                    current_steps = current_steps[1:] + current_steps[0]
                
                cycle.append(step_count)

                if first_z is None:
                    first_z = current
                    step_count = 0
                elif current == first_z:
                    break

            cycles.append(cycle)
        
        # Least Common Multiples?
        print(cycles)

        nums = [cycle[0] for cycle in cycles]

        print(nums)

        lcm = nums.pop()

        # Greatest Common Divisor
        for num in nums:
            lcm = lcm * num // gcd(lcm, num)
        
        print(lcm)
        return lcm
        #This took way to long process!!!!!!!
        # while not all([x.endswith("Z") for x in current_locations]):
        #     steps_counter += 1

        #     for i, each in enumerate(current_locations):
        #         if sequence[0] == "L":
        #             current_locations[i] = diagram[current_locations[i]][0]
        #         else:
        #             current_locations[i] = diagram[current_locations[i]][1]

        #     sequence = sequence[1:] + sequence[0]


        # return steps_counter

if __name__ == "__main__":
    isTest = False
    expected = 6

    if isTest:
        data_file = "data_day8_test_2.txt"
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
