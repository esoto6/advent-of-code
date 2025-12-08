
def run():
    with open("input.txt", "r") as file:
        lines = file.readlines()
        
        fresh_ranges = []
        products = []
        for line in lines:
            line = line.strip()
            if "-" in line:
                start, end = line.split("-")
                fresh_ranges.append((int(start), int(end)))
            elif line != "":
                products.append(int(line))

        print(fresh_ranges)
        print(products)


    # updates_fresh_ranges = []
    # for range in fresh_ranges.sort():
    #     print(range)
    
    fresh_ranges.sort(key=lambda x: int(x[0])) 

    good_product = 0
    for product in products:
        for ranges in fresh_ranges:
            range_min, range_max = min(ranges), max(ranges)
            print(type(product))
            if product > range_min and product < range_max:

                # print(f"True {product=}, {range_min=}, {range_max=}")
                good_product += 1
                break
    return good_product
if __name__ == "__main__":
    result = run()
    print(f"Result: {result}")