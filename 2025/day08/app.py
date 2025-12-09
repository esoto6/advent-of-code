
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

    print(distances_list)

    for dist, pos1, pos2 in distances_list:
        print(dist, pos1, pos2)
    return distances_list

def create_junctions(dist_list, grid):
    junctions = [{i} for i in range(len(grid))]
    print(len(junctions))
    print(junctions)

    count = 0 

    for dist, pt1, pt2 in dist_list:
        
        if count == 1000: return junctions

        print(f"Printing: Dist={dist}, Pos 1={pt1}, Pos 2={pt2}")
        matching_idxs = []
        for idx, junc in enumerate(junctions):
            print(idx, junc)
            if pt1 in junc or pt2 in junc:
                print(f"{matching_idxs=}, {idx=}")
                matching_idxs.append(idx)

        if not matching_idxs:
            print("Here one")
            junctions.append({pt1, pt2})
            print(junctions)
        else:
            print("Here two")
            base_idx = matching_idxs[0]
            junctions[base_idx].update([pt1,pt2])

            for extra in reversed(matching_idxs[1:]):
                junctions[base_idx].update(junctions[extra])
                del junctions[extra]

            print(junctions)
        count += 1
    print(junctions)
    return junctions

if __name__ == "__main__":
    grid = create_grid() 
    dist_list = calculate_euclidean_distance(grid)
    junctions = create_junctions(dist_list, grid)

    top_junc = sorted([len(x) for x in junctions], reverse=True)
    print(top_junc)
    result = top_junc[0] * top_junc[1] * top_junc[2] 
    print(f"Result: {result}")

        
