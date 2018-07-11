import unittest

from solution import solution_part_one, solution_part_two


class TestPartOne(unittest.TestCase):
    def test_one(self):
        self.assertEqual(solution_part_one("s1,x3/4,pe/b", groups_len=5), "baedc")


class TestPartTwo(unittest.TestCase):
    def test_one(self):
        self.assertEqual(solution_part_two("s1,x3/4,pe/b", groups_len=5, iterations=2), "ceadb")


if __name__ == "__main__":
    unittest.main()
