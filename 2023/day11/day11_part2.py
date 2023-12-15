import os


def expand_galaxies(graph):
    rows_wo_galaxies = [i for i, row in enumerate(graph) if "#" not in row]
    cols_wo_galaxies = [i for i, col in enumerate(zip(*graph)) if "#" not in col]

    print(f"rows_wo_galaxies: {rows_wo_galaxies}")
    print(f"Cols wo galaxies: {cols_wo_galaxies}")

    return rows_wo_galaxies, cols_wo_galaxies


def main(file):
    with open(file, "r") as f:
        contents = f.read().split()

        graph = []
        for line in contents:
            line = [x for x in line]
            print(line)
            graph.append(line)

        row_wo_gal, col_wo_gal = expand_galaxies(graph)

        coordinates = []
        for row in range(0, len(graph)):
            for col in range(0, len(graph[0])):
                if graph[row][col] == "#":
                    # print(i, i2, graph[i][i2])
                    coordinates.append((row, col))

        print(coordinates)
        if isTest:
            assert len(coordinates) == 9

        ans = 0
        pair_counts = 0
        # expansion = 10**6 - 1
        for i, (r1, c1) in enumerate(coordinates):
            for j in range(i, len(coordinates)):
                # print(coord, coordinates[i])
                r2, c2 = coordinates[j]
                dist = abs(r2 - r1) + abs(c2 - c1)

                for empty_row in row_wo_gal:
                    if min(r1, r2) <= empty_row <= max(r1, r2):
                        dist += 1000000 - 1

                for empty_col in col_wo_gal:
                    if min(c1, c2) <= empty_col <= max(c1, c2):
                        dist += 1000000 - 1

                ans += dist
                pair_counts += 1
    print(ans)
    return ans


if __name__ == "__main__":
    isTest = True
    expected = 82000210

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
