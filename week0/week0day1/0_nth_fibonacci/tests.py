import solution
import unittest


class SolutionTest(unittest.TestCase):
    """Testing Problem 0 - N-th Fibonacci module"""
    def test_nth_fibonacci(self):
        self.assertEqual(1, solution.nth_fibonacci(1))
        self.assertEqual(1, solution.nth_fibonacci(2))
        self.assertEqual(2, solution.nth_fibonacci(3))
        self.assertEqual(55, solution.nth_fibonacci(10))


if __name__ == '__main__':
    unittest.main()