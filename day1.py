def count_calories(input_file):
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


print(count_calories("day1.txt"))
