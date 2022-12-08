def is_tree_visible_in_line_of_trees(line: [int], tree_idx: int) -> bool:
    if tree_idx == 0 or tree_idx == len(line) - 1:
        return True
    else:
        tree = line[tree_idx]
        highest_to_left = 0
        highest_to_right = 0
        for idx, t in enumerate(line[:tree_idx]):
            if t > highest_to_left:
                highest_to_left = t
        for idx, t in enumerate(line[tree_idx + 1 :]):
            if t > highest_to_right:
                highest_to_right = t

        return tree > highest_to_left or tree > highest_to_right


def is_individual_tree_visible(grid: [[int]], row_idx: int, col_idx: int) -> bool:
    col = [row[col_idx] for row in grid]

    return is_tree_visible_in_line_of_trees(
        grid[row_idx], col_idx
    ) or is_tree_visible_in_line_of_trees(col, row_idx)


def count_visible_trees(grid: [[int]]) -> int:
    visible = 0
    for row_idx, row in enumerate(grid):
        for col_idx, tree in enumerate(row):
            if is_individual_tree_visible(grid, row_idx, col_idx):
                visible += 1

    return visible


def count_visible(input_file: str) -> int:
    with open(input_file) as f:
        lines = f.readlines()

    grid = []
    for line in lines:
        grid.append(list(map(lambda s: int(s), list(line.strip()))))

    return count_visible_trees(grid)


def score_for_neighbours(line: [int], tree_height: int) -> int:
    score = 0
    for neighbour in line:
        if tree_height > neighbour:
            score += 1
        else:
            score += 1
            return score

    return score


def calculate_scenic_score_for_tree(
    grid: [[int]], row_idx: int, col_idx: int, tree_height: int
) -> int:
    row = grid[row_idx]
    col = [row[col_idx] for row in grid]

    if (
        row_idx == 0
        or row_idx == len(col) - 1
        or col_idx == 0
        or col_idx == len(row) - 1
    ):
        return 0

    trees_left = row[::-1][len(row) - col_idx :]
    trees_right = row[col_idx + 1 :]
    trees_above = col[::-1][len(col) - row_idx :]
    trees_below = col[row_idx + 1 :]

    left_visibility = score_for_neighbours(trees_left, tree_height)
    right_visibility = score_for_neighbours(trees_right, tree_height)
    up_visibility = score_for_neighbours(trees_above, tree_height)
    down_visibility = score_for_neighbours(trees_below, tree_height)

    return left_visibility * right_visibility * up_visibility * down_visibility


def calculate_highest_scenic_score(grid: [[int]]) -> int:
    highest_scenic_score = 0
    for row_idx, row in enumerate(grid):
        for col_idx, tree in enumerate(row):
            tree_scenic_score = calculate_scenic_score_for_tree(
                grid, row_idx, col_idx, tree
            )
            if tree_scenic_score > highest_scenic_score:
                highest_scenic_score = tree_scenic_score

    return highest_scenic_score


def calculate_scenic(input_file: str) -> int:
    with open(input_file) as f:
        lines = f.readlines()

    grid = []
    for line in lines:
        grid.append(list(map(lambda s: int(s), list(line.strip()))))

    return calculate_highest_scenic_score(grid)


print(f"Solution to Part One: {count_visible('day8.txt')}\n")
print(f"Solution to Part Two: {calculate_scenic('day8.txt')}")
