import unittest

from solution import solution

class TestDay1(unittest.TestCase):

    def test_one(self):
        self.assertEqual(solution("1122"), 3)

    def test_two(self):
        self.assertEqual(solution("1111"), 4)

    def test_three(self):
        self.assertEqual(solution("1234"), 0)

    def test_one(self):
        self.assertEqual(solution("91212129"), 9)

if __name__ == '__main__':
    unittest.main()