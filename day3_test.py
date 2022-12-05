import day3


def test_example_case_part_one():
    assert day3.get_priorities("day3_test.txt") == 157


def test_example_case_part_two():
    assert day3.get_priorities_for_groups_of_three("day3_test.txt") == 70
