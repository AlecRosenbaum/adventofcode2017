import unittest

from solution import solution_part_one, solution_part_two


class TestPartOne(unittest.TestCase):
    def test_one(self):
        self.assertEqual(solution_part_one(a=65, b=8921), 588)


class TestPartTwo(unittest.TestCase):
    def test_one(self):
        self.assertEqual(solution_part_two(a=65, b=8921), 309)


if __name__ == "__main__":
    unittest.main()
