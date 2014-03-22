import solution
import unittest


class SolutionTest(unittest.TestCase):
    """Testing Problem 16 - Biggest difference between two numbers module"""
    def test_biggest_difference(self):
        self.assertEqual(-1, solution.biggest_difference([1,2]))
        self.assertEqual(-4, solution.biggest_difference([1,2,3,4,5]))
        self.assertEqual(-9, solution.biggest_difference([-10, -9, -1]))
        self.assertEqual(-99, solution.biggest_difference(range(100)))


if __name__ == '__main__':
    unittest.main()