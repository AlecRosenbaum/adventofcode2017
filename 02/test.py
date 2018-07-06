import unittest

from solution import solution_part_one, solution_part_two


class TestPartOne(unittest.TestCase):
    def test_one(self):
        test_string = """
            5 1 9 5
            7 5 3
            2 4 6 8
        """
        self.assertEqual(solution_part_one(test_string), 18)


class TestPartTwo(unittest.TestCase):
    def test_one(self):
        test_string = """
            5 9 2 8
            9 4 7 3
            3 8 6 5
        """
        self.assertEqual(solution_part_two(test_string), 9)


if __name__ == "__main__":
    unittest.main()
