import os


    
def is_possible(file):
    max = {"red": 12, "green":13, "blue":14}
    valid = 0
    with open(file, "r") as f:
        lines = f.readlines()
        for line in lines:
            isInvalid = False
            line = line.strip()
            # print(line)
            game, line = line.split(":")
            idx = game.split(" ")[1]
            # print(idx)
            # print(idx, line)
            for session in line.split(";"):
                for cubes in session.split(','):
                    n, color = cubes.split()
                    # print(n, color)
                    if max[color] < int(n):
                        print(f"IDX: {idx} is not valid")
                        isInvalid = True
                        break
            if isInvalid:
                pass
            else:
                print(f"IDX: {idx} is valid")
                valid = valid + int(idx)
        return valid

if __name__ == "__main__":

    isTest = False
    expected = 8

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