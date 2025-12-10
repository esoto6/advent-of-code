import math

def create_records():
    lines = []
    with open("input.txt", "r") as file:
        for line in file:
            line = [int(x) for x in line.strip().split(",")]
            lines.append(line)
        print(lines)
    return lines 

def get_largest_volume(records):
    max = 0
    for i, (x1,y1) in enumerate(records):
        for j, (x2,y2) in enumerate(records):
            width, height = abs(x2 - x1), abs(y2 - y1)
            print(f"{width=}, {height=}, {(width + 1) * (height + 1)=}")
            area = (width + 1) * (height + 1)
            if area > max:
                max = area 
    return max

if __name__ == "__main__":
    grid = create_records()
    print(grid)
    largest = get_largest_volume(grid)   
    print(largest)