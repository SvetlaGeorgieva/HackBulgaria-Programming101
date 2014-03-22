import solution
import unittest


class SolutionTest(unittest.TestCase):
    """Testing Problem 3 - Sum all divisors of an integer module"""
    def test_sum_of_divisors(self):
        self.assertEqual(15, solution.sum_of_divisors(8))
        self.assertEqual(8, solution.sum_of_divisors(7))
        self.assertEqual(1, solution.sum_of_divisors(1))
        self.assertEqual(2340, solution.sum_of_divisors(1000))


if __name__ == '__main__':
    unittest.main()