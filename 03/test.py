import unittest

from solution import solution_part_one, solution_part_two


class TestPartOne(unittest.TestCase):
    def test_one(self):
        self.assertEqual(solution_part_one(1), 0)
    def test_two(self):
        self.assertEqual(solution_part_one(12), 3)
    def test_three(self):
        self.assertEqual(solution_part_one(23), 2)
    def test_four(self):
        self.assertEqual(solution_part_one(1024), 31)


class TestPartTwo(unittest.TestCase):
    def test_one(self):
        self.assertEqual(solution_part_two(7), 10)
    def test_two(self):
        self.assertEqual(solution_part_two(5), 10)
    def test_three(self):
        self.assertEqual(solution_part_two(10), 11)


if __name__ == "__main__":
    unittest.main()
