import solution
import unittest


class SolutionTest(unittest.TestCase):
    """Testing Problem 4 - Check if integer is prime module"""
    def test_is_prime(self):
        self.assertEqual(False, solution.is_prime(1))
        self.assertEqual(True, solution.is_prime(2))
        self.assertEqual(False, solution.is_prime(8))
        self.assertEqual(True, solution.is_prime(11))
        self.assertEqual(False, solution.is_prime(-10))


if __name__ == '__main__':
    unittest.main()