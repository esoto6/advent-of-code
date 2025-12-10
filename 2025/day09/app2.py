import math


def create_records():
    lines = []
    with open("sample.txt", "r") as file:
        for line in file:
            line = [int(x) for x in line.strip().split(",")]
            lines.append(line)
        print(lines)
    return lines 

def is_range_valid(grid, x1, y1, x2, y2):
    min_x, max_x = min(x1, x2), max(x1, x2)
    min_y, max_y = min(y1, y2), max(y1, y2)

    for i in range(min_y, max_y + 1):
        for j in range(min_x, max_x + 1):
            if grid[i][j] != "X":
                return False
    return True

def get_largest_volume(records, grid):
    max = 0
    for i, (x1,y1) in enumerate(records):
        for j, (x2,y2) in enumerate(records):
            width, height = abs(x2 - x1), abs(y2 - y1)
            area = (width +1 ) * (height + 1)
            if area > max:
                isValid = is_range_valid(grid, x1, y1, x2, y2)
                if isValid:
                    area = (width + 1) * (height + 1)
                    print(f"{width=}, {height=}, {area=}")
                    if area > max:
                        max = area 
    return max

def create_grid(records):
    max_y, max_x = max(y for (x,y) in records), max(x for (x,y) in records)
    min_y, min_x = min(y for (x,y) in records), min(x for (x,y) in records)
    
    print(f"Ranges: {min_x=}, {max_x=}, {min_y=}, {max_y=}")
    grid = [["." for _ in range(max_x + 2)] for _ in range(max_y + 2)]
 
    for i, (x,y) in enumerate(records):
        grid[y][x] = "X"
 
    for i, row in enumerate(grid): 
        l, r = 0, len(row) - 1
        while l != r:
            if row[l] == "X" and row[r] == "X":
                print("True")
                for j in range(l, r):
                    grid[i][j] = 'X'
                break
            elif row[l] == "X" and row[r] != "X":
                r -= 1
            else:
                l += 1

    for col in range(len(grid[0])):
        t, b = 0, len(grid) - 1
        while t != b:
            if grid[t][col] == "X" and grid[b][col] == "X":
                for j in range(t, b):
                    grid[j][col] = 'X'
                break
            elif grid[t][col] != "X" and grid[b][col] == "X":
                t += 1
            else:
                b -= 1

    print("After filling columns:")
    for row in grid:
        print(row) 

    return grid



if __name__ == "__main__":
    records = create_records()
    grid = create_grid(records)
    largest = get_largest_volume(records, grid)   
    print(f"Largest area: {largest}")
