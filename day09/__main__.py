import itertools

import utils


def to_blocks(ints: list[int]) -> list[str]:
    blocks = []
    for i, x in enumerate(ints):
        if i % 2 == 0:
            blocks += x * [str(i // 2)]
        else:
            blocks += x * ["."]

    return blocks


def part1(ints: list[int]) -> None:
    blocks = to_blocks(ints)

    n_blocks = blocks[::]

    free_p = n_blocks.index(".")
    for i in range(len(blocks) - 1, -1, -1):
        if free_p >= i:
            break

        if blocks[i] == ".":
            continue

        n_blocks[free_p] = blocks[i]
        n_blocks[i] = "."
        free_p = blocks.index(".", free_p + 1)

    print(sum(int(x) * i for i, x in enumerate(n_blocks) if x != "."))


def part2(ints: list[int]) -> None:
    blocks = to_blocks(ints)

    n_blocks = blocks[::]
    groups = list(enumerate(ints[::2]))[::-1]
    for i, g in groups:
        start = blocks.index(str(i))
        c_groups = [(a, len(list(b))) for a, b in itertools.groupby(n_blocks[:start])]
        # print(c_groups)

        insert_start = 0
        for j, h in c_groups:
            if j == "." and g <= h:
                for k in range(insert_start, insert_start + g):
                    n_blocks[k] = str(i)
                for k in range(start, start + g):
                    n_blocks[k] = "."

                break

            insert_start += h

    print(sum(int(x) * i for i, x in enumerate(n_blocks) if x != "."))


if __name__ == "__main__":
    txt = utils.read_input()
    ints = [int(x) for x in list(txt.rstrip())]

    part1(ints)
    part2(ints)
