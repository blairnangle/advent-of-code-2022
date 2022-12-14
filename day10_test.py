import day10


def test_example_case_part_one_list_commands():
    commands = [
        "noop",
        "addx 3",
        "addx -5",
    ]

    interesting_cycles = [
        5
    ]

    assert day10.count_strength_at_interesting_cycles(commands=commands, interesting_cycles=interesting_cycles) == -5


def test_example_case_part_one_from_file():

    interesting_cycles = [
        20,
        60,
        100,
        140,
        180,
        220,
    ]

    assert day10.count_load_from_file(input_file="day10_test.txt", interesting_cycles=interesting_cycles) == 13140
