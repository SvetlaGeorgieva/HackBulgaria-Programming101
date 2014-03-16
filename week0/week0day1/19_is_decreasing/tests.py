import solution
import unittest


class SolutionTest(unittest.TestCase):
    """Testing Problem 19 - Descreasing sequence? module"""
    def test_is_decreasing(self):
        self.assertEqual(True, solution.is_decreasing([5,4,3,2,1]))
        self.assertEqual(False, solution.is_decreasing([1,2,3]))
        self.assertEqual(True, solution.is_decreasing([100, 50, 20]))
        self.assertEqual(False, solution.is_decreasing([1,1,1,1]))


if __name__ == '__main__':
    unittest.main()