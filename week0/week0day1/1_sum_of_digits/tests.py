import solution
import unittest


class SolutionTest(unittest.TestCase):
    """Testing Problem 1 - Sum all digits of a number module"""
    def test_sum_of_digits(self):
        self.assertEqual(43, solution.sum_of_digits(1325132435356))
        self.assertEqual(6, solution.sum_of_digits(123))
        self.assertEqual(6, solution.sum_of_digits(6))
        self.assertEqual(1, solution.sum_of_digits(-10))

if __name__ == '__main__':
    unittest.main()