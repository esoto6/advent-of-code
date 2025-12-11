from collections import deque

def load_data(file_name):
    with open(file_name, "r") as file:
        lines = file.readlines()
    
    data = {}
    for line in lines:
        key, sections = line.split(":")
        sections = sections.split()
        print(f"key: {key}, Sections: {sections}")
        
        data[key] = sections
    #print(data)
    return data


def dfs(graph, start, end):
    all_points = []
    stack = deque()

    stack.append((start, [start]))

    while stack:
        current_node, path = stack.pop()

        if current_node == end:
            all_points.append(path)
        else:
            for neighbor in graph[current_node]:
                new_path = path + [neighbor]
                stack.append((neighbor, new_path))
    
    return all_points

                 
    
if __name__ == "__main__":
    graph = load_data("input.txt")
    print(f"Graph: {graph}")
    result = dfs(graph, "you", "out")
    print(f"Length: {len(result)}")
