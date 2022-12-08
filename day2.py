# win = 6
# draw = 3
# lose = 0
# A = opponent rock
# B = opponent paper
# C = opponent scissors
# X = me rock (+1)
# Y = me paper(+2)
# Z = me scissors (+3)


def score_strategy_one(input_file):
    permutations = {
        "AX": 4,
        "AY": 8,
        "AZ": 3,
        "BX": 1,
        "BY": 5,
        "BZ": 9,
        "CX": 7,
        "CY": 2,
        "CZ": 6,
    }

    with open(input_file) as f:
        lines = f.readlines()

    total = 0

    for line in lines:
        permutation = "".join(line.strip().split(" "))
        total += permutations[permutation]

    return total


# win = 6
# draw = 3
# lose = 0
# A = opponent rock
# B = opponent paper
# C = opponent scissors
# X = I need to lose
# Y = I need to draw
# Z = I need to win
# choosing rock = +1
# choosing paper = +2
# choosing scissors = +3


def score_strategy_two(input_file):
    outcome_based_score = {
        "X": 0,
        "Y": 3,
        "Z": 6,
    }

    choice_based_score = {
        "AX": 3,
        "AY": 1,
        "AZ": 2,
        "BX": 1,
        "BY": 2,
        "BZ": 3,
        "CX": 2,
        "CY": 3,
        "CZ": 1,
    }

    with open(input_file) as f:
        lines = f.readlines()

    total = 0

    for line in lines:
        permutation = "".join(line.strip().split(" "))
        total += outcome_based_score[permutation[1]] + choice_based_score[permutation]

    return total


print(f"Solution to Part One: {score_strategy_one('day2.txt')}\n")
print(f"Solution to Part Two: {score_strategy_two('day2.txt')}")
