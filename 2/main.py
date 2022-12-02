from utils import open_input_file

MAPS = {
    "A": 1,  # Rock
    "B": 2,  # Paper
    "C": 3,  # Scissors,
    "X": 1,
    "Y": 2,
    "Z": 3
}


def get_outcome(a, b):
    if a == b:
        return 3
    if (b > a and b - a != 2) or (a > b and a - b == 2):
        return 6
    return 0


def check_point(a, b):
    first_player = MAPS[a]
    second_player = MAPS[b]
    outcome = get_outcome(first_player, second_player)
    return outcome + second_player


OUTCOME = {
    "X": 0,  # Lose
    "Y": 3,  # Draw
    "Z": 6  # Win
}


def get_part_2_answer(a, outcome):
    if outcome == "Y":
        return a
    if outcome == "Z":
        answer = a + 1
        if answer == 4:
            answer = 1
    if outcome == "X":
        answer = a - 1
        if answer == 0:
            answer = 3
    return answer


def check_point_part_2(a, outcome):
    a_to_num = MAPS[a]
    return get_part_2_answer(a_to_num, outcome) + OUTCOME[outcome]


if __name__ == '__main__':
    data = open_input_file("2/input.txt")
    rounds = [x.split(" ") for x in data.split("\n")]
    # Part 1
    total_score = sum([check_point(*m) for m in rounds])
    print(total_score)

    # Part 2
    total_score = sum([check_point_part_2(*m) for m in rounds])
    print(total_score)
