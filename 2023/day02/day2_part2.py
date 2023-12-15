import os


    
def is_possible(file):
    max = {"red": 12, "green":13, "blue":14}
    valid = 0
    with open(file, "r") as f:
        lines = f.readlines()
        for line in lines:
            isInvalid = False
            line = line.strip()
            score = 1
            game, line = line.split(":")
            idx = game.split(" ")[1]
            max_possible = {"red":0, "green":0, "blue":0}
            for session in line.split(";"):
                for cubes in session.split(','):
                    n, color = cubes.split()
                    if max_possible[color] < int(n):
                        max_possible[color] = int(n)
                        print(max_possible)
            
            for i, key in enumerate(max_possible.keys()):
                score = score * max_possible[key]
            print(score)
            valid += score

            
        return valid

if __name__ == "__main__":

    isTest = False
    expected = 2286

    if isTest:
        data_file = "data_day2_test.txt"
    else:
        data_file = "data_day2.txt"

    file = os.path.join(os.path.dirname(__file__), data_file)
    count = is_possible(file)

    if isTest:
        if count == expected:
            print("Passed: True")
        else:
            print("Passed: False")
    else:
        print(f"Value: {count}")