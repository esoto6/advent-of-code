
def get_rolls(grid):
    rolls_removed = 0
    

    to_continue = True
    while to_continue:
        total_removed = 0 
        idxs = set()
        directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1),  (1,0),  (1,1)]

        rows, cols = (len(grid), len(grid[0]))

        for i in range(rows):
            for j in range(cols):

                # print(f"Current Position: {i=}, {j=}, Grid={grid[i][j]}, Total Removed = {total_removed}")

                if grid[i][j] != "@":
                    # print("Can skip!")
                    continue
                
                can_remove = 0
                # print(f"Starting Counter {can_remove=}")
                for direction in directions:
                    
                    x, y = (i + direction[0], j + direction[1])
                    # print(f"Checking {x=}, {y=}")

                    if 0 <= x < rows and 0 <= y < cols and grid[x][y] == '@':                   
                        can_remove += 1
                        # print(f"INCREMENTING {can_remove=}")

                        if can_remove >= 4:
                            break
                if can_remove < 4:
                    # print("Increementing")
                    total_removed += 1
                    idxs.add((i,j))

        print(f"Lenght of idxs {len(idxs)}, {idxs}")
        print(f"Total Removed= {total_removed}")

        if total_removed != 0:

            for update_x, update_y in idxs:
                # for idx in idxs:
                    # print(idx)
                    # print(update_x, update_y)
                    # print(grid[update_x][update_y])
                grid[update_x][update_y] = "."

            rolls_removed += total_removed
            print(f"Rolls Removed: {rolls_removed}")
        else:
            to_continue = False
        
    print(f"Going to return? {rolls_removed=}, {total_removed=}")



    return rolls_removed


def create_grid():
    grid = []
    with open("input.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            row = [x for x in line]
            grid.append(row)
    return grid

def run():
    grid = create_grid()
    rolls = get_rolls(grid)
   
    return rolls

if __name__ == "__main__":
    result = run()
    print(f"Result = {result}")