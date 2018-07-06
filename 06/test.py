import unittest

from solution import solution_part_one, solution_part_two


class TestPartOne(unittest.TestCase):
    def test_one(self):
        self.assertEqual(solution_part_one([0, 2, 7, 1]), 5)


class TestPartTwo(unittest.TestCase):
    def test_one(self):
        self.assertEqual(solution_part_two([0, 2, 7, 1]), 4)

if __name__ == "__main__":
    unittest.main()
