


def run():
    
    cur_pos = 50
    counter = 0

    with open("input.txt", "r") as file:
        lines = file.readlines()

        for line in lines:
            direction, steps = line[0], int(line[1:])
            
            if direction == "L":
                cur_pos = (cur_pos - steps) % 100
            else:
                cur_pos = (cur_pos + steps) % 100

            if cur_pos == 0:
                counter += 1

    return counter

if __name__ == "__main__":
    counter = run()
    print(f"Counter: {counter}")
