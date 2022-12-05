from utils import open_input_file


def get_priority(c):
    priority = ord(c.lower()) - 96
    if c.isupper():
        priority += 26
    return priority


def find_match(*args):
    intersect = set(args[0])
    for s in args[1:]:
        intersect = intersect.intersection(s)
    return list(intersect)


def task_1(rs):
    matching = []
    for s in rs:
        matching += find_match(*s)
    return sum([get_priority(c) for c in matching])


def task_2(rs):
    matching = []
    for idx in range(0, len(rs), 3):
        matching += find_match(*rs[idx:idx + 3])
    return sum(get_priority(c[0]) for c in matching)

if __name__ == '__main__':
    data = open_input_file("3/input.txt")
    rucksacks = data.split("\n")

    # Task 1
    #rucksacks = [[list(r)[:int(len(r) / 2)], list(r)[int(len(r) / 2):]] for r in rucksacks]
    #print(task_1(rucksacks))

    #Task 2
    print(task_2(rucksacks))
