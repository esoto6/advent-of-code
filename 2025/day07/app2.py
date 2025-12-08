
from functools import cache

def load_file(file_name: str):
    with open(file_name, "r") as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]

    for line in lines:
        print(line)
    return lines

def run():
    data = load_file("input.txt")


    pos = (0, data[0].index("S"))
    print(*pos)

    @cache
    def solve(r, c):
        if r >= len(data): return 1

        if data[r][c] == "." or data[r][c] == "S":
            return solve(r +1 , c)    
        elif data[r][c] == "^":
            return solve(r, c-1) + solve(r, c +1 )
    
    result = solve(*pos)
    return result

if __name__ == "__main__":
    result = run()
    print(f"Result: {result}")