from collections import deque

def create_records():
    lines = []
    with open("input.txt", "r") as file:
        for line in file:
            line = [int(x) for x in line.strip().split(",")]
            lines.append(line)
    print(f"Loaded {len(lines)} points")
    return lines 

def create_compressed_grid(points):
    xs = sorted(set(x for x, y in points))
    ys = sorted(set(y for x, y in points))
    
    # print(f"Compressed grid: {len(xs)} x {len(ys)}")
    
    # Create grid with space for edges (2x size - 1)
    grid = [[0] * (len(ys) * 2 - 1) for _ in range(len(xs) * 2 - 1)]
    # print(f"{grid=}")
    return grid, xs, ys

def mark_edges(grid, xs, ys, points):
    for i in range(len(points)):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % len(points)] 
        
        cx1 = xs.index(x1) * 2 
        cx2 = xs.index(x2) * 2
        cy1 = ys.index(y1) * 2
        cy2 = ys.index(y2) * 2
        
        for cx in range(min(cx1, cx2), max(cx1, cx2) + 1):
            for cy in range(min(cy1, cy2), max(cy1, cy2) + 1):
                grid[cx][cy] = 1
    
    marked = sum(sum(row) for row in grid)
    
    return grid

def flood_fill_outside(grid):
    outside = {(-1, -1)}
    queue = deque([(-1, -1)])
    
    while queue:
        tx, ty = queue.popleft()
        
        for nx, ny in [(tx - 1, ty), (tx + 1, ty), (tx, ty - 1), (tx, ty + 1)]:
            # Skip if out of extended bounds
            if nx < -1 or ny < -1 or nx > len(grid) or ny > len(grid[0]):
                continue
            # Skip if hitting an edge (grid[nx][ny] == 1)
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 1:
                continue
            # Skip if already marked as outside
            if (nx, ny) in outside:
                continue
            
            outside.add((nx, ny))
            queue.append((nx, ny))
    
    print(f"Found {len(outside)} cells outside the loop")
    return outside

def mark_interior_cells(grid, outside):
    
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if (x, y) not in outside:
                grid[x][y] = 1
    
    return grid

def build_prefix_sum_array(grid):
    
    psa = [[0] * len(grid[0]) for _ in range(len(grid))]
    for x in range(len(psa)):
        for y in range(len(psa[0])):
            left = psa[x - 1][y] if x > 0 else 0
            top = psa[x][y - 1] if y > 0 else 0
            topleft = psa[x - 1][y - 1] if x > 0 and y > 0 else 0
            psa[x][y] = left + top - topleft + grid[x][y]
    
    return psa

def is_valid(x1, y1, x2, y2, xs, ys, psa):
    cx1 = xs.index(x1) * 2
    cx2 = xs.index(x2) * 2
    cy1 = ys.index(y1) * 2
    cy2 = ys.index(y2) * 2
    
    if cx1 > cx2:
        cx1, cx2 = cx2, cx1
    if cy1 > cy2:
        cy1, cy2 = cy2, cy1
    
    left = psa[cx1 - 1][cy2] if cx1 > 0 else 0
    top = psa[cx2][cy1 - 1] if cy1 > 0 else 0
    topleft = psa[cx1 - 1][cy1 - 1] if cx1 > 0 and cy1 > 0 else 0
    count = psa[cx2][cy2] - left - top + topleft
    
    expected = (cx2 - cx1 + 1) * (cy2 - cy1 + 1)
    return count == expected

def find_max_rectangle(points, xs, ys, psa):
    max_area = 0
    total_pairs = len(points) * (len(points) - 1) // 2
    checked = 0
    
    for i in range(len(points)):
        x1, y1 = points[i]
        for j in range(i + 1, len(points)):  
            x2, y2 = points[j]
            
            if is_valid(x1, y1, x2, y2, xs, ys, psa):
                width = abs(x2 - x1)
                height = abs(y2 - y1)
                area = (width + 1) * (height + 1)
                
                if area > max_area:
                    max_area = area
                    print(f"New max area {max_area} found between points ({x1},{y1}) and ({x2},{y2})")
    
    return max_area

if __name__ == "__main__":
    points = create_records()
    compressed_grid, xs, ys = create_compressed_grid(points)
    compressed_grid = mark_edges(compressed_grid, xs, ys, points)
    outside = flood_fill_outside(compressed_grid)
    compressed_grid = mark_interior_cells(compressed_grid, outside)
    psa = build_prefix_sum_array(compressed_grid)
    result = find_max_rectangle(points, xs, ys, psa)
    
    print(f"{result=}")