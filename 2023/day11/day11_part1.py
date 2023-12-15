import os


def expand_galaxies(graph):
    rows_wo_galaxies = [i for i, row in enumerate(graph) if "#" not in row]
    cols_wo_galaxies = [i for i, col in enumerate(zip(*graph)) if "#" not in col]

    for i in reversed(rows_wo_galaxies):
        graph.insert(i, graph[i])

    # Copy of graph to perform updates
    graph_copy = [list(row) for row in graph]
    # Recieved unexpected behavior when using original graph to update rows?
    for row in graph_copy:
        for idx in sorted(cols_wo_galaxies, reverse=True):
            row.insert(idx, ".")

    print(len(graph), len(graph[0]))
    print(len(graph_copy), len(graph_copy[0]))

    return graph_copy


def main(file):
    with open(file, "r") as f:
        contents = f.read().split()

        graph = []
        for line in contents:
            line = [x for x in line]
            print(line)
            graph.append(line)

        matrix = expand_galaxies(graph)

        coordinates = []
        for i, row in enumerate(matrix):
            for i2, col in enumerate(matrix[i]):
                if matrix[i][i2] == "#":
                    print(i, i2, matrix[i][i2])
                    coordinates.append((i, i2))

        print(coordinates)
        if isTest:
            assert len(coordinates) == 9

        total = 0
        pair_counts = 0
        for i, coord in enumerate(coordinates):
            for i in range(i + 1, len(coordinates)):
                # print(coord, coordinates[i])
                row_trav = abs(coordinates[i][0] - coord[0])

                col_trav = abs(coordinates[i][1] - coord[1])

                distance = abs(row_trav + col_trav)
                total += distance
                pair_counts += 1
        print(total)
    return total


if __name__ == "__main__":
    isTest = False
    expected = 374

    if isTest:
        data_file = "data_day11_test.txt"
    else:
        data_file = "data_day11.txt"

    file = os.path.join(os.path.dirname(__file__), data_file)

    val = main(file)

    if isTest:
        if val == expected:
            print(f"Passed: True")
        else:
            print("Passed: False")
            print(f"Results: {val}")
    else:
        print(f"Results: {val}")
