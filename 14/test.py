import unittest

from solution import solution_part_one, solution_part_two


TEST_INPUT = """flqrgnkx"""

class TestPartOne(unittest.TestCase):
    def test_one(self):
        self.assertEqual(solution_part_one(TEST_INPUT), 8108)


class TestPartTwo(unittest.TestCase):
    def test_one(self):
        self.assertEqual(solution_part_two(TEST_INPUT), 1242)


if __name__ == "__main__":
    unittest.main()
