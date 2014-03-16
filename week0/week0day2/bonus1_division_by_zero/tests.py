import solution
import unittest


class SolutionTest(unittest.TestCase):
    """Testing Bonus Round 1 - Division by zero module"""
    def test_division_by_zero(self):
        self.assertEqual(3, solution.division_by_zero([9, 2]))
        self.assertEqual(3, solution.division_by_zero([8, 2]))
        self.assertEqual(1, solution.division_by_zero([50]))
        self.assertEqual(11, solution.division_by_zero([1, 5, 8, 30, 15, 4]))
        self.assertEqual(7, solution.division_by_zero([1, 2, 4, 8, 16, 32, 64]))
        self.assertEqual(7, solution.division_by_zero([6, 2, 18]))


if __name__ == '__main__':
    unittest.main()