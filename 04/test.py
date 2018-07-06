import unittest

from solution import solution_part_one, solution_part_two


class TestPartOne(unittest.TestCase):
    def test_one(self):
        self.assertEqual(solution_part_one("aa bb cc dd ee"), 1)
    def test_two(self):
        self.assertEqual(solution_part_one("aa bb cc dd aa"), 0)
    def test_three(self):
        self.assertEqual(solution_part_one("aa bb cc dd aaa"), 1)


class TestPartTwo(unittest.TestCase):
    def test_one(self):
        self.assertEqual(solution_part_two("abcde fghij"), 1)
    def test_two(self):
        self.assertEqual(solution_part_two("abcde xyz ecdab"), 0)
    def test_three(self):
        self.assertEqual(solution_part_two("a ab abc abd abf abj"), 1)
    def test_four(self):
        self.assertEqual(solution_part_two("iiii oiii ooii oooi oooo"), 1)
    def test_five(self):
        self.assertEqual(solution_part_two("oiii ioii iioi iiio"), 0)

if __name__ == "__main__":
    unittest.main()
