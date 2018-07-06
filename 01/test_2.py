import unittest

from solution_2 import solution

class TestDay1(unittest.TestCase):

    def test_one(self):
        self.assertEqual(solution("1212"), 6)

    def test_two(self):
        self.assertEqual(solution("1221"), 0)

    def test_three(self):
        self.assertEqual(solution("123425"), 4)

    def test_four(self):
        self.assertEqual(solution("123123"), 12)

    def test_five(self):
        self.assertEqual(solution("12131415"), 4)

if __name__ == '__main__':
    unittest.main()