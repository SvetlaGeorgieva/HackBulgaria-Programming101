import solution
import unittest


class SolutionTest(unittest.TestCase):
    """Testing Problem 18 - Increasing sequence? module"""
    def test_is_increasing(self):
        self.assertEqual(True, solution.is_increasing([1,2,3,4,5]))
        self.assertEqual(True, solution.is_increasing([1]))
        self.assertEqual(False, solution.is_increasing([5,6,-10]))
        self.assertEqual(False, solution.is_increasing([1,1,1,1]))


if __name__ == '__main__':
    unittest.main()