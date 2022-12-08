def build_priorities_dict():
    lower = {
        chr(ascii_code): idx + 1 for idx, ascii_code in enumerate(range(97, 97 + 26))
    }
    upper = {
        chr(ascii_code): idx + 27 for idx, ascii_code in enumerate(range(65, 65 + 26))
    }

    return lower | upper


def get_priorities(input_file):
    with open(input_file) as f:
        lines = f.readlines()

    total = 0
    priorities_dict = build_priorities_dict()

    for line in lines:
        len_line = len(line)
        compartment_1 = line[0 : len_line // 2]
        compartment_2 = line[len_line // 2 : len_line - 1]
        intersection = list(set(compartment_1).intersection(set(compartment_2)))
        common_item = intersection[0]
        total += priorities_dict[common_item]

    return total


def get_priorities_for_groups_of_three(input_file):
    with open(input_file) as f:
        lines = f.readlines()

    total = 0
    priorities_dict = build_priorities_dict()

    for idx, line in enumerate(lines):
        if idx % 3 == 0:
            elf_1 = line.strip()
            elf_2 = lines[idx + 1].strip()
            elf_3 = lines[idx + 2].strip()
            intersection = list(
                set(elf_1).intersection(set(elf_2)).intersection(set(elf_3))
            )
            common_item = intersection[0]
            total += priorities_dict[common_item]
        else:
            continue

    return total


print(f"Solution to Part One: {get_priorities('day3.txt')}\n")
print(f"Solution to Part Two: {get_priorities_for_groups_of_three('day3.txt')}")
