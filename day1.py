def get_top_elf_calories(input_file):
    with open(input_file) as f:
        lines = f.readlines()

    highest = 0
    current = 0
    n_lines = len(lines)

    for idx, line in enumerate(lines):
        if line == "\n" or idx == n_lines - 1:
            if current > highest:
                highest = current
                current = 0
            else:
                current = 0
        else:
            current += int(line)

    return highest


def get_top_three_elves_calories(input_file):
    with open(input_file) as f:
        lines = f.readlines()

    top_three = []

    current = 0
    n_lines = len(lines)

    for idx, line in enumerate(lines):
        if line == "\n" or idx == n_lines - 1:
            if current > min(top_three, default=0):
                top_three.sort()
                if len(top_three) == 3:
                    top_three[0] = current
                else:
                    top_three.append(current)
                current = 0
            else:
                current = 0
        else:
            current += int(line)

    return sum(top_three)


print(f"Solution to Part One: {get_top_elf_calories('day1.txt')}\n")
print(f"Solution to Part Two: {get_top_three_elves_calories('day1.txt')}")
