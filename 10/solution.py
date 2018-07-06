"""
Day 9 challenge
"""
import attr
from functools import reduce


def solution_part_one(arg, num_elements=256):
    my_list = list(range(num_elements))
    lengths = arg[:]
    skip_size = 0
    curr_position = 0

    for length in lengths:
        # reverse length elements starting at curr_position
        elements = [my_list[(curr_position + idx) % len(my_list)] for idx in range(length)]
        for idx, elem in enumerate(reversed(elements)):
            my_list[(curr_position + idx) % len(my_list)] = elem

        # bump curr_position
        curr_position += length + skip_size

        # bump skip size
        skip_size += 1

    return my_list[0] * my_list[1]


def solution_part_two(arg, num_elements=256):
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


if __name__ == "__main__":
    print(solution_part_one([192,69,168,160,78,1,166,28,0,83,198,2,254,255,41,12]))
    print(solution_part_two("192,69,168,160,78,1,166,28,0,83,198,2,254,255,41,12"))
