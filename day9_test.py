import day9


def test_is_tail_within_one_move_of_head():
    for head_coordinates, y_coordinates, expected in [
        [(0, 0), (0, 0), True],
        [(0, 2), (0, 0), False],
    ]:
        assert (
            day9.is_tail_within_one_move_of_head(
                head_coordinates[0],
                head_coordinates[1],
                y_coordinates[0],
                y_coordinates[1],
            )
            == expected
        )


def test_example_case_part_one_r4():
    assert day9.move(
        vector_direction="R",
        vector_magnitude=4,
        x_head=0,
        y_head=0,
        x_tail=0,
        y_tail=0,
    ) == ((4, 0), (3, 0), [(0, 0), (1, 0), (2, 0), (3, 0)])


def test_example_case_part_one_u4():
    assert day9.move(
        vector_direction="U",
        vector_magnitude=4,
        x_head=4,
        y_head=0,
        x_tail=3,
        y_tail=0,
    ) == ((4, 4), (4, 3), [(3, 0), (4, 1), (4, 2), (4, 3)])


def test_example_case_part_one_l3():
    assert day9.move(
        vector_direction="L",
        vector_magnitude=3,
        x_head=4,
        y_head=4,
        x_tail=4,
        y_tail=3,
    ) == ((1, 4), (2, 4), [(4, 3), (3, 4), (2, 4)])


def test_example_case_part_one_d1():
    assert day9.move(
        vector_direction="D",
        vector_magnitude=1,
        x_head=1,
        y_head=4,
        x_tail=2,
        y_tail=4,
    ) == ((1, 3), (2, 4), [(2, 4)])


def test_count_unique_coordinates():
    assert day9.count_unique_coordinates([(1, 1), (1, 2), (2, 3), (1, 1)]) == 3
