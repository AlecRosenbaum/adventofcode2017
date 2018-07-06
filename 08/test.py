import unittest

from solution import solution_part_one, solution_part_two


class TestPartOne(unittest.TestCase):
    def test_one(self):
        program_input = """b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10"""
        self.assertEqual(solution_part_one(program_input), 1)


class TestPartTwo(unittest.TestCase):
    def test_one(self):
        program_input = """b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10"""
        self.assertEqual(solution_part_two(program_input), 10)

if __name__ == "__main__":
    unittest.main()
