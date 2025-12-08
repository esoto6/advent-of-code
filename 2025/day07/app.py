

def load_file(file_name: str):
    with open(file_name, "r") as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]

    for line in lines:
        print(line)
    return lines

def get_total_splits(data):
    height, width = len(data), len(data[0]) 
    print(height, width)

    start = data[0].index("S")

    visited = set()
    seen_splits = set()

    beams = [(0, start, "down")]
    print(f"Beams: {beams}")


    while beams:
        row, col, dir = beams.pop()
        print(row, col, dir)
        if (row, col, dir) in visited:
            continue
        visited.add((row,col,dir))

        while 0 <= row < height and 0 <= col < width:
            cell = data[row][col]

            if cell == "^":
                seen_splits.add((row,col))

                if col -1 >= 0:
                    beams.append((row + 1, col -1, "down"))
                if col +1 < len(data[0]):
                    beams.append((row +1, col + 1, "down"))
                
                break

            if dir == "down":
                row += 1
            elif dir == "left":
                col -= 1
                row += 1
            elif dir == "right":
                col += 1
                row += 1

    return len(seen_splits)
    
if __name__ == "__main__":
    data = load_file("input.txt")
    result = get_total_splits(data)
    print(f"Result: {result}")