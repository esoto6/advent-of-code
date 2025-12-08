
def invalid_id(start_range: int, end_range: int)-> int:
    invalid_ids=[]
    pos = start_range

    while pos != end_range + 1:
        curr_id = str(pos)
        length = len(curr_id)
        mid = length // 2
        print(f"Curr: {curr_id}, Length: {length}, Mid: {mid}")
        
        if length % 2 == 0:
            if length == 2:
                if curr_id[0] == curr_id[1]:
                    invalid_ids.append(pos)

            elif curr_id[:mid] == curr_id[mid:]:
                invalid_ids.append(pos)

        pos += 1
    print(f"Invalid IDs: {invalid_ids}")
    return sum(invalid_ids)

def run():
    with open("antonio.txt", "r") as file:
        cum_sum = 0
        content = file.read().replace("\n", "")

        product_ids = content.split(",")
        print(product_ids)

        for product in product_ids:
            start_range, end_range = product.split("-")
            print(f"Start Range: {start_range}, End Range: {end_range}")
            val = invalid_id(int(start_range), int(end_range))
            cum_sum += val

        return cum_sum
if  __name__ == "__main__":
    result = run()
    print(f"Result: {result}")
