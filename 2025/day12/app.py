import math

def read_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.read()

    lines = lines.split("\n\n")

    last_line = lines[-1]
    last_line = [x for x in last_line.split("\n") if x]
    
    presents_shapes = {}
    regions = []

    for line in lines[:-1]:
        l = line.split(":")[0]

        if 'x' not in l:
            index = int(l)
            right = line.split(":")[1].split("\n")
            right = [r for r in right  if r.strip()]
            count = sum(1 for row in right for x in row if x == "#")
            presents_shapes[index] = (count, right)
    
    for line in last_line:
        l = line.split(":")[0]
        
        if 'x' in l:
            shape = l 
            right = [x for x in line.split(":")[1].strip().split("\n") if x]
            right = [int(x) for item in right for x in item.split()]
            regions.append((shape, right))
        else:
            print(f"No match?")

    print(f"Presents Shapes: {presents_shapes}")
    print(f"Regions: {regions}")

    return presents_shapes, regions

def check_fits(grid_size, indexes, presents_shapes, threshold):
    print(f"--------------------------------")

    thresh = int(round(grid_size * threshold))
    print(thresh)
    presents_size = 0
    presents = []
    for idx, val in enumerate(indexes):
        presents.append(presents_shapes[idx][0] * val)
    presents_size = sum(x for x in presents)

    print(f"{presents_size=}, {grid_size=}, {thresh=}")
    if presents_size >= thresh:
        return 0
    return 1

if __name__ == "__main__":
    file_path = 'input.txt'
    presents_shapes, regions = read_file(file_path)

    count = 0
    for grid_size, indexes in regions:
        grid_size = math.prod([int(x) for x in grid_size.split("x")])

        print(f"Checking grid size: {grid_size} with presents: {indexes}")
        val = check_fits(grid_size, indexes, presents_shapes, threshold=0.85)        
        count += val

    print(f"Total fitting presents: {count}")

