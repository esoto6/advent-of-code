import os
from pprint import pprint


def refine_work(workflow):
    workflow = workflow.split("\n")
    print(workflow)

    workflows = {}
    for row in workflow:
        row = row.replace("{", " ").replace("}", "")
        work_key, rules = row.split(" ")

        rules = rules.split(",")

        rule_list = []
        workflows[work_key] = ()
        for rule in rules:
            if ":" in rule:
                rule, answer = rule.split(":")
                ruleKey = rule[0]
                ruleOp = rule[1]
                ruleValue = int(rule[2:])
                rule_list.append((ruleKey, ruleOp, ruleValue, answer))
            else:
                elseValue = rule
        workflows[work_key] = rule_list, elseValue

    return workflows


def find_combinations(parts_ranges, strategy="in"):
    if strategy == "A":
        product = 1
        for start, stop in parts_ranges.values():
            product *= stop - start + 1
        return product

    if strategy == "R":
        return 0

    rules, returnValue = workflows.get(strategy)

    total = 0
    for ruleKey, ruleOP, ruleValue, ruleifTrue in rules:
        start, stop = parts_ranges[ruleKey]
        if ruleOP == "<":
            true_Range = (start, min(ruleValue - 1, stop))
            false_Range = (max(ruleValue, start), stop)
        else:
            true_Range = (max(ruleValue + 1, start), stop)
            false_Range = (start, min(ruleValue, stop))

        if true_Range[0] <= true_Range[1]:
            parts_copy = dict(parts_ranges)
            parts_copy[ruleKey] = true_Range
            total += find_combinations(parts_copy, ruleifTrue)

        if false_Range[0] <= false_Range[1]:
            parts_ranges = dict(parts_ranges)
            parts_ranges[ruleKey] = false_Range
        else:
            break
    else:
        total += find_combinations(parts_ranges, returnValue)

    return total


def main(file):
    with open(file, "r") as f:
        workflow, parts = f.read().split("\n\n")

    workflows = refine_work(workflow)
    pprint(f"Workflow: {workflows}")

    return workflows


if __name__ == "__main__":
    isTest = False
    expected = 167409079868000

    if isTest:
        data_file = "data_day19_test.txt"
    else:
        data_file = "data_day19.txt"

    file = os.path.join(os.path.dirname(__file__), data_file)

    workflows = main(file)

    val = find_combinations({key: (1, 4000) for key in "xmas"})

    if isTest:
        if val == expected:
            print(f"Passed: True")
        else:
            print("Passed: False")
            print(f"Results: {val}")
    else:
        print(f"Results: {val}")
