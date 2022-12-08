import day8

grid = [
    [3, 0, 3, 7, 3],
    [2, 5, 5, 1, 2],
    [6, 5, 3, 3, 2],
    [3, 3, 5, 4, 9],
    [3, 5, 3, 9, 0],
]


def test_example_case_part_one_with_nested_lists():
    assert day8.count_visible_trees(grid) == 21


def test_example_case_part_one_with_input_file():
    assert day8.count_visible("day8_test.txt") == 21


def test_example_case_part_two_with_nested_lists():
    assert day8.calculate_highest_scenic_score(grid) == 8


def test_example_case_part_two_with_input_file():
    assert day8.calculate_scenic("day8_test.txt") == 8
