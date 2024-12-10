import utils

ADD = 0
MUL = 1
CONCAT = 2

eq_t = tuple[int, list[int]]


def partial_eval(ints: list[int], assigns: list[int]) -> int:
    assert len(assigns) < len(ints)

    total = ints[0]
    for i, a in zip(ints[1:], assigns):
        if a == ADD:
            total += i
        elif a == MUL:
            total *= i
        elif a == CONCAT:
            total = int(str(total) + str(i))

    return total


def bt(t: int, ints: list[int], ops: list[int], assigns: list[int]) -> bool:
    assigns = assigns[::]

    for x in ops:
        assigns.append(x)
        p_eval = partial_eval(ints, assigns)
        if p_eval <= t:
            if len(assigns) == len(ints) - 1:
                if p_eval == t:
                    return True
            else:
                if bt(t, ints, ops, assigns):
                    return True
        assigns = assigns[:-1]

    return False


def part1(eqs: list[eq_t]) -> None:
    total = 0

    for t, ints in eqs:
        if bt(t, ints, [ADD, MUL], []):
            total += t

    print(total)


def part2(eqs: list[eq_t]) -> None:
    total = 0

    for t, ints in eqs:
        if bt(t, ints, [ADD, MUL, CONCAT], []):
            total += t

    print(total)


if __name__ == "__main__":
    lines = utils.read_lines()

    eqs = [tuple(x.split(": ")) for x in lines]
    eqs = [(int(a), [int(x) for x in b.split(" ")]) for a, b in eqs]

    # part1(eqs)
    part2(eqs)
