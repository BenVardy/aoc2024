import itertools

import utils


def part1(txt: list[str]) -> None:
    total = 0

    PAT = "XMAS"
    D = [-1, 0, 1]

    n_cols = len(txt[0])

    for i, j in itertools.product(range(len(txt)), range(n_cols)):
        if txt[i][j] != "X":
            continue

        for di, dj in itertools.product(D, D):
            if di == 0 and dj == 0:
                continue

            try:
                if i + (di * 3) < 0 or j + (dj * 3) < 0:
                    continue

                if all(
                    txt[i + (di * m)][j + (dj * m)] == PAT[m]
                    for m in range(1, len(PAT))
                ):
                    total += 1
            except IndexError:
                continue

    print(total)


def part2(txt: list[str]) -> None:
    total = 0
    n_cols = len(txt[0])

    for i, j in itertools.product(range(1, len(txt)), range(1, n_cols)):
        if txt[i][j] != "A":
            continue

        try:
            l = txt[i - 1][j - 1]
            r = txt[i - 1][j + 1]
            if (l != "M" and l != "S") or (r != "M" and r != "S"):
                continue

            l2 = "M" if l == "S" else "S"
            r2 = "M" if r == "S" else "S"

            if txt[i + 1][j - 1] == r2 and txt[i + 1][j + 1] == l2:
                total += 1

        except IndexError:
            continue

    print(total)


if __name__ == "__main__":
    txt = utils.read_input()

    txt = txt.splitlines()

    part1(txt)
    part2(txt)
