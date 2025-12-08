import  math

def run():
    with open("sample.txt", "r") as file:
        lines = file.readlines()

        line = [line.strip().split() for line in lines]
        print(len(lines))
        print(line)
        # transposed_rows = [[] for l in range(len(lines))]
        # print(transposed_rows)

        # for line in lines:
            # new_line = line.strip().split(" ")
            # new_line = [line.strip().split() for l in line]
            # print(line)

            # for l in new_line:

        transposed = [list(row) for row in zip(*line)]
        print(transposed)

        result = 0
        for row in transposed:
            operator = row[-1]
            int_row = [int(val) for val in row[:-1]]
            # print(operator)

            if operator == "*":
                temp_result = math.prod(int_row)
                result += temp_result

            if operator == "+":
                temp_result = sum(int_row)
                result += temp_result

        return result



if __name__ == "__main__":
    result = run()
    print(result)