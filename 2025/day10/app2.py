from z3 import Int, Sum, Optimize, sat

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

            joltages = list(int(x) for x in line[-1].strip("{}").split(","))
            print(f"{joltages=}")

            combinations.append((button, sequences, joltages))

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

def get_min_presses(sequences, targets):
    num_buttons = len(sequences)
    num_counters = len(targets)

    button_presses = [Int(f"x{i}") for i in range(num_buttons)]
    print(f"{button_presses=}")

    solver = Optimize()

    for xi in button_presses: 
        solver.add(xi >= 0)
    
    for idx in range(num_counters):
        counter_sum = Sum([
            button_presses[j] 
            for j in range(num_buttons) 
            if idx in sequences[j]
        ])
        solver.add(counter_sum == targets[idx])

    solver.minimize(Sum(button_presses))

    if solver.check() == sat:
        model = solver.model()
        presses = [model[xi].as_long() for xi in button_presses] 
        total_presses = sum(presses)
        print(f"Model: {model}, Total Presses: {total_presses}")
        print(f"{total_presses=}")
        return total_presses, presses

    return None, None

if __name__ == "__main__": 
    file_name = "input.txt"
    combinations = get_file(file_name)

    result = 0
    for button, sequences, targets in combinations:
        print(f"---------- Start -----------")
        print(f"{sequences=}, {targets=}")

        val, presses = get_min_presses(sequences, targets)
        if val is not None:
            result += val
   
    print(f"Result= {result}")

    # Not 390