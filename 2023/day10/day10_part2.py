from collections import deque
import os
from pprint import pprint
from typing import List
import csv
from itertools import chain


mappings = {
    "|": ["UP", "DOWN"],  # Down, Up
    "-": ["LEFT", "RIGHT"],  # Right, Left
    "L": ["UP", "RIGHT"],  # Up, Right
    "J": ["UP", "LEFT"],  # Up, Left
    "7": ["LEFT", "DOWN"],  # Left, Down
    "F": ["DOWN", "RIGHT"],  # Down, Right
    "S": ["UP", "DOWN", "LEFT", "RIGHT"],  # eVERYTHING
    ".": ["", ""],
}


def count_invs(graph, visited, i, j):
    # WTF
    line = graph[i]
    line = "".join(line)
    count = 0
    for k in range(j):
        if not (i, k) in visited:
            continue
        count += line[k] in {"J", "L", "|"}
    return count


def create_visual_debugging(output_graph):
    with open(
        os.path.join(os.path.dirname(__file__), "visual_debugger.csv"), "w", newline=""
    ) as csvf:
        csvwriter = csv.writer(csvf)
        csvwriter.writerows(output_graph)


def replace_starting(graph, sp, left, right, up, down):
    left_char = graph[left[0]][left[1]]
    right_char = graph[right[0]][right[1]]
    up_char = graph[up[0]][up[1]]
    down_char = graph[down[0]][down[1]]

    print(left_char, right_char, up_char, down_char)

    if "RIGHT" in mappings.get(left_char) and "LEFT" in mappings.get(right_char):
        graph[sp[0]][sp[1]] = "-"
        return graph


def traverse_graph(graph):
    output_graph = []
    counter = 0
    for i in range(len(graph)):
        rows = [" "] * len(graph[0])
        output_graph.append(rows)

    # Get Starting Location
    for i, r in enumerate(graph):
        if "S" in r:
            for i2, c in enumerate(r):
                if c == "S":
                    sr = i
                    sc = i2
                    continue

    visited = {(sr, sc)}
    d = deque([(sr, sc)])

    print(f"Current Value: {graph[sr][sc]}, Starting Row: {sr}, Starting Col: {sc}, ")

    while d:
        cr, cc = d.popleft()
        curr_char = graph[cr][cc]

        print(f"Current Char: {curr_char}")

        # Get Options for curent Char
        directions = mappings.get(curr_char)

        for direction in directions:
            if "UP" in direction:
                r, c = [cr - 1, cc]
                new_char = graph[r][c]

                # Check if new Char can go down
                if "DOWN" in mappings.get(new_char) and (r, c) not in visited:
                    visited.add((r, c))
                    d.append((r, c))

            if "DOWN" in direction:
                r, c = [cr + 1, cc]
                new_char = graph[r][c]

                # Check if enw char can go up
                if "UP" in mappings.get(new_char) and (r, c) not in visited:
                    visited.add((r, c))
                    d.append((r, c))

            if "LEFT" in direction:
                r, c = [cr, cc - 1]
                new_char = graph[r][c]

                if "RIGHT" in mappings.get(new_char) and (r, c) not in visited:
                    visited.add((r, c))
                    d.append((r, c))

            if "RIGHT" in direction:
                r, c = [cr, cc + 1]
                new_char = graph[r][c]

                if "LEFT" in mappings.get(new_char) and (r, c) not in visited:
                    visited.add((r, c))
                    d.append((r, c))

    create_visual_debugging(output_graph)

    # Need to replace S to get inner
    # sr = 49 sc = 46
    graph = replace_starting(
        graph, (sr, sc), (sr, sc - 1), (sr - 1, sc), (sr + 1, sc), (sr - 1, sc)
    )

    ans = 0
    for i, line in enumerate(graph):
        for j in range(len(graph[i])):
            if not (i, j) in visited:
                invs = count_invs(graph, visited, i, j)
                if invs % 2 == 1:
                    ans += 1
    return ans


def main(file):
    with open(file, "r") as f:
        contents = f.read().split("\n")

        graph = []
        for line in contents:
            line = [x for x in line]
            # print(line)
            graph.append(line)

        val = traverse_graph(graph)
        return val


if __name__ == "__main__":
    isTest = True
    expected = 10

    if isTest:
        data_file = "data_day10_test_2.txt"
    else:
        data_file = "data_day10.txt"

    file = os.path.join(os.path.dirname(__file__), data_file)

    val = main(file)

    if isTest:
        if val == expected:
            print(f"Passed: True")
        else:
            print("Passed: False")
            pprint(f"Results: {val}")
    else:
        print(f"Results: {val}")
