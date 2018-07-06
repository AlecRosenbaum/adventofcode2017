import unittest

from solution import solution_part_one, solution_part_two


TEST_INPUT = """0: 3
1: 2
4: 4
6: 4"""

class TestPartOne(unittest.TestCase):
    def test_one(self):
        self.assertEqual(solution_part_one(TEST_INPUT), 24)


class TestPartTwo(unittest.TestCase):
    def test_one(self):
        self.assertEqual(solution_part_two(TEST_INPUT), 10)


if __name__ == "__main__":
    unittest.main()
