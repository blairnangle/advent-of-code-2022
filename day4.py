def is_fully_contained(r1, r2):
    return r1[0] <= r2[0] and r1[1] >= r2[1]


def is_overlapping(r1, r2):
    return r1[0] <= r2[0] <= r1[1] or r1[0] <= r2[1] <= r1[1]


def get_number_of_completely_contained_ranges(input_file):
    with open(input_file) as f:
        lines = f.readlines()

    total = 0

    for line in lines:
        r1_raw, r2_raw = line.split(",")
        r1 = tuple(map(lambda bound: int(bound), r1_raw.split("-")))
        r2 = tuple(map(lambda bound: int(bound), r2_raw.split("-")))
        if is_fully_contained(r1, r2) or is_fully_contained(r2, r1):
            total += 1

    return total


def get_number_of_overlapping_ranges(input_file):
    with open(input_file) as f:
        lines = f.readlines()

    total = 0

    for line in lines:
        r1_raw, r2_raw = line.split(",")
        r1 = tuple(map(lambda bound: int(bound), r1_raw.split("-")))
        r2 = tuple(map(lambda bound: int(bound), r2_raw.split("-")))
        if is_overlapping(r1, r2) or is_overlapping(r2, r1):
            total += 1

    return total


print(f"Solution to Part One: {get_number_of_completely_contained_ranges('day4.txt')}\n")
print(f"Solution to Part Two: {get_number_of_overlapping_ranges('day4.txt')}")
