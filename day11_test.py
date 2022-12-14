import copy

import day11

monkeys_initial = {
    0: {
        "starting_items": [
            79,
            98,
        ],
        "operation": "new = old * 19",
        "test": "divisible by 23",
        "true": "throw to monkey 2",
        "false": "throw to monkey 3",
        "inspections": 0,
    },
    1: {
        "starting_items": [
            54,
            65,
            75,
            74,
        ],
        "operation": "new = old + 6",
        "test": "divisible by 19",
        "true": "throw to monkey 2",
        "false": "throw to monkey 0",
        "inspections": 0,
    },
    2: {
        "starting_items": [
            79,
            60,
            97,
        ],
        "operation": "new = old * old",
        "test": "divisible by 13",
        "true": "throw to monkey 1",
        "false": "throw to monkey 3",
        "inspections": 0,
    },
    3: {
        "starting_items": [
            74,
        ],
        "operation": "new = old + 3",
        "test": "divisible by 17",
        "true": "throw to monkey 0",
        "false": "throw to monkey 1",
        "inspections": 0,
    },
}

monkeys_expected = {
    0: {
        "starting_items": [
            20,
            23,
            27,
            26,
        ],
        "operation": "new = old * 19",
        "test": "divisible by 23",
        "true": "throw to monkey 2",
        "false": "throw to monkey 3",
        "inspections": 2,
    },
    1: {
        "starting_items": [
            2080,
            25,
            167,
            207,
            401,
            1046,
        ],
        "operation": "new = old + 6",
        "test": "divisible by 19",
        "true": "throw to monkey 2",
        "false": "throw to monkey 0",
        "inspections": 4,
    },
    2: {
        "starting_items": [],
        "operation": "new = old * old",
        "test": "divisible by 13",
        "true": "throw to monkey 1",
        "false": "throw to monkey 3",
        "inspections": 3,
    },
    3: {
        "starting_items": [],
        "operation": "new = old + 3",
        "test": "divisible by 17",
        "true": "throw to monkey 0",
        "false": "throw to monkey 1",
        "inspections": 5,
    },
}


def test_example_case_part_one_1_round():
    assert day11.play_round(copy.deepcopy(monkeys_initial)) == monkeys_expected


def test_example_case_part_one_n_rounds():
    assert day11.play_n_rounds(copy.deepcopy(monkeys_initial), 1) == monkeys_expected


def test_parse_from_file_to_monkeys():
    assert day11.parse_file_into_monkeys("day11_test.txt") == monkeys_initial


def test_calculate_monkey_business():
    assert (
        day11.play_n_rounds_and_calculate_monkey_business("day11_test.txt", 20) == 10605
    )
