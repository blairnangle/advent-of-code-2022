def is_tail_within_one_move_of_head(x_head, y_head, x_tail, y_tail) -> bool:
    return abs(x_head - x_tail) <= 1 and abs(y_head - y_tail) <= 1


# return new head and tail coordinates, plus all the coordinates that the tail visited
def move(
    vector_direction, vector_magnitude, x_head, y_head, x_tail, y_tail
) -> ((int, int), (int, int), [(int, int)]):
    coordinates_tail = []

    for movement in range(0, vector_magnitude):
        if vector_direction == "R":
            x_head += 1
            if not is_tail_within_one_move_of_head(x_head, y_head, x_tail, y_tail):
                x_tail += 1
                y_tail = y_head
            coordinates_tail.append((x_tail, y_tail))
        elif vector_direction == "U":
            y_head += 1
            if not is_tail_within_one_move_of_head(x_head, y_head, x_tail, y_tail):
                y_tail += 1
                x_tail = x_head
            coordinates_tail.append((x_tail, y_tail))
        elif vector_direction == "L":
            x_head -= 1
            if not is_tail_within_one_move_of_head(x_head, y_head, x_tail, y_tail):
                x_tail -= 1
                y_tail = y_head
            coordinates_tail.append((x_tail, y_tail))
        elif vector_direction == "D":
            y_head -= 1
            if not is_tail_within_one_move_of_head(x_head, y_head, x_tail, y_tail):
                y_tail -= 1
                x_tail = x_head
            coordinates_tail.append((x_tail, y_tail))

    return (x_head, y_head), (x_tail, y_tail), coordinates_tail


def count_unique_coordinates(coordinates: [(int, int)]) -> int:
    return len(set(coordinates))


def parse_and_move(input_file: str):
    with open(input_file) as f:
        lines = f.readlines()

    coordinates_all = []
    x_head, y_head, x_tail, y_tail = 0, 0, 0, 0

    for line in lines:
        line_vals = line.strip().split(" ")
        vector_direction, vector_magnitude = line_vals[0], int(line_vals[1])
        (x_head, y_head), (x_tail, y_tail), coordinates_per_move = move(
            vector_direction, vector_magnitude, x_head, y_head, x_tail, y_tail
        )
        coordinates_all += coordinates_per_move

    return count_unique_coordinates(coordinates_all)


print(f"Solution to Part One: {parse_and_move('day9.txt')}\n")
