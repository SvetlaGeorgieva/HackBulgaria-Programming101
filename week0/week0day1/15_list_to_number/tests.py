import solution
import unittest


class SolutionTest(unittest.TestCase):
    """Testing Problem 15 - Turn a list of digits into a number module"""
    def test_list_to_number(self):
        self.assertEqual(123, solution.list_to_number([1,2,3]))
        self.assertEqual(99999, solution.list_to_number([9,9,9,9,9]))
        self.assertEqual(123023, solution.list_to_number([1,2,3,0,2,3]))


if __name__ == '__main__':
    unittest.main()