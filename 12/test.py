import unittest

from solution import solution_part_one, solution_part_two


TEST_INPUT = """0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5"""

class TestPartOne(unittest.TestCase):
    def test_one(self):
        self.assertEqual(solution_part_one(TEST_INPUT), 6)


class TestPartTwo(unittest.TestCase):
    def test_one(self):
        self.assertEqual(solution_part_two(TEST_INPUT), 2)


if __name__ == "__main__":
    unittest.main()
