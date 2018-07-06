import unittest

from solution import solution_part_one, solution_part_two


class TestPartOne(unittest.TestCase):
    def test_one(self):
        self.assertEqual(solution_part_one([3, 4, 1, 5], num_elements=5), 12)


class TestPartTwo(unittest.TestCase):
    def test_one(self):
        self.assertEqual(solution_part_two("AoC 2017"), "33efeb34ea91902bb2f59c9920caa6cd")
        self.assertEqual(solution_part_two("1,2,3"), "3efbe78a8d82f29979031a4aa0b16a9d")
        self.assertEqual(solution_part_two("1,2,4"), "63960835bcdc130f0b66d7ff4f6a5a8e")

if __name__ == "__main__":
    unittest.main()
