import day6


def test_example_case_part_one():
    assert day6.find_first_marker_position("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 4) == 7
    assert day6.find_first_marker_position("bvwbjplbgvbhsrlpgdmjqwftvncz", 4) == 5
    assert day6.find_first_marker_position("nppdvjthqldpwncqszvftbrmjlhg", 4) == 6
    assert day6.find_first_marker_position("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 4) == 10
    assert day6.find_first_marker_position("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 4) == 11


def test_small_permutations_part_one():
    assert day6.find_first_marker_position("abcda", 4) == 4
    assert day6.find_first_marker_position("aabcd", 4) == 5
    assert day6.find_first_marker_position("aaabcd", 4) == 6
    assert day6.find_first_marker_position("aaaabcd", 4) == 7
    assert day6.find_first_marker_position("baabcd", 4) == 6


def test_example_case_part_two():
    assert day6.find_first_marker_position("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 14) == 19
    assert day6.find_first_marker_position("bvwbjplbgvbhsrlpgdmjqwftvncz", 14) == 23
    assert day6.find_first_marker_position("nppdvjthqldpwncqszvftbrmjlhg", 14) == 23
    assert day6.find_first_marker_position("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 14) == 29
    assert day6.find_first_marker_position("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 14) == 26
