"""
Day 3 challenge
"""
import attr

from queue import Queue


@attr.s
class Offset(object):
    horizontal = attr.ib(default=0)
    vertical = attr.ib(default=0)
    name = attr.ib(default=None)

    def add(self, offset):
        self.horizontal += offset.horizontal
        self.vertical += offset.vertical

    def __add__(self, other):
        return self.__class__(
            horizontal=self.horizontal + other.horizontal,
            vertical=self.vertical + other.vertical,
        )

    def __str__(self):
        if name:
            return name
        return super(Offset).__str__()


@attr.s
class State(object):
    max_offset = attr.ib(default=0)
    offset = attr.ib(default=attr.Factory(Offset))
    position = attr.ib(default=1)

    def move(self, direction):
        self.offset.add(direction)
        self.position += 1


@attr.s
class Board(object):
    _data = attr.ib(default=attr.Factory(dict))

    def set(self, offset, value):
        self._data[(offset.horizontal, offset.vertical)] = value

    def get(self, offset):
        return self._data.get((offset.horizontal, offset.vertical), 0)


def solution_part_one(arg):
    left = Offset(horizontal=-1, name="left")
    right = Offset(horizontal=1, name="right")
    up = Offset(vertical=1, name="up")
    down = Offset(vertical=-1, name="down")

    state = State()

    queue = Queue()
    queue.put(right)
    queue.put(up)
    n = 2
    while state.position < arg:
        state.move(queue.get())
        if queue.empty():
            if n % 2 == 1:
                tuple(map(queue.put, [right] * n))
                tuple(map(queue.put, [up] * n))
            else:
                tuple(map(queue.put, [left] * n))
                tuple(map(queue.put, [down] * n))
            n += 1

    return sum(map(abs, (state.offset.vertical, state.offset.horizontal)))


def solution_part_two(arg):
    W = Offset(horizontal=-1)
    N = Offset(vertical=1)
    E = Offset(horizontal=1)
    S = Offset(vertical=-1)
    NW = N + W
    NE = N + E
    SW = S + W
    SE = S + E

    directions = [W, NW, N, NE, E, SE, S, SW]
    state = State()
    board = Board()

    queue = Queue()
    queue.put(E)
    queue.put(N)
    n = 2
    board.set(Offset(), 1)
    while board.get(state.offset) <= arg:
        state.move(queue.get())
        board.set(
            state.offset,
            sum([board.get(state.offset + direction) for direction in directions]),
        )
        if queue.empty():
            if n % 2 == 1:
                tuple(map(queue.put, [E] * n))
                tuple(map(queue.put, [N] * n))
            else:
                tuple(map(queue.put, [W] * n))
                tuple(map(queue.put, [S] * n))
            n += 1
    return board.get(state.offset)


if __name__ == "__main__":
    puzzle_input = 277678

    print(solution_part_one(puzzle_input))
    print(solution_part_two(puzzle_input))
