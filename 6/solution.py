"""
Day 5 challenge
"""
import attr


def solution_part_one(arg):
    banks = arg[:]
    n = 0
    seen_sets = set()
    while tuple(banks) not in seen_sets:
        seen_sets.add(tuple(banks))
        idx = banks.index(max(banks))
        val = banks[idx]
        banks[idx] = 0
        for i in range(val):
            banks[(idx + i + 1) % len(banks)] += 1
        n += 1

    return n


def solution_part_two(arg):
    banks = arg[:]
    n = 0
    seen_sets = set()
    match = None
    while match is None or tuple(banks) != match:
        if not match and tuple(banks) in seen_sets:
            match = tuple(banks)
            n = 0
        seen_sets.add(tuple(banks))
        idx = banks.index(max(banks))
        val = banks[idx]
        banks[idx] = 0
        for i in range(val):
            banks[(idx + i + 1) % len(banks)] += 1
        n += 1

    return n


if __name__ == "__main__":
    puzzle_input = [
        5, 1, 10, 0, 1, 7, 13, 14, 3, 12, 8, 10, 7, 12, 0, 6,
    ]

    print(solution_part_one(puzzle_input))
    print(solution_part_two(puzzle_input))
