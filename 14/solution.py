"""
Day 14 challenge
"""
import attr
from functools import reduce


@attr.s
class Row(object):
    key = attr.ib()

    def cells(self):
        knot_hash = calculate_knot(self.key)
        return bin(int(knot_hash, 16))[2:].zfill(128)


def calculate_knot(arg, num_elements=256):
    """Copied form day 10, part 2"""
    my_list = list(range(num_elements))
    lengths = list(map(ord, arg)) + [17, 31, 73, 47, 23]
    skip_size = 0
    curr_position = 0

    for _ in range(64):
        for length in lengths:
            # reverse length elements starting at curr_position
            elements = [my_list[(curr_position + idx) % len(my_list)] for idx in range(length)]
            for idx, elem in enumerate(reversed(elements)):
                my_list[(curr_position + idx) % len(my_list)] = elem

            # bump curr_position
            curr_position += length + skip_size

            # bump skip size
            skip_size += 1

    dense_hash = []
    for start in range(len(my_list)//16):
        dense_hash.append(reduce(lambda agg, x: agg ^ x, my_list[(start*16)+1:(start*16)+16], my_list[(start*16)]))

    return "".join([f"0{i[2:]}"[-2:] for i in map(hex, dense_hash)])


def solution_part_one(arg):
    return sum([
        Row(key=f"{arg}-{i}").cells().count("1")
        for i in range(128)
    ])


def solution_part_two(arg):
    disk = [
        list(map(int, Row(key=f"{arg}-{i}").cells()))
        for i in range(128)
    ]

    # for i in range(8):
    #     for j in range(8):
    #         print(disk[i][j], end="")
    #     print("")

    OFFSETS = [
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1),
    ]

    groups = {}
    for row_num, row in enumerate(disk):
        for col_num, col in enumerate(row):
            if col:
                merge_groups = []
                for offset in OFFSETS:
                    group = groups.get((row_num + offset[0], col_num + offset[1]))
                    if group:
                        merge_groups.append(group)
                if merge_groups:
                    # merge those groups into single larger group
                    new_group = min(merge_groups)
                    for k, v in groups.items():
                        if v in merge_groups:
                            groups[k] = new_group
                    groups[(row_num, col_num)] = new_group
                else:
                    # assign new group number
                    groups[(row_num, col_num)] = max(groups.values(), default=0) + 1

    # for i in range(8):
    #     for j in range(8):
    #         group = groups.get((i, j))
    #         print((" " + str(group or "."))[-2:], end="")
    #     print("")
    return len(set(groups.values()))


if __name__ == "__main__":
    puzzle_input = """stpzcrnm"""
    print(solution_part_one(puzzle_input))
    print(solution_part_two(puzzle_input))
