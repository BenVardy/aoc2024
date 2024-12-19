from __future__ import annotations

from typing import Any


class IVec2:
    i: int
    j: int

    def __init__(self, i: int, j: int) -> None:
        self.i = i
        self.j = j

    def __eq__(self, o: Any) -> bool:
        if type(o) != IVec2:
            return False

        return self.i == o.i and self.j == o.j

    def __ne__(self, o: Any) -> bool:
        return not (self == o)

    def __hash__(self) -> int:
        return hash((self.i, self.j))

    def __add__(self, o: Any) -> IVec2:
        if type(o) != IVec2:
            raise TypeError(f"Cannot add type '{type(o)}' to IVec2")

        return IVec2(self.i + o.i, self.j + o.j)

    __radd__ = __add__

    def __iadd__(self, o: Any) -> IVec2:
        if type(o) != IVec2:
            raise TypeError()

        self.i += o.i
        self.j += o.j
        return self

    def __sub__(self, o: Any) -> IVec2:
        if type(o) != IVec2:
            raise TypeError()

        return IVec2(self.i - o.i, self.j - o.j)

    __rsub__ = __sub__

    def __isub__(self, o: Any) -> IVec2:
        if type(o) != IVec2:
            raise TypeError()

        self.i -= o.i
        self.j -= o.j
        return self

    def __mul__(self, o: Any) -> IVec2:
        if type(o) != int:
            raise TypeError()

        return IVec2(self.i * o, self.j * o)

    __rmul__ = __mul__

    def __imul__(self, o: Any) -> IVec2:
        if type(o) != int:
            raise TypeError()

        self.i *= o
        self.j *= o
        return self

    def __truediv__(self, o: Any) -> IVec2:
        if type(o) != int:
            raise TypeError()

        return IVec2(self.i / o, self.j / o)

    __rtruediv__ = __truediv__

    def __itruediv__(self, o: Any) -> IVec2:
        if type(o) != int:
            raise TypeError()

        self.i /= o
        self.j /= o
        return self

    def __neg__(self) -> IVec2:
        return IVec2(-self.i, -self.j)

    def __str__(self) -> str:
        return "v[{}, {}]".format(self.i, self.j)

    def __repr__(self) -> str:
        return self.__str__()

    def abs(self) -> IVec2:
        return IVec2(abs(self.i), abs(self.j))

    def manhattan(self, o: IVec2) -> int:
        diff = (self - o).abs()
        return diff.i + diff.j

    def in_box(self, i_bound: IVec2, j_bound: IVec2) -> bool:
        return (
            self.i >= i_bound.i
            and self.i < i_bound.j
            and self.j >= j_bound.i
            and self.j < j_bound.j
        )

    def copy(self) -> IVec2:
        return IVec2(self.i, self.j)
