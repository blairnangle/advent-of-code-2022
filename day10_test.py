import day10


def test_example_case_part_one_list_commands():
    commands = [
        "noop",
        "addx 3",
        "addx -5",
    ]

    assert (
        day10.count_strength_at_interesting_cycles(
            commands=commands, interesting_cycles=[5]
        )
        == 20
    )


def test_example_case_part_one_from_file():
    interesting_cycles = [
        20,
        60,
        100,
        140,
        180,
        220,
    ]

    assert (
        day10.count_load_from_file(
            input_file="day10_test.txt", interesting_cycles=interesting_cycles
        )
        == 13140
    )


def test_example_case_part_two_draw_row_from_list_of_commands():
    commands = [
        "addx 15",
        "addx -11",
        "addx 6",
        "addx -3",
        "addx 5",
        "addx -1",
        "addx -8",
        "addx 13",
        "addx 4",
        "noop",
        "addx -1",
    ]

    assert (
        day10.draw(commands=commands, crt_width=21, crt_height=1)
        == "##..##..##..##..##..#"
    )


def test_example_case_part_two_render_multiple_rows_from_file():
    assert (
        day10.render_from_file(input_file="day10_test.txt", crt_width=40, crt_height=6)
        == """##..##..##..##..##..##..##..##..##..##..
###...###...###...###...###...###...###.
####....####....####....####....####....
#####.....#####.....#####.....#####.....
######......######......######......####
#######.......#######.......#######....."""
    )
