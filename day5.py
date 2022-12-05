import re
import string


def parse(input_file):
    with open(input_file) as f:
        lines = f.readlines()

    initial_state = {}
    instructions = []

    for line in lines:
        if line.startswith("move"):
            instructions.append(line.strip())
        if re.match("^[0-9]", line):
            line_elements = line.strip().translate(str.maketrans('', '', string.punctuation)).split(" ")
            stack_number, crates = line_elements[0], line_elements[1:]
            initial_state[stack_number] = crates

    return initial_state, instructions


def move_crates_9000(input_file):
    state, instructions = parse(input_file)

    for instruction in instructions:
        split = instruction.split(" ")
        start = split[3]
        end = split[5]
        n = int(split[1])

        for crate in range(0, n):
            state[end].append(state[start].pop())

    return "".join([crates[-1] for crates in state.values()])


def move_crates_9001(input_file):
    state, instructions = parse(input_file)

    for instruction in instructions:
        split = instruction.split(" ")
        start = split[3]
        end = split[5]
        n = int(split[1])

        new_starting_stack = state[start][:len(state[start]) - n]
        crates_to_move = state[start][len(state[start]) - n:]

        state[start] = new_starting_stack
        state[end] = state[end] + crates_to_move

    return "".join([crates[-1] for crates in state.values()])


print(f"Solution to Part One: {move_crates_9000('day5.txt')}\n")
print(f"Solution to Part Two: {move_crates_9001('day5.txt')}")
