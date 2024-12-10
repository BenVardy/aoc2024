import itertools
import utils

pos_t = tuple[int, int]
map_t = list[list[str]]


def find_guard(_map: map_t) -> pos_t:
    for i, r in enumerate(_map):
        for j, v in enumerate(r):
            if v == "^":
                return (i, j)

    return None


def part1(_map: map_t, guard_start: pos_t) -> None:
    _map = [x[::] for x in _map]
    _map[guard_start[0]][guard_start[1]] == "0"
    guard = guard_start
    _dir: pos_t = (-1, 0)

    n = len(_map)
    m = len(_map[0])

    counter = 1

    while True:
        next_pos = (guard[0] + _dir[0], guard[1] + _dir[1])
        if next_pos[0] < 0 or next_pos[0] >= n or next_pos[1] < 0 or next_pos[1] >= m:
            break
        if _map[next_pos[0]][next_pos[1]] == "#":
            _dir = (_dir[1], -_dir[0])
        else:
            guard = next_pos
            if _map[next_pos[0]][next_pos[1]] == ".":
                _map[next_pos[0]][next_pos[1]] = str(counter)
                counter += 1

    # print("\n".join("".join(x.rjust(len(str(counter)) + 1) for x in r) for r in _map))

    print(counter)


def __traverse(_map: map_t, guard_start: pos_t) -> bool:
    n = len(_map)
    m = len(_map[0])

    guard = guard_start
    _dir: pos_t = (-1, 0)
    # Traverse.
    moves = 0

    prevs = set()
    while True:
        # print(moves)
        next_pos = (guard[0] + _dir[0], guard[1] + _dir[1])
        if next_pos[0] < 0 or next_pos[0] >= n or next_pos[1] < 0 or next_pos[1] >= m:
            break

        # print(next_pos, guard_start, _dir)
        if (*next_pos, *_dir) in prevs:
            # print("here")
            # return next_pos == guard_start and _dir == (-1, 0)
            return True

        if _map[next_pos[0]][next_pos[1]] == "#":
            _dir = (_dir[1], -_dir[0])
        else:
            guard = next_pos
            if _map[next_pos[0]][next_pos[1]] == ".":
                _map[next_pos[0]][next_pos[1]] = str(moves)
                moves += 1
                prevs.add((*guard, *_dir))

    return False


def part2(_map: map_t, guard_start: pos_t) -> None:
    counter = 0
    n = len(_map)
    m = len(_map[0])

    for oi, oj in itertools.product(range(n), range(m)):
        # print(counter)
        new_map = [x[::] for x in _map]
        if new_map[oi][oj] != ".":
            continue

        new_map[oi][oj] = "#"

        if __traverse(new_map, guard_start):
            counter += 1

    print(counter)


if __name__ == "__main__":
    txt = utils.read_input()

    _map = [list(l) for l in txt.splitlines()]
    guard_start = find_guard(_map)
    _map[guard_start[0]]

    part1(_map, guard_start)
    part2(_map, guard_start)
