import solution
import unittest


class SolutionTest(unittest.TestCase):
    """Testing Problem 6 - Are there n sevens in a row? module"""
    def test_sevens_in_a_row(self):
        self.assertEqual(True, solution.sevens_in_a_row([10,8,7,6,7,7,7,20,-7], 3))
        self.assertEqual(False, solution.sevens_in_a_row([1,7,1,7,7], 4))
        self.assertEqual(True, solution.sevens_in_a_row([7,7,7,1,1,1,7,7,7,7], 3))
        self.assertEqual(True, solution.sevens_in_a_row([7,2,1,6,2], 1))


if __name__ == '__main__':
    unittest.main()