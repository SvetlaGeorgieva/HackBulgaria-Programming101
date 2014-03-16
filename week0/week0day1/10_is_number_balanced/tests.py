import solution
import unittest


class SolutionTest(unittest.TestCase):
    """Testing Problem 10 - Is number balanced? module"""
    def test_is_number_balanced(self):
        self.assertEqual(True, solution.is_number_balanced(9))
        self.assertEqual(True, solution.is_number_balanced(11))
        self.assertEqual(False, solution.is_number_balanced(13))
        self.assertEqual(True, solution.is_number_balanced(121))
        self.assertEqual(True, solution.is_number_balanced(4518))
        self.assertEqual(False, solution.is_number_balanced(28471))
        self.assertEqual(True, solution.is_number_balanced(1238033))


if __name__ == '__main__':
    unittest.main()