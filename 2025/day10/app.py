
def get_file(file_name):
    
    with open(file_name, "r") as file:
        lines = file.readlines()

        combinations = []
        for line in lines:
            line = line.strip().split()
            # button, sequence, joltage = line[0].strip("[").strip("]"), line[1:-1], line[1-1].strip("{").strip("}")

            button = line[0].strip("[]")

            sequences = []
            for seq in line[1:-1]:
                seq = tuple(int(x) for x in seq.strip("()").split(","))
                sequences.append(seq)

            combinations.append((button, sequences))

    return combinations

def diagram_to_mask(el):
    mask = 0
    for i, ch in enumerate(el):
        if ch == "#":
            mask |= (1 << i)
    print(f"Diagram: {el}, Mask: {mask:b}")
    return mask

def sequence_to_mask(sequence):
    mask = 0
    for i in sequence:
        mask |= (1 << i)
    print(f"Sequence: {sequence}, Mask: {mask:b}")
    return mask

def get_least_possible_buttons(button, sequences):
    # button = [False if num == "." else True for num in button]
    target = diagram_to_mask(button)
    sequence_masks = [sequence_to_mask(seq) for seq in sequences]

    n = len(sequence_masks)
    best = float("inf")

    for subset in range( 1 << n): 
        current = 0
        presses = 0
        for i in range(n):
            if subset & (1 << i):
                current ^= sequence_masks[i]
                presses += 1

                if presses >= best:
                    break
        if current == target:
            best = min(best, presses)
    
    if best == float("inf"):
        return None

    print(f"Best for {button=} is {best}") 
    return best

if __name__ == "__main__": 
    file_name = "input.txt"
    combinations = get_file(file_name)

    result = 0
    for button, sequences in combinations:
        print(f"---------- Start -----------")
        print(f"{button=}, {sequences=}")
        val = get_least_possible_buttons(button, sequences)
        if val is not None:
            result += val
   
    print(f"Result= {result}")