import unittest

from solution import solution_part_one, solution_part_two


class TestPartOne(unittest.TestCase):
    def test_one(self):
        self.assertEqual(solution_part_one([0, 3, 0, 1, -3]), 5)


class TestPartTwo(unittest.TestCase):
    def test_one(self):
        self.assertEqual(solution_part_two([0, 3, 0, 1, -3]), 10)

if __name__ == "__main__":
    unittest.main()
