def count_strength_at_interesting_cycles(
    commands: [str], interesting_cycles: [int]
) -> int:
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


def draw(commands: [str], crt_width: int, crt_height: int) -> [str]:
    x = 1
    command_idx = 0
    next_cycle_to_apply_command_to = 0
    command_queue = []
    crt_row = []
    row_n = 0
    monitor = []
    sprite_position = [0, 1, 2]

    for cycle in range(crt_width * crt_height):
        pixel_currently_being_drawn = cycle - row_n * crt_width
        if command_queue:
            if command_queue[0][0] == cycle:
                diff = command_queue.pop()[1]
                x += diff
                sprite_position = [x - 1, x, x + 1]
        if pixel_currently_being_drawn in sprite_position:
            crt_row.append("#")
        else:
            crt_row.append(".")
        if cycle == next_cycle_to_apply_command_to:
            command = commands[command_idx].strip()
            if command.startswith("noop"):
                next_cycle_to_apply_command_to += 1
                command_idx += 1
            else:
                increment = int(command.split(" ")[1])
                command_queue.append((cycle + 2, increment))
                next_cycle_to_apply_command_to += 2
                command_idx += 1
        if cycle != 0 and (cycle + 1) % crt_width == 0:
            sprite_position = [0, 1, 2]
            monitor.append(crt_row)
            crt_row = []
            row_n += 1

    return """\n""".join(["".join(row) for row in monitor])


def render_from_file(input_file: str, crt_width: int, crt_height: int) -> str:
    with open(input_file) as f:
        lines = f.readlines()

    commands = list(map(lambda line: line.strip(), lines))

    return draw(commands, crt_width, crt_height)


print(
    f"Solution to Part One: {count_load_from_file(input_file='day10.txt', interesting_cycles=[20, 60, 100, 140, 180, 220])}\n"
)
print(
    f"Solution to Part Two:\n{render_from_file(input_file='day10.txt', crt_width=40, crt_height=6)}\n"
)
