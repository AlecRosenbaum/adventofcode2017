import unittest

from solution import solution_part_one, solution_part_two


class TestPartOne(unittest.TestCase):
    def test_one(self):
        self.assertEqual(solution_part_one(r"{}"), 1)
    def test_two(self):
        self.assertEqual(solution_part_one(r"{{{}}}"), 6)
    def test_three(self):
        self.assertEqual(solution_part_one(r"{{},{}}"), 5)
    def test_four(self):
        self.assertEqual(solution_part_one(r"{{{},{},{{}}}}"), 16)
    def test_five(self):
        self.assertEqual(solution_part_one(r"{<a>,<a>,<a>,<a>}"), 1)
    def test_six(self):
        self.assertEqual(solution_part_one(r"{{<ab>},{<ab>},{<ab>},{<ab>}}"), 9)
    def test_seven(self):
        self.assertEqual(solution_part_one(r"{{<!!>},{<!!>},{<!!>},{<!!>}}"), 9)
    def test_eight(self):
        self.assertEqual(solution_part_one(r"{{<a!>},{<a!>},{<a!>},{<ab>}}"), 3)


class TestPartTwo(unittest.TestCase):
    def test_one(self):
        self.assertEqual(solution_part_two(r"{<>}"), 0)
    def test_two(self):
        self.assertEqual(solution_part_two(r"{<random characters>}"), 17)
    def test_three(self):
        self.assertEqual(solution_part_two(r"{<<<<>}"), 3)
    def test_four(self):
        self.assertEqual(solution_part_two(r"{<{!>}>}"), 2)
    def test_five(self):
        self.assertEqual(solution_part_two(r"{<!!>}"), 0)
    def test_six(self):
        self.assertEqual(solution_part_two(r"{<!!!>>}"), 0)
    def test_seven(self):
        self.assertEqual(solution_part_two(r'{<{o"i!a,<{i<a>}'), 10)


if __name__ == "__main__":
    unittest.main()
