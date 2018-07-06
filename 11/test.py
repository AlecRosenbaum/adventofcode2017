import unittest

from solution import solution_part_one, solution_part_two


class TestPartOne(unittest.TestCase):
    def test_one(self):
        self.assertEqual(solution_part_one("ne,ne,ne"), 3)
    def test_two(self):
        self.assertEqual(solution_part_one("ne,ne,sw,sw"), 0)
    def test_three(self):
        self.assertEqual(solution_part_one("ne,ne,s,s"), 2)
    def test_four(self):
        self.assertEqual(solution_part_one("se,sw,se,sw,sw"), 3)


class TestPartTwo(unittest.TestCase):
    def test_one(self):
        self.assertEqual(solution_part_two("ne,ne,ne"), 3)
    def test_two(self):
        self.assertEqual(solution_part_two("ne,ne,sw,sw"), 2)
    def test_three(self):
        self.assertEqual(solution_part_two("ne,ne,s,s"), 2)
    def test_four(self):
        self.assertEqual(solution_part_two("se,sw,se,sw,sw"), 3)

if __name__ == "__main__":
    unittest.main()
