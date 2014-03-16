import solution
import unittest


class SolutionTest(unittest.TestCase):
    """Testing Problem 14 - Turn a number into a list of digits module"""
    def test_number_to_list(self):
        self.assertEqual([1, 2, 3], solution.number_to_list(123))
        self.assertEqual([9, 9, 9, 9, 9], solution.number_to_list(99999))
        self.assertEqual([1, 2, 3, 0, 2, 3], solution.number_to_list(123023))


if __name__ == '__main__':
    unittest.main()