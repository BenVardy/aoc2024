import sys

import itertools


def part1(left: list[int], right: list[int]) -> None:
    left = sorted(left)
    right = sorted(right)

    print(sum(abs(a - b) for a, b in zip(left, right)))


def part2(left: list[int], right: list[int]) -> None:
    left = sorted(left)
    right = sorted(right)

    print(sum(x * right.count(x) for x in left))


if __name__ == "__main__":
    with open(sys.argv[1], "r") as f:
        txt = f.readlines()

    left = []
    right = []
    for line in txt:
        a, b = line.split("   ", 2)
        left.append(int(a))
        right.append(int(b))

    part1(left, right)

    part2(left, right)
