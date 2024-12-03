import re

import utils


def part1(txt: str) -> None:
    PATTERN = r"mul\((\d+),(\d+)\)"
    print(sum(int(x.group(1)) * int(x.group(2)) for x in re.finditer(PATTERN, txt)))


def part2(txt: str) -> None:
    PATTERN = r"(mul\((\d+),(\d+)\))|(do\(\))|(don't\(\))"

    enabled = True
    total = 0

    for m in re.finditer(PATTERN, txt):
        token = m.groups()
        if token[0] is not None and enabled:
            total += int(token[1]) * int(token[2])
        elif token[3] is not None:
            enabled = True
        elif token[4] is not None:
            enabled = False

    print(total)


if __name__ == "__main__":
    txt = utils.read_input()

    part1(txt)
    part2(txt)
