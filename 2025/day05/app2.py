
def run():
    with open("input.txt", "r") as file:
        lines = file.readlines()
        
        fresh_ranges = []
        # products = []
        for line in lines:
            line = line.strip()
            if "-" in line:
                start, end = line.split("-")
                fresh_ranges.append((int(start), int(end)))
            # elif line != "":
            #     products.append(int(line))

        print(fresh_ranges)
        # print(products)


    
    fresh_ranges.sort(key=lambda x: int(x[0])) 
    updated_ranges = []

    for start, end in fresh_ranges:
        
        print(f"Start: {start},  End: {end}")

        if not updated_ranges or start > updated_ranges[-1][1]:
            updated_ranges.append([start, end])
        else:
            updated_ranges[-1][1] = max(updated_ranges[-1][1], end)
    
    print(len(updated_ranges))

     

    print(updated_ranges)
    total = 0
    for start, end in updated_ranges:
        val = end - start + 1
        print(start, end, val)
        total += val
    return total

    # good_product = 0
    # for product in products:
    #     for ranges in fresh_ranges:
    #         range_min, range_max = min(ranges), max(ranges)
    #         print(type(product))
    #         if product > range_min and product < range_max:

    #             # print(f"True {product=}, {range_min=}, {range_max=}")
    #             good_product += 1
    #             break
    # return good_product
if __name__ == "__main__":
    result = run()
    print(f"Result: {result}")