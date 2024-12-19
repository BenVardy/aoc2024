import itertools

import utils
from utils import IVec2


antenna_t = dict[str, list[IVec2]]


def search(_map: list[list[str]]) -> antenna_t:
    res: antenna_t = {}

    for i, j in itertools.product(range(len(_map)), range(len(_map[0]))):
        v = _map[i][j]
        if v != ".":
            if v not in res:
                res[v] = []
            res[v].append(IVec2(i, j))

    return res


def part1(_map: list[list[str]]) -> None:
    _map = [x[::] for x in _map]
    antennas = search(_map)

    bb = (IVec2(0, len(_map)), IVec2(0, len(_map[0])))

    anti_nodes = set()

    for locs in antennas.values():
        for a, b in itertools.combinations(locs, 2):
            diff = b - a

            c = a - diff
            d = b + diff

            if c.in_box(*bb):
                _map[c.i][c.j] = "#"
                anti_nodes.add(c)

            if d.in_box(*bb):
                _map[d.i][d.j] = "#"
                anti_nodes.add(d)

    utils.print_map(_map)
    print(len(anti_nodes))


def part2(_map: list[list[str]]) -> None:
    _map = [x[::] for x in _map]
    antennas = search(_map)

    bb = (IVec2(0, len(_map)), IVec2(0, len(_map[0])))

    anti_nodes = set()

    for locs in antennas.values():
        for a, b in itertools.combinations(locs, 2):
            print(a, b)
            anti_nodes.add(a)
            anti_nodes.add(b)
            diff = b - a

            c = a.copy()
            while True:
                c -= diff
                if c.in_box(*bb):
                    print(c)
                    if _map[c.i][c.j] == ".":
                        _map[c.i][c.j] = "#"
                    anti_nodes.add(c.copy())
                else:
                    break

            d = b.copy()
            while True:
                d += diff
                if d.in_box(*bb):
                    if _map[d.i][d.j] == ".":
                        _map[d.i][d.j] = "#"
                    anti_nodes.add(d.copy())
                else:
                    break

    utils.print_map(_map)
    print(len(anti_nodes))


if __name__ == "__main__":
    txt = utils.read_input()

    _map = [list(x) for x in txt.splitlines()]

    # part1(_map)
    part2(_map)
