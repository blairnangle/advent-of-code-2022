import day5


def test_example_case_part_one():
    assert day5.move_crates_9000("day5_test.txt") == "CMZ"


def test_example_case_part_two():
    assert day5.move_crates_9001("day5_test.txt") == "MCD"
