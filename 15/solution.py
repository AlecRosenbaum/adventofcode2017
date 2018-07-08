"""
Day 14 challenge
"""
import attr
from functools import reduce


@attr.s
class Generator(object):
    val = attr.ib()
    mult_factor= attr.ib()

    def get(self):
        self.val = (self.val * self.mult_factor) % 2147483647
        return self.val

    def get_multiple_of(self, multiple_val):
        while self.get() % multiple_val:
            pass
        return self.val



def solution_part_one(a=873, b=583):
    gen_a = Generator(val=a, mult_factor=16807)
    gen_b = Generator(val=b, mult_factor=48271)
    return sum([
        1 if gen_a.get() % 65536 == gen_b.get() % 65536 else 0
        for _ in range(40000000)
    ])


def solution_part_two(a=873, b=583):
    gen_a = Generator(val=a, mult_factor=16807)
    gen_b = Generator(val=b, mult_factor=48271)
    return sum([
        1 if gen_a.get_multiple_of(4) % 65536 == gen_b.get_multiple_of(8) % 65536 else 0
        for _ in range(5000000)
    ])


if __name__ == "__main__":
    print(solution_part_one(a=873, b=583))
    print(solution_part_two(a=873, b=583))
