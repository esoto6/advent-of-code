import os


# Groups of valid springs are always seperated by at least one operations spring
def process(spring: str, record: tuple):
    # If the spring starts with either "." or "?" calls process with the remainder string
    # If the spring starts with either "#" or "?" ->
    # Evaluate 3 conditions:
    #   1. If the record[0] is less than or equal to the length of spring
    #   2. If there are no "." characters in teh substrin gof spring up to the lenght of record[0]
    #   3. If char at index in record[0] in spring is not '#'
    #       or
    #      If record[0] is at the end of 'spring'
    #   4. If all above conditions are met Callprocess with updated indices in spring and record
    #       and update result
    # Return Result

    print(spring, record)
    # Sprint = ['???.###']
    # Record = (1, 1, 3)

    if spring == "":
        # If string is empty and record is empty tuple return 1
        if record == ():
            return 1
        else:
            return 0

    if record == ():
        # If no more record's if '#' in spring return
        if "#" in spring:
            return 0
        else:
            return 1

    result = 0

    # If multiple '?' in records tehy must all become dots
    if spring[0] in ".?":
        # Call Process with the remainder of string and record
        result += process(spring[1:], record)

    if spring[0] in "#?":
        # 3 conditions
        if (
            record[0] <= len(spring)
            and "." not in spring[: record[0]]
            and (record[0] == len(spring) or spring[record[0]] != "#")
        ):
            # If true
            result += process(spring[record[0] + 1 :], record[1:])

    return result


def main(file):
    with open(file, "r") as f:
        content = f.read().split("\n")

        total = 0

        for line in content:
            springs, records = line.split()
            # spring = [x for x in springs]

            # Make record a tuple since it is immutable.
            record = tuple(map(int, records.split(",")))
            total += process(springs, record)
    return total


if __name__ == "__main__":
    isTest = False
    expected = 21

    if isTest:
        data_file = "data_day12_test.txt"
    else:
        data_file = "data_day12.txt"

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
