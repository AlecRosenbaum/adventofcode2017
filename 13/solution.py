"""
Day 13 challenge
"""
import attr


@attr.s
class Layer(object):
    layer = attr.ib()
    scan_range = attr.ib()


def solution_part_one(arg):
    layers = []
    for line in arg.split("\n"):
        layer, scan_range = line.split(": ")
        layers.append(Layer(layer=int(layer), scan_range=int(scan_range)))

    severity = 0
    for layer in layers:
        if layer.layer % ((layer.scan_range - 1) * 2) == 0:
            severity += layer.layer * layer.scan_range

    return severity


def solution_part_two(arg):
    layers = []
    for line in arg.split("\n"):
        layer, scan_range = line.split(": ")
        layers.append(Layer(layer=int(layer), scan_range=int(scan_range)))

    def was_caught(delay):
        for layer in layers:
            if (delay + layer.layer) % ((layer.scan_range - 1) * 2) == 0:
                return True
        return False

    delay = 0
    while was_caught(delay):
        delay += 1

    return delay


if __name__ == "__main__":
    puzzle_input = """0: 5
1: 2
2: 3
4: 4
6: 6
8: 4
10: 8
12: 6
14: 6
16: 8
18: 6
20: 9
22: 8
24: 10
26: 8
28: 8
30: 12
32: 8
34: 12
36: 10
38: 12
40: 12
42: 12
44: 12
46: 12
48: 14
50: 12
52: 14
54: 12
56: 14
58: 12
60: 14
62: 14
64: 14
66: 14
68: 14
70: 14
72: 14
76: 14
80: 18
84: 14
90: 18
92: 17"""
    print(solution_part_one(puzzle_input))
    print(solution_part_two(puzzle_input))
