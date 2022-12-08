def find_first_marker_position(buffer, n_distinct_chars):
    window = []
    for idx, letter in enumerate(list(buffer)):
        if letter in window:
            window.append(letter)
            window = window[window.index(letter) + 1 :]
            continue
        else:
            window.append(letter)
        if len(window) == n_distinct_chars:
            return idx + 1


def solution_wrapper(input_file, n_distinct_chars):
    with open(input_file) as f:
        buffer = f.readlines()[0]

    return find_first_marker_position(buffer, n_distinct_chars)


print(f"Solution to Part One: {solution_wrapper('day6.txt', 4)}\n")
print(f"Solution to Part Two: {solution_wrapper('day6.txt', 14)}")
