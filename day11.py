def execute_operation(operation_str: str, old: int) -> int:
    split = operation_str.split(" ")
    operator = split[-2]
    operand = split[-1]
    if operand == "old":
        operand = old
    else:
        operand = int(operand)
    if operator == "+":
        return old + operand
    elif operator == "*":
        return old * operand


def execute_test(test_str: str, worry_level: int) -> bool:
    split = test_str.split(" ")
    if split[-3] == "divisible":
        return worry_level % int(split[-1]) == 0


def execute_throw(monkeys: dict, throw_str: str, item: int) -> None:
    monkeys[int(throw_str.split()[-1])]["starting_items"].append(item)


def play_round(monkeys: dict):
    for monkey_key in monkeys.keys():
        starting_items = monkeys[monkey_key]["starting_items"]
        for item in starting_items:
            worry_level = execute_operation(monkeys[monkey_key]["operation"], item) // 3
            monkeys[monkey_key]["inspections"] += 1
            if execute_test(monkeys[monkey_key]["test"], worry_level):
                execute_throw(monkeys, monkeys[monkey_key]["true"], worry_level)
            else:
                execute_throw(monkeys, monkeys[monkey_key]["false"], worry_level)

        monkeys[monkey_key]["starting_items"] = []

    return monkeys


def play_n_rounds(monkeys: dict, n: int) -> dict:
    for r in range(n):
        monkeys = play_round(monkeys)

    return monkeys


def parse_file_into_monkeys(input_file: str) -> dict:
    with open(input_file) as f:
        lines = f.readlines()

    monkeys = {}

    for idx, line in enumerate(lines):
        stripped = line.strip()
        if stripped.startswith("Monkey"):
            monkey_n = int(stripped[-2])
            monkeys[monkey_n] = {}
            monkeys[monkey_n]["starting_items"] = list(
                map(lambda s: int(s), lines[idx + 1].split(":")[1].split(","))
            )
            monkeys[monkey_n]["operation"] = lines[idx + 2].split(":")[1].strip()
            monkeys[monkey_n]["test"] = lines[idx + 3].split(":")[1].strip()
            monkeys[monkey_n]["true"] = lines[idx + 4].split(":")[1].strip()
            monkeys[monkey_n]["false"] = lines[idx + 5].split(":")[1].strip()
            monkeys[monkey_n]["inspections"] = 0

    return monkeys


def play_n_rounds_and_calculate_monkey_business(input_file: str, n: int) -> int:
    monkeys = parse_file_into_monkeys(input_file)

    for r in range(n):
        monkeys = play_round(monkeys)

    inspections_sorted = sorted(
        list(map(lambda key: monkeys[key]["inspections"], monkeys.keys()))
    )

    return inspections_sorted[-1] * inspections_sorted[-2]


print(
    f"Solution to Part One: {play_n_rounds_and_calculate_monkey_business(input_file='day11.txt', n=20)}\n"
)
