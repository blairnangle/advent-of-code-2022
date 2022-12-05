import day1


def test_example_case_part_one():
    assert day1.get_top_elf_calories("day1_test.txt") == 24000


def test_example_case_part_two():
    assert day1.get_top_three_elves_calories("day1_test.txt") == 45000
