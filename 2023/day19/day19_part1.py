import os


def create_parts(parts):
    parts = parts.split("\n")

    partsList = []

    for row in parts:
        row = row.replace("{", "").replace("}", "")

        row = row.split(",")
        print(row)
        row_dict = {"x": 0, "m": 0, "a": 0, "s": 0}
        for letter in row:
            letter, value = letter.split("=")
            row_dict[letter] = value
        partsList.append(row_dict)

    print(partsList)

    return partsList


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
                ruleValue = rule[2:]
                rule_list.append((ruleKey, ruleOp, ruleValue, answer))
            else:
                elseValue = rule
        workflows[work_key] = rule_list, elseValue

    return workflows


def find_valid_parts(parts, key, workflows):
    if key == "A":
        return True

    if key == "R":
        return False

    rules, returnValue = workflows.get(key)

    passed_list = []
    for rule in rules:
        ruleKey = rule[0]
        ruleOP = rule[1]
        ruleValue = int(rule[2])
        ruleifTrue = rule[3]

        if ruleOP == ">":
            if int(parts[ruleKey]) > ruleValue:
                passed_list.append(ruleifTrue)
            # else:
            # passed_list.append("")
        if ruleOP == "<":
            if int(parts[ruleKey]) < ruleValue:
                passed_list.append(ruleifTrue)
            # else:
            # passed_list.append("")

    if not passed_list:
        passed_list = [returnValue]

    # isAnswer = True
    return find_valid_parts(parts, passed_list[0], workflows)
    # for idx, val in enumerate(passed_list):
    # if val != "":
    # if val == "A":
    #     isAnswer = True
    #     break
    # if val == "R":
    #     isanswer = True
    #     # break
    # else:
    #     pritn("hello")
    # isAnswer = find_valid_parts(parts=parts, key=val, workflows=workflows)

    # if isAnswer:
    # return True
    # print(idx, val)

    # print(rule)
    # print(rules)


def main(file):
    with open(file, "r") as f:
        workflow, parts = f.read().split("\n\n")

    workflow = refine_work(workflow)
    print(f"Workflow: {workflow}")
    parts = create_parts(parts)
    print(f"Parts: {parts}")

    total = 0
    for row in parts:
        val = find_valid_parts(parts=row, key="in", workflows=workflow)

        if val:
            rowTotal = sum([int(row[key]) for key in row.keys()])
            total += rowTotal

    return total


if __name__ == "__main__":
    isTest = False
    expected = 19114

    if isTest:
        data_file = "data_day19_test.txt"
    else:
        data_file = "data_day19.txt"

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
