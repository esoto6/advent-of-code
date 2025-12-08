def run():
    cur_pos = 50
 
    counter = 0
 
    with open("sample.txt", "r") as file:
        lines = file.readlines()
 
        for line in lines:
            direction = line[0]
            steps = int(line[1:])
         
            print(f"dir: {direction}, steps: {steps}, pos: {cur_pos}")
            counter += steps // 100
            remainder = steps % 100
 
            print(f"Counter: {counter}, Remainder: {remainder}")
 
            if direction == "L":
                if cur_pos == 0:
                    cur_pos = 100 - remainder
                else:
                    cur_pos = cur_pos - remainder
                    if cur_pos < 0:
                        counter += 1
                        cur_pos = 100 + cur_pos
                    if cur_pos == 0:
                        counter += 1
                        cur_pos = 0  
            else:
                if cur_pos == 0:
                    cur_pos = remainder
                else:              
                    cur_pos = cur_pos + remainder
                    if cur_pos > 100:
                        cur_pos = cur_pos % 100
                        counter += 1
                    if cur_pos == 100:
                        counter += 1
                        cur_pos = 0
 
            print(f"Counter {counter}")
 
        return counter
 
if __name__ == "__main__":
    counter = run()
    print(f"counter: {counter}")
 
