import day4


def test_example_case_part_one():
    assert day4.get_number_of_completely_contained_ranges("day4_test.txt") == 2


def test_example_case_part_two():
    assert day4.get_number_of_overlapping_ranges("day4_test.txt") == 4
