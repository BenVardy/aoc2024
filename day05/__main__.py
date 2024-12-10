import utils


rules_t = list[tuple[int, int]]
updates_t = list[int]


def is_valid(rules: rules_t, a: int, b: int) -> bool:
    return (b, a) not in rules


def part1(rules: rules_t, updates: updates_t) -> None:
    valid_updates = []

    for u in updates:
        if all(
            all(is_valid(rules, u1, u2) for u2 in u[i + 1 :])
            for i, u1 in enumerate(u[:-1])
        ):
            valid_updates.append(u)

    ans = sum(vu[len(vu) // 2] for vu in valid_updates)
    print(ans)


def part2(rules: rules_t, updates: updates_t) -> None:
    invalid_updates = []

    for u in updates:
        if not all(
            all(is_valid(rules, u1, u2) for u2 in u[i + 1 :])
            for i, u1 in enumerate(u[:-1])
        ):
            invalid_updates.append(u)

    for u in invalid_updates:
        # Bubble sort the things.
        for n in range(1, len(u)):
            changed = False
            for i in range(len(u) - n):
                if not is_valid(rules, u[i], u[i + 1]):
                    changed = True
                    temp = u[i]
                    u[i] = u[i + 1]
                    u[i + 1] = temp

            if not changed:
                break

    ans = sum(vu[len(vu) // 2] for vu in invalid_updates)
    print(ans)


if __name__ == "__main__":
    txt = utils.read_input()

    rules_txt, updates_txt = txt.split("\n\n")

    rules = []
    for l in rules_txt.splitlines():
        a, b = l.split("|")

        rules.append((int(a), int(b)))

    updates = [[int(x) for x in l.split(",")] for l in updates_txt.splitlines()]

    part1(rules, updates)
    part2(rules, updates)
