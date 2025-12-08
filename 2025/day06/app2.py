import  math
from typing import List

def get_idxs(lines) -> List[int]:
    idxs_to_split = [] 
    for i in range(len(lines[0])):
        print(f"Index: {i}")

        check = list(map(lambda col: col[i], lines))
        if set(check) == {'0'}:
        # print(f"Index: {i}")
            idxs_to_split.append(int(i))
            # print(f"Index to split: {i}")

    print(idxs_to_split)
    return idxs_to_split

def split_lines(lines, idxs) -> List[str]:
    new_lines = []

    for row in lines:
        # print(row, len(row))
        temp = list(row)
        # print(f"Temp: {temp}")

        for i in range(len(temp)):
            if i in idxs:
                temp[i] = ","

        temp = "".join(temp)
        temp = temp.split(",")
        # print(f"Nedw Temp: {temp}")
        new_lines.append(temp)
    return new_lines

def convert_to_nums(rows):
    grid = [list(r) for r in rows]
    cols = list(zip(*grid))[::-1]
    print(f"Cols: {cols}")

    new_list = []
    for val in cols:
        print(f"Val: {val}")
        temp = []
        for v in val:
            if v == '0':
                continue
            else:
                temp.append(v)
        # print(f"Temp: {temp}")
        val = "".join(temp)
        new_list.append(int(val))
    # print(new_list)
    return new_list

def run():
    with open("input.txt", "r") as file:
        lines = file.readlines()

        lines_replaced = [line.replace(" ", "0").strip() for line in lines[:-1]]
        operator = lines[-1]
        operator = operator.strip().split() 

        # print(lines_replaced)
        # print(operator)

        idxs = get_idxs(lines_replaced)
        # print(f"Idxs: {idxs}")
        new_lines = split_lines(lines_replaced, idxs)
        # print(f"New: {new_lines}")

        transposed = [list(row) for row in zip(*new_lines)]
        
        print(transposed)
        # print([list(row) for row in transposed])

        result = 0
        for row, op in zip(reversed(transposed), reversed(operator)):
            
            int_row = convert_to_nums(row)
            # int_row = [int(val) for val in row[:-1]]
            print(f"Row to eval: {int_row}")
            print(op)

            if op == "*":
                temp_result = math.prod(int_row)
                result += temp_result

            if op == "+":
                temp_result = sum(int_row)
                result += temp_result

        return result
    
if __name__ == "__main__":
    result = run()
    print(result)