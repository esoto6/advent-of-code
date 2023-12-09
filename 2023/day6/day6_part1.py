import os
from functools import reduce

# Starting Speed  (0 millimeters per Millisecond)
# For each Millisecond speed increases by one millimeter
# How long can we hold the button to win the race.

def main(file: str):
    with open(os.path.join(os.path.dirname(__file__), file)) as f:
        time, distance = f.read().split("\n")

        time = [int(x) for x in time.split(":")[1].split()]
        print(time)

        distance = [int(x) for x in distance.split(":")[1].split()]

    # time = [7, 15, 30] 
    # distance = [9, 40, 200]

        data_set = set(zip(time, distance))
        ways_to_win = []
        for ea in data_set:
            time_to_travel = ea[0]
            record_distance = ea[1]

            print(f"Time to travel: {time_to_travel}, Record Distance: {record_distance}")

            can_win = 0
            for second_held in range(0, time_to_travel):
                distance = second_held * (time_to_travel - second_held)
                if distance > record_distance:
                    print(f"seconds held: {second_held}")
                    can_win += 1
            ways_to_win.append(can_win)
        
        print(ways_to_win)
        product = reduce((lambda x, y: x * y), ways_to_win)
        return product
        
if __name__ == "__main__":

    isTest = False
    expected = 288

    if isTest:
        data_file = "data_day6_test.txt"
    else:
        data_file = "data_day6.txt"

    file = os.path.join(os.path.dirname(__file__), data_file)
    val = main(file)

    if isTest:
        if val == expected:
            print("Passed: True")
        else:
            print("Passed: False")
    else:
        print(f"Result: {val}")