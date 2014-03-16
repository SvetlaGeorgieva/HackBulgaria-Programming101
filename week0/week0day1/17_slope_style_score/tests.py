import solution
import unittest


class SolutionTest(unittest.TestCase):
    """Testing Problem 17 - Slope style score module"""
    def test_slope_style_score(self):
        self.assertEqual(94.66, solution.slope_style_score([94, 95, 95, 95, 90]))
        self.assertEqual(80.0, solution.slope_style_score([60, 70, 80, 90, 100]))
        self.assertEqual(93.5, solution.slope_style_score([96, 95.5, 93, 89, 92]))


if __name__ == '__main__':
    unittest.main()