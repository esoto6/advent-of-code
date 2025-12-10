

        
def create_grid():
    grid = []
    with open("input.txt", "r") as file:
        
        for line in file:
            x,y,z = [int(x) for x in line.strip().split(",")]
            grid.append((x,y,z))

    return grid

def calculate_euclidean_distance(grid):
    distances_list = []

    for i, (x,y,z) in enumerate(grid):
        # print(i, x,y,z)
        for j, (x2,y2,z2) in enumerate(grid):
            dist = (x - x2)**2 + (y - y2) **2 + (z - z2) **2
            if i > j:
                distances_list.append((dist, i, j))
    distances_list.sort(key=lambda x: x[0])

    return distances_list

def create_junctions(dist_list, grid):
    junctions = [{i} for i in range(len(grid))]

    for dist, pt1, pt2 in dist_list:

        # print(f"Printing: Dist={dist}, Pos 1={pt1}, Pos 2={pt2}")
        
        matching_idxs = []
        for idx, junc in enumerate(junctions):
            # print(idx, junc)
            if pt1 in junc or pt2 in junc:
                matching_idxs.append(idx)

        if not matching_idxs:
            junctions.append({pt1, pt2})
        else:
            base_idx = matching_idxs[0]
            junctions[base_idx].update([pt1,pt2])

            for extra in reversed(matching_idxs[1:]):
                junctions[base_idx].update(junctions[extra])
                del junctions[extra]

        if len(junctions) == 1:
            print("This is down to one.")
            print(grid[pt1], grid[pt2])
            result = grid[pt1][0] * grid[pt2][0]
            return result


if __name__ == "__main__":
    grid = create_grid() 
    dist_list = calculate_euclidean_distance(grid)
    junctions = create_junctions(dist_list, grid)

    print(f"Result: {junctions}")

        
