import utils


def is_safe(level: list[int]) -> bool:
    if level[0] < level[1]:
        for i in range(1, len(level)):
            if level[i - 1] >= level[i]:
                return False
    elif level[0] > level[1]:
        for i in range(1, len(level)):
            if level[i - 1] <= level[i]:
                return False
    else:
        return False

    diffs = [abs(a - b) for a, b in zip(level[:-1], level[1:])]
    return all([x >= 1 and x <= 3 for x in diffs])


def problem_dampener(level: list[int]) -> bool:
    for i in range(len(level)):
        l = level[:i] + level[i + 1 :]
        if is_safe(l):
            return True

    return False


def part1(levels: list[list[int]]):
    safe = [l for l in levels if is_safe(l)]

    print(len(safe))


def part2(levels: list[list[int]]):
    safe = [l for l in levels if is_safe(l)]
    dampened = [l for l in levels if not is_safe(l) and problem_dampener(l)]

    print(len(safe) + len(dampened))


if __name__ == "__main__":
    txt = utils.read_input()

    levels = [[int(y) for y in x.split(" ")] for x in txt.splitlines()]

    part1(levels)
    part2(levels)
