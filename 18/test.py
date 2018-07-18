import unittest

from solution import solution_part_one, solution_part_two


class TestPartOne(unittest.TestCase):
    TEST_INPUT = """
set a 1
add a 2
mul a a
mod a 5
snd a
set a 0
rcv a
jgz a -1
set a 1
jgz a -2
"""
    def test_one(self):
        self.assertEqual(solution_part_one(self.TEST_INPUT), 4)


# class TestPartTwo(unittest.TestCase):
#     def test_one(self):
#         self.assertEqual(solution_part_two(3), 1222153)


if __name__ == "__main__":
    unittest.main()
