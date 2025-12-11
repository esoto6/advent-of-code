from collections import deque, defaultdict
from functools import cache

def load_data(file_name):
    with open(file_name, "r") as file:
        lines = file.readlines()
    
    data = {}
    for line in lines:
        key, sections = line.split(":")
        sections = sections.split()
        # print(f"key: {key}, Sections: {sections}")
        
        data[key] = sections
    #print(data)
    return data

@cache
def count_valid_paths(x, seen_dac, seen_fft):
    print(f"Entering dps: x={x}, seen_dac={seen_dac}, seen_fft={seen_fft}")
    if x == 'out':
        print(f"Reached 'out': seen_dac={seen_dac}, seen_fft={seen_fft}, returning '1'")
        return 1 if seen_dac and seen_fft else 0
    else:
        ans = 0
        for y in graph[x]:
            print(f"Y: {y} X: {graph[x]}")
            new_seen_dac = seen_dac or y == 'dac'
            new_seen_fft = seen_fft or y == 'fft'
            ans += count_valid_paths(y, new_seen_dac, new_seen_fft)
        return ans
        
        
if __name__ == "__main__":
    graph = load_data("input.txt")
    print(f"Graph: {graph}")
    # result = dfs(graph, "svr", "out")

    result = count_valid_paths('svr', False, False)
    print(f"Result: {result}")

