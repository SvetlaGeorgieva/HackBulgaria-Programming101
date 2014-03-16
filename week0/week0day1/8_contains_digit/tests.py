import solution
import unittest


class SolutionTest(unittest.TestCase):
    """Testing Problem 8 - Number containing a single digit? module"""
    def test_contains_digit(self):
        self.assertEqual(False, solution.contains_digit(123, 4))
        self.assertEqual(True, solution.contains_digit(42, 2))
        self.assertEqual(True, solution.contains_digit(1000, 0))
        self.assertEqual(False, solution.contains_digit(12346789, 5))


if __name__ == '__main__':
    unittest.main()