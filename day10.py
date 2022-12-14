def count_strength_at_interesting_cycles(commands: [str], interesting_cycles: [int]) -> int:
    x = 1
    command_idx = 0
    next_cycle_to_apply_command_to = 0
    command_queue = []
    results = []

    for cycle in range(max(interesting_cycles) + 1):
        if cycle in interesting_cycles:
            results.append(x * cycle)
        if command_queue:
            if command_queue[0][0] == cycle:
                x += command_queue.pop()[1]
        if cycle == max(interesting_cycles):
            break
        if cycle == next_cycle_to_apply_command_to:
            command = commands[command_idx].strip()
            if command.startswith("noop"):
                next_cycle_to_apply_command_to += 1
                command_idx += 1
                continue
            else:
                increment = int(command.split(" ")[1])
                command_queue.append((cycle + 2, increment))
                next_cycle_to_apply_command_to += 2
                command_idx += 1

    return sum(results)


def count_load_from_file(input_file: str, interesting_cycles: [int]) -> int:
    with open(input_file) as f:
        lines = f.readlines()

    commands = list(map(lambda line: line.strip(), lines))

    return count_strength_at_interesting_cycles(commands, interesting_cycles)


print(f"Solution to Part One: {count_load_from_file('day10.txt', [20, 60, 100, 140, 180, 220])}\n")
